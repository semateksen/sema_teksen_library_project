from models.book import Book
from models.library import Library

def main():
    library = Library("library.json")

    while True:
        print("\n--- Kütüphane Uygulaması ---")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")

        choice = input("Seçiminizi yapınız (1-5): ")

        if choice == "1":
            title = input("Kitap başlığı: ")
            author = input("Yazar: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif choice == "2":
            isbn = input("Silinecek kitabın ISBN numarası: ")
            library.remove_book(isbn)

        elif choice == "3":
            library.list_books()

        elif choice == "4":
            isbn = input("Aranacak kitabın ISBN numarası: ")
            book = library.find_book(isbn)
            if book:
                print("Kitap bulundu:", book)
            else:
                print("Kitap bulunamadı.")

        elif choice == "5":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen 1-5 arasında bir değer girin.")

if __name__ == "__main__":
    main()
