from fastapi import FastAPI

from app.database import Base, engine
from app.models import Book
from app.routers.books import router as books_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = 'Book-Management'
)


app.include_router(books_router)
