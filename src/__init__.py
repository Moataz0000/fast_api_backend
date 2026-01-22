from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.db.main import init_db

from .books.routes import book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("Server is Stopping...")


version = "v1"

app = FastAPI(
    title="Bookly",
    description="A RESTful API for a book review web service",
    version=version,
    lifespan=lifespan,
)

app.include_router(book_router, prefix=f"/api/{version}/book", tags=["books"])
