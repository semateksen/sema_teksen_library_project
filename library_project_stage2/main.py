from library import Library

def main():
    library = Library()
    
    while True:
        print("\nKütüphane Uygulaması")
        print("1. Kitap Ekle (ISBN ile)")
        print("2. Kitap Sil (ISBN ile)")
        print("3. Kitapları Listele")
        print("4. Kitap Ara (ISBN ile)")
        print("5. Çıkış")
        
        choice = input("Seçiminizi yapınız (1-5): ")
        
        if choice == "1":
            isbn = input("ISBN giriniz (10-13 haneli): ").strip()
            library.add_book(isbn)
            
        elif choice == "2":
            isbn = input("Silinecek kitabın ISBN'ini giriniz: ").strip()
            library.remove_book(isbn)
            
        elif choice == "3":
            library.list_books()
            
        elif choice == "4":
            isbn = input("Aranacak kitabın ISBN'ini giriniz: ").strip()
            book = library.find_book(isbn)
            if book:
                print("\nKitap bulundu:")
                print(book)
            else:
                print("Kitap bulunamadı.")
                
        elif choice == "5":
            print("Sistemden çıkılıyor...")
            break
            
        else:
            print("Geçersiz seçim. Lütfen 1-5 arası rakam giriniz.")

if __name__ == "__main__":
    main()