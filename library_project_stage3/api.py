from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import httpx
import json
from datetime import datetime

app = FastAPI()

# Pydantic modelleri
class Book(BaseModel):
    title: str
    author: str
    isbn: str
    publication_year: int

class ISBNInput(BaseModel):
    isbn: str

# Library sınıfını uyarlama
class LibraryAPI:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                books_data = json.load(f)
                self.books = books_data
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump(self.books, f, indent=2)

    async def add_book(self, isbn: str):
        if not (10 <= len(isbn) <= 13) or not isbn.isdigit():
            raise HTTPException(status_code=400, detail="Invalid ISBN format")

        if any(book['isbn'] == isbn for book in self.books):
            raise HTTPException(status_code=400, detail="Book already exists")

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"https://openlibrary.org/isbn/{isbn}.json",
                    follow_redirects=True,
                    timeout=10.0
                )
                response.raise_for_status()
                book_data = response.json()

                title = book_data.get("title", "Unknown Title")
                
                authors = book_data.get("authors", [])
                if authors and isinstance(authors[0], dict):
                    author_key = authors[0].get("key", "/authors/OL0A")
                    author_response = await client.get(
                        f"https://openlibrary.org{author_key}.json",
                        follow_redirects=True,
                        timeout=5.0
                    )
                    author_data = author_response.json()
                    author = author_data.get("name", "Unknown Author")
                else:
                    author = ", ".join(authors) if authors else "Unknown Author"

                publish_date = book_data.get("publish_date", "")
                current_year = datetime.now().year
                publication_year = current_year
                
                if publish_date:
                    for part in str(publish_date).split():
                        if part.isdigit() and len(part) == 4:
                            year = int(part)
                            if 1400 <= year <= current_year:
                                publication_year = year
                                break

                new_book = {
                    "title": title,
                    "author": author,
                    "isbn": isbn,
                    "publication_year": publication_year
                }
                
                self.books.append(new_book)
                self.save_books()
                return new_book

        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=404, detail="Book not found in Open Library")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def remove_book(self, isbn: str):
        for i, book in enumerate(self.books):
            if book['isbn'] == isbn:
                removed_book = self.books.pop(i)
                self.save_books()
                return removed_book
        raise HTTPException(status_code=404, detail="Book not found")

library = LibraryAPI()

# API Endpoint'leri
@app.get("/books", response_model=List[Book])
async def list_books():
    return library.books

@app.post("/books", response_model=Book)
async def add_book(isbn_input: ISBNInput):
    return await library.add_book(isbn_input.isbn)

@app.delete("/books/{isbn}")
async def delete_book(isbn: str):
    return library.remove_book(isbn)