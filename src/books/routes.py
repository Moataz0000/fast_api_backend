from typing import List

from fastapi import APIRouter, HTTPException, status

from .book_data import BOOKS
from .schemas import Book, BookUpdate

book_router = APIRouter()


@book_router.get("/list", response_model=List[Book])
async def get_all_books():
    return BOOKS


@book_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    BOOKS.book_routerend(new_book)
    return new_book


@book_router.get("/{book_id}/detail")
async def get_book_by_id(book_id: int) -> dict:
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The book with this id '{book_id}' is not found.",
    )


@book_router.put("/{book_id}/update")
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


@book_router.delete("/{book_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
async def remove_book(book_id: int) -> None:
    for book in BOOKS:
        if book["id"] == book_id:
            BOOKS.remove(book)

            return {}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The book with this id '{book_id}' is not found.",
    )
