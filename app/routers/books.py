from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.dependency import get_db


from app.models import Book
from app.schemas import BookCreate, BookResponse

router = APIRouter(tags=['Book Management'])


@router.post('/books', response_model=BookResponse)
def create_book(book: BookCreate, session: Session = Depends(get_db)):
    new_book = Book(
        title=book.title,
        author=book.author,
        genre=book.genre,
        year=book.year,
        rating=book.rating
    )
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book


@router.get("/books", response_model=List[BookResponse])
def get_all_books(session: Session = Depends(get_db)):
    books = session.query(Book).all()
    return books


@router.get('/books/{book_id}', response_model=BookResponse)
def get_one_book(book_id: int, session: Session = Depends(get_db)):
    searched_book = session.query(Book).filter(Book.id == book_id).first()
    if not searched_book:
        raise HTTPException(status_code=404, detail='Book not found')
    return searched_book


@router.delete('/books/{book_id}', response_model=BookResponse)
def delete_book(book_id: int, session: Session = Depends(get_db)):
    deleting_book = session.query(Book).filter(Book.id == book_id).first()
    if not deleting_book:
        raise HTTPException(status_code=404, detail='Book not found')

    session.delete(deleting_book)
    session.commit()
    return deleting_book
