import json
import httpx
from datetime import datetime

class Book:
    def __init__(self, title: str, author: str, isbn: str, publication_year: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Yayin_Yili: {self.publication_year})"

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, isbn: str):
    # ISBN doğrulama
        if not (10 <= len(isbn) <= 13) or not isbn.isdigit():
            print("Geçersiz ISBN. 10-13 haneli olmalıdır.")
            return False

        # Kitabın varlığını kontrol etme
        if self.find_book(isbn):
            print("Bu ISBN'li kitap kütüphanede zaten var.")
            return False

        # Açık Kütüphane API'sinden kitap verilerini follow_redirects=True ile alın
        try:
            response = httpx.get(
                f"https://openlibrary.org/isbn/{isbn}.json",
                follow_redirects=True,  # Otomatik yönlendirmeyi etkinleştir
                timeout=10
            )
            response.raise_for_status()
            book_data = response.json()

            title = book_data.get("title", "Unknown Title")
            
            # Yazarları yönet (list veya dict olabilir)
            authors = book_data.get("authors", [])
            if authors and isinstance(authors[0], dict):
                author_key = authors[0].get("key", "/authors/OL0A")
                try:
                    author_response = httpx.get(
                        f"https://openlibrary.org{author_key}.json",
                        follow_redirects=True,
                        timeout=5
                    )
                    author_data = author_response.json()
                    author = author_data.get("name", "Unknown Author")
                except:
                    author = "Unknown Author"
            else:
                author = ", ".join(authors) if authors else "Unknown Author"

            # Yayın yılını getir (farklı formatları yönet)
            publish_date = book_data.get("publish_date", "")
            if isinstance(publish_date, list):
                publish_date = publish_date[0]
            
            # Tarih stringinden yılı çıkar
            current_year = datetime.now().year
            publication_year = current_year  # varsayılan
            
            # Yayın yılında 4 hane bulmaya çalış
            if publish_date:
                for part in publish_date.split():
                    if part.isdigit() and len(part) == 4:
                        year = int(part)
                        if 1400 <= year <= current_year:
                            publication_year = year
                            break

            # Yayın yılını doğrula
            if not (1400 <= publication_year <= current_year):
                print(f"Geçersiz yayın yılı: {publication_year}. 1400 ve {current_year} arasında olmalıdır.")
                return False

            # Kitap oluştur ve ekle
            new_book = Book(title, author, isbn, publication_year)
            self.books.append(new_book)
            self.save_books()
            print(f"Kitap başarıyla eklendi: {new_book}")
            return True

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                print("Kitap Open Library'de bulunamadı.")
            else:
                print(f"API Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        return False

    def remove_book(self, isbn: str):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Kitap silindi: {book.title}")
            return True
        print("Kitap bulunamadı.")
        return False

    def list_books(self):
        if not self.books:
            print("Kütüphane boş.")
            return
        
        print("\nKütüphanede Bulunan Kitaplar:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def find_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                books_data = json.load(f)
                self.books = [
                    Book(
                        book["title"],
                        book["author"],
                        book["isbn"],
                        book["publication_year"]
                    ) for book in books_data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        books_data = [
            {
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "publication_year": book.publication_year
            } for book in self.books
        ]
        with open(self.filename, "w") as f:
            json.dump(books_data, f, indent=2)