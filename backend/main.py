from typing import List

from books import BOOKS
from fastapi import FastAPI, HTTPException, status
from schema import Book, BookUpdate

app = FastAPI(
    title="Book App",
    description="A fully CRUD backend app.",
    version="0.0.1",
)


@app.get("/")
async def root():
    return {"message": "Hello, I'm A Book App."}


@app.get("/api/book/list", response_model=List[Book])
async def get_all_books():
    return BOOKS


@app.post("/api/book/create", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    BOOKS.append(new_book)
    return new_book


@app.get("/api/book/{book_id}/detail")
async def get_book_by_id(book_id: int) -> dict:
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The book with this id '{book_id}' is not found.",
    )


@app.put("/api/book/{book_id}/update")
async def update_book(book_id: int, book_updated_data: BookUpdate) -> dict:
    for book in BOOKS:
        if book["id"] == book_id:
            book["title"] == book_updated_data.title
            book["publisher"] == book_updated_data.publisher
            book["page_count"] == book_updated_data.page_count
            book["language"] == book_updated_data.language

            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The book with this id '{book_id}' is not found.",
    )


@app.delete("/api/book/{book_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
async def remove_book(book_id: int) -> None:
    for book in BOOKS:
        if book["id"] == book_id:
            BOOKS.remove(book)

            return {}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The book with this id '{book_id}' is not found.",
    )
