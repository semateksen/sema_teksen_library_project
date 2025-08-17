import json
import os
from models.book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book.from_dict(item) for item in data]
        else:
            self.books = []

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def add_book(self, book: Book):
        if self.find_book(book.isbn):
            print("Bu ISBN'e sahip bir kitap zaten mevcut.")
            return
        self.books.append(book)
        self.save_books()
        print("Kitap başarıyla eklendi.")

    def remove_book(self, isbn: str):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            print("Kitap silindi.")
        else:
            print("Kitap bulunamadı.")

    def list_books(self):
        if not self.books:
            print("Kütüphane boş.")
        for book in self.books:
            print(book)

    def find_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None