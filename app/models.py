from sqlalchemy import Column, Integer, String, Numeric, CheckConstraint

from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(200), nullable=False)
    genre = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Numeric(2,1), CheckConstraint("rating >= 0.0 AND rating <= 5.0"), nullable=False )

