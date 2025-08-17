import pytest
import os
import json
from library import Book, Library

@pytest.fixture
def sample_book():
    return Book("Test Book", "Test Author", "1234567890", 2020)

@pytest.fixture
def temp_library(tmp_path):
    filename = tmp_path / "test_library.json"
    lib = Library(filename=str(filename))
    yield lib
    if os.path.exists(filename):
        os.remove(filename)

def test_book_str(sample_book):
    assert str(sample_book) == "Test Book by Test Author (ISBN: 1234567890, Yayin_Yili: 2020)"

def test_library_add_remove(temp_library, sample_book):
    # Test adding
    temp_library.books.append(sample_book)
    temp_library.save_books()
    
    # Test loading
    new_lib = Library(filename=temp_library.filename)
    assert len(new_lib.books) == 1
    assert new_lib.books[0].title == "Test Book"
    
    # Test removing
    temp_library.remove_book("1234567890")
    assert len(temp_library.books) == 0

def test_find_book(temp_library, sample_book):
    temp_library.books.append(sample_book)
    found = temp_library.find_book("1234567890")
    assert found is not None
    assert found.title == "Test Book"
    
    not_found = temp_library.find_book("0000000000")
    assert not_found is None

def test_invalid_isbn(temp_library):
    # Too short
    assert not temp_library.add_book("123")
    # Too long
    assert not temp_library.add_book("12345678901234")
    # Non-digit
    assert not temp_library.add_book("ABCDEFGHIJ")