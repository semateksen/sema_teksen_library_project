# 📚 Kütüphane Yönetim Sistemi (OOP Projesi)

## 📌 Proje Açıklaması

Bu proje, **Python Nesne Yönelimli Programlama (OOP)** prensiplerini
kullanarak oluşturulmuş basit bir kütüphane yönetim sistemidir.\
Kullanıcılar kitap ekleyebilir, silebilir, listeleyebilir ve kitaplar
arasında arama yapabilir.\
Veriler **JSON dosyasında** saklanır ve program yeniden
çalıştırıldığında yüklenir.

------------------------------------------------------------------------

## 🎯 Amaç

-   Python OOP mantığını uygulamak
-   Sınıflar, nesneler, metotlar ve kalıtımı kullanmak
-   Dosya okuma/yazma (JSON) işlemleri ile veri kalıcılığını sağlamak

------------------------------------------------------------------------

## 🛠 Kullanılan Teknolojiler

-   **Python 3.x**
-   **JSON** veri saklama formatı
-   **Pytest** ile testler

------------------------------------------------------------------------

## 📂 Proje Klasör Yapısı

    library-project/
    │── main.py                 # Programın ana çalıştırma dosyası
    │── models/
    │   ├── book.py             # Book sınıfı
    │   ├── library.py          # Library sınıfı
    │── library.json            # Kitap verilerinin saklandığı dosya 
    │── tests/
    │   ├── test_library.py     # Pytest test dosyaları
    │── README.md               # Proje açıklama dosyası

------------------------------------------------------------------------

## 📌 Sınıflar ve Görevleri

### **1. Book Sınıfı (`book.py`)**

-   Kitap bilgilerini tutar: `title`, `author`, `isbn`
-   `__str__` metodu ile kitap bilgisini döndürür

### **2. Library Sınıfı (`library.py`)**

-   Kitap ekleme, silme, listeleme ve arama işlemlerini yapar
-   Verileri JSON dosyasına kaydeder ve yükler

------------------------------------------------------------------------

## 🚀 Kullanım

### 1️⃣ Projeyi Klonla

``` bash
git clone https://github.com/semateksen/sema_teksen_library_project.git
cd sema_teksen_library_project/library_project_stage1
```

### 2️⃣ Programı Çalıştır

``` bash
python main.py
```

### 3️⃣ Örnek Çıktı

--- Kütüphane Uygulaması ---
1. Kitap Ekle
2. Kitap Sil
3. Kitapları Listele
4. Kitap Ara
5. Çıkış
Seçiminizi yapınız (1-5): 1
Kitap başlığı: Sefiller
Yazar: Victor Hugo
ISBN: 9789750703270
Kitap başarıyla eklendi.


**1. Kitap Ekle:** Yukarıdaki şekilde ana menüden 1 seçimi ile seçilir ve kitap kaydı library.json dosyasına eklenir.

Not: Aynı ISBN numarasına ait bir kitap daha kaydedilmek istenirse:
"Bu ISBN'e sahip bir kitap zaten mevcut." ibaresi gelir ve yeni kayıt oluşmaz.


**2. Kitap Sil:** 2 seçimi ile seçilir.
"Silinecek kitabın ISBN numarası" sorulur. Kayıtlı olmayan bir ISBN numarası girilirse veya boş geçilirse:
"Kitap bulunamadı." ibaresi gelir ve ardından "Kütüphane Uygulaması" ana menüsüne gelir.

Kayıtlı bir kitabın ISBN numarası girilirse:
"Kitap silindi." ibaresi gelir ve kitap library.json dosyasından silinir ve "Kütüphane Uygulaması" ana menüsü gelir.


**3. Kitapları Listele:** 3 seçimi ile seçilir. Kayıtlı kitapları listeler. Kayıtlı kitap yoksa "Kütüphane boş." ibaresi gelir ve ardından ana menü gelir.


**4. Kitap Ara:** 4 seçimi ile seçilir. Kayıtlı kitaplar arasından ISBN numarasına göre kitabı bulup, "Kitap bulundu:" ibaresiyle bilgilerini getirir.
Aratılan ISBN numarasına ait bir kitap kaydı yoksa "Kitap bulunamadı." ibaresini döner ve ardından ana menü gelir.


**5. Çıkış:** 5 seçimi ile seçilir.
"Programdan çıkılıyor..." ibaresiyle "Kütüphane Uygulaması" menüsünden çıkış yapar.

------------------------------------------------------------------------

## 🧪 Test Çalıştırma

Pytest ile testleri çalıştırmak için:

``` bash
pytest tests/test_library.py
```

Başarılı olduğunda tüm testlerden geçer yoksa hata verir. İstenirse tüm testlerden başarıyla geçtiğine dair kullanıcıya bir mesaj da gösterilebilir.

------------------------------------------------------------------------

## 📌 Geliştirme Fikirleri (Henüz yapılmadı.)

-   Kitapları **kategoriye göre filtreleme**
-   Kullanıcı giriş sistemi ekleme
-   SQLite veritabanı desteği
-   Web arayüzü (Flask/Django)
