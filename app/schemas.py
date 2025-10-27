from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    author: str = Field(min_length=2, max_length=100)
    genre: str = Field(min_length=2, max_length=100)
    year: int = Field(ge=0, le=2100)
    rating: float = Field(ge=0.0, le=5.0)

class BookResponse(BookCreate):
    id: int
    title: str
    author: str

    class Config:
        from_attributes = True
