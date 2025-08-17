# 📚 Kütüphane Yönetim Sistemi - Python 202 Bootcamp Projesi

## 🌟 Proje Açıklaması
Bu proje, Global AI Hub Python 202 Bootcamp kapsamında geliştirilmiş 3 aşamalı bir kütüphane yönetim sistemidir. Her aşamada proje daha fazla geliştirilerek:

1️⃣ **Terminal uygulaması** →  
2️⃣ **Harici API entegrasyonlu uygulama** →  
3️⃣ **Tam teşekküllü web API'si** haline getirilmiştir.

## 📦 Kurulum

### 1. Gereksinimler
- Python 3.8+
- Git (opsiyonel)

### 2. Projeyi Bilgisayarınıza Alın
```bash
git clone https://github.com/semateksen/sema_teksen_library_project.git
cd sema_teksen_library_project
# Not: İlerleyen süreçte aşamalar test edilecektir. Örn: cd library_project_stage1 ile geçiş yapılarak aşama 1 için işlemler ve testler yapılır.
# Aşama 1 ile ilgili işlemleri yaptıktan sonra cd .. ile "sema_teksen_library_project" üst dizinine geçilir.
# Sonra test etmek istediğimiz yeni aşamaya (cd library_project_stage2 veya cd library_project_stage3) ile geçilir.
# Öncelikle aşağıdaki şekilde sanal ortam oluşturulur ve bağımlılıklar yüklenir.
```

### 3. Sanal Ortam Oluşturun (Önerilir)
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 4. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

## 🚀 Aşamalar ve Kullanım

### 🔹 Aşama 1: Temel Terminal Uygulaması
**Dizin:** `library_project_stage1/`

```bash
cd library_project_stage1
python main.py
```

**Özellikler:**
- ✔️ Kitap ekleme/silme/listeleme
- ✔️ Verilerin JSON'da saklanması (`library.json`)
- ✔️ OOP yapısı (Book ve Library sınıfları)

**Menü:**
```
1. Kitap Ekle
2. Kitap Sil
3. Kitapları Listele
4. Kitap Ara
5. Çıkış
```

### 🔹 Aşama 2: Open Library API Entegrasyonu
**Dizin:** `library_project_stage2/`

```bash
cd library_project_stage2
python main.py
```

**Yeni Özellikler:**
- 🌐 Open Library API bağlantısı
- 🔍 Sadece ISBN girerek kitap bilgilerini otomatik çekme
- ✔️ ISBN doğrulama (10-13 hane)
- 📅 Yayın yılı kontrolü (1400-günümüz yılı)
- ⚠️ Hata yönetimi geliştirmeleri

**Örnek Kullanım:**
```
Seçiminizi yapınız (1-5): 4
Aranacak kitabın ISBN'ini giriniz: 9780061120084

Kitap bulundu:
To Kill a Mockingbird by Harper Lee (ISBN: 9780061120084, Yayin_Yili: 2006)
```

### 🔹 Aşama 3: FastAPI Web Servisi
**Dizin:** `library_project_stage3/`

```bash
cd library_project_stage3
uvicorn api:app --reload
# Tarayıcıda http://localhost:8000/docs sayfasına gidilir.
# Kitaplar için GET (Listeleme), POST (Ekleme) ve DELETE (Silme) işlemleri açılan bu Swagger UI ortamında yapılabilir.
```

**Özellikler:**
- 🚀 RESTful API endpoint'leri
- 📚 Otomatik dokümantasyon (Swagger UI ve ReDoc)
- ⚡ Async işlemler
- 🔒 Pydantic veri doğrulama

**API Endpoint'leri:**
| Method | Endpoint          | Açıklama                     | Örnek İstek                  |
|--------|-------------------|------------------------------|------------------------------|
| GET    | `/books`          | Tüm kitapları listeler       | `GET /books`                 |
| POST   | `/books`          | Yeni kitap ekler             | `POST /books {"isbn":"..."}` |
| DELETE | `/books/{isbn}`   | Kitap siler                  | `DELETE /books/9780061120084`|

## 🧪 Testler

### Aşama 1-2 Testleri
```bash
cd library_project_stage1
pytest tests/test_library.py -v
# cd library_project_stage2
# pytest test_library.py -v
```

### Aşama 3 Testleri
```bash
cd library_project_stage3
pytest test_api.py -v
```

### Testlerin Görseli (Sırasıyla Aşama 1-2-3 için)

<img width="1906" height="1102" alt="tests" src="https://github.com/user-attachments/assets/89e5bfb7-5191-4246-b45d-6e8ff28b4cf2" />


## 📂 Proje Yapısı

```
sema_teksen_library_project/
├── library_project_stage1/
│   ├── main.py
│   ├── models/
│   │   ├── book.py
│   │   ├── library.py          
│   ├── tests/
│   │   ├── test_library.py
│   └── library.json (otomatik oluşur)
├── library_project_stage2/
│   ├── main.py
│   ├── library.py
│   ├── test_library.py
│   └── library.json
├── library_project_stage3/
│   ├── api.py
│   ├── test_api.py
│   └── library.json
│── README.md          # Hem genel hem de aşamalar özelinde README.md dosyaları oluşturuldu.
└── requirements.txt   # Bu dosya da hem genelde hem de aşamalar özelinde tutuldu.
```

## 💡 Kullanım Örnekleri

### Terminal Uygulaması (Aşama 1-2)
```python
# Kitap ekleme örneği (Aşama 1 için)
--- Kütüphane Uygulaması ---
1. Kitap Ekle
2. Kitap Sil
3. Kitapları Listele
4. Kitap Ara
5. Çıkış
Seçiminizi yapınız (1-5): 1
Kitap başlığı: To Kill a Mockingbird
Yazar: Harper Lee
ISBN: 9780061120084
Kitap başarıyla eklendi.

# Kitap ekleme örneği (Aşama 2 için)
Seçiminizi yapınız (1-5): 1
ISBN giriniz (10-13 haneli): 9780061120084
Kitap başarıyla eklendi: To Kill a Mockingbird by Harper Lee (ISBN: 9780061120084, Yayin_Yili: 2006)
```

### API Kullanımı (Aşama 3)
```bash
# Kitap ekleme
curl -X POST "http://localhost:8000/books" \
-H "Content-Type: application/json" \
-d "{\"isbn\":\"9780061120084\"}"

# Kitapları listeleme
curl "http://localhost:8000/books"
```

## 🔧 Karşılaşılan Sorunlar ve Çözümler

| Sorun | Çözüm |
|-------|-------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `uvicorn: command not found` | Sanal ortamı aktive edin |
| Port çakışması | `uvicorn api:app --port 8001` |
| API yanıt vermiyor | `--reload` parametresini kaldırın |
| Testler başarısız | `library.json` dosyasını temizleyin |

## 🤝 Katkıda Bulunma
1. Repoyu fork edin
2. Yeni branch oluşturun (`git checkout -b feature/benim-ozelligim`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'i pushlayın (`git push origin feature/benim-ozelligim`)
5. Pull Request açın
---

**Not:** Projeyi çalıştırmadan önce ilgili aşamanın dizinine gidip sanal ortamı aktive etmeyi unutmayın.
