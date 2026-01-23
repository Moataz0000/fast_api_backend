from sqlmodel import Session, SQLModel, create_engine

from src.config import Config

engine = create_engine(url=Config.DATABASE_URL, echo=True)


def init_db():
    print("Creating Database")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
