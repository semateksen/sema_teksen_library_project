import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Bu, tests klasöründen bir üst dizini (library_project) arama yoluna ekler.
import pytest
from models.book import Book
from models.library import Library

@pytest.fixture
def temp_library():
    # Test için geçici bir dosya kullan
    test_file = "test_library.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    lib = Library(filename=test_file)
    yield lib
    if os.path.exists(test_file):
        os.remove(test_file)

def test_add_book(temp_library):
    book = Book("Test Kitabı", "Test Yazar", "1234567890")
    temp_library.add_book(book)
    assert len(temp_library.books) == 1
    assert temp_library.books[0].title == "Test Kitabı"

def test_remove_book(temp_library):
    book = Book("Silinecek Kitap", "Yazar", "9876543210")
    temp_library.add_book(book)
    temp_library.remove_book("9876543210")
    assert len(temp_library.books) == 0

def test_find_book(temp_library):
    book = Book("Aranacak Kitap", "Yazar", "1122334455")
    temp_library.add_book(book)
    found = temp_library.find_book("1122334455")
    assert found is not None
    assert found.title == "Aranacak Kitap"

def test_list_books(temp_library, capsys):
    book1 = Book("Kitap1", "Yazar1", "111")
    book2 = Book("Kitap2", "Yazar2", "222")
    temp_library.add_book(book1)
    temp_library.add_book(book2)
    temp_library.list_books()
    captured = capsys.readouterr()
    assert "Kitap1" in captured.out
    assert "Kitap2" in captured.out
