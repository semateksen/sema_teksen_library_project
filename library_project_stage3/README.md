# 📚 Kütüphane Yönetim Sistemi - FastAPI (Aşama 3)

## 🌟 Proje Açıklaması
Bu proje, Global AI Hub Python 202 Bootcamp kapsamında geliştirilmiş 3 aşamalı bir kütüphane yönetim sistemidir. Aşama 3'te, önceki aşamalarda geliştirilen terminal uygulaması FastAPI ile bir web servisine dönüştürülmüştür. Sistem kitapları ISBN numaralarıyla takip edebilir, Open Library API entegrasyonu bulunur ve verileri JSON formatında saklar.

## 🛠️ Kurulum

### 1. Repoyu Klonlama
```bash
git clone https://github.com/semateksen/sema_teksen_library_project.git
cd sema_teksen_library_project/library_project_stage3
```

### 2. Sanal Ortam Oluşturma ve Aktif Etme
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Bağımlılıkları Yükleme
```bash
pip install -r requirements.txt
```

### Gereklilikler (requirements.txt)
```
fastapi>=0.68.0
uvicorn>=0.15.0
httpx>=0.19.0
pydantic>=1.8.0
```

## 🚀 Kullanım

### Aşama 1-2: Terminal Uygulaması
```bash
python main.py
```

### Aşama 3: API Sunucusu
```bash
uvicorn api:app --reload
```

Sunucu başladıktan sonra tarayıcınızda şu adrese gidin:
```
http://localhost:8000/docs
```

## 📡 API Dokümantasyonu

### Temel Endpoint'ler

| Endpoint | Method | Açıklama | Örnek İstek |
|----------|--------|----------|-------------|
| `/books` | GET | Tüm kitapları listeler | `GET http://localhost:8000/books` |
| `/books` | POST | Yeni kitap ekler | `POST http://localhost:8000/books`<br>Body: `{"isbn": "9780061120084"}` |
| `/books/{isbn}` | DELETE | Belirtilen ISBN'e sahip kitabı siler | `DELETE http://localhost:8000/books/9780061120084` |

### Örnek API İstekleri

**1. Kitap Ekleme (POST):**
```bash
curl -X POST "http://localhost:8000/books" \
-H "Content-Type: application/json" \
-d "{\"isbn\":\"9780061120084\"}"
```

**2. Kitapları Listeleme (GET):**
```bash
curl "http://localhost:8000/books"
```

**3. Kitap Silme (DELETE):**
```bash
curl -X DELETE "http://localhost:8000/books/9780061120084"
```

## 🌐 API Dokümantasyon Arayüzleri

FastAPI otomatik olarak iki farklı dokümantasyon arayüzü sağlar:

1. **Swagger UI** (Interactive):
   ```
   http://localhost:8000/docs
   ```
   - Tüm endpoint'leri test edebileceğiniz interaktif arayüz
   - Örnek istekler oluşturabilirsiniz

2. **ReDoc** (Dokümantasyon):
   ```
   http://localhost:8000/redoc
   ```
   - Temiz ve düzenli API dokümantasyonu

## 🧪 Testler

API endpoint'lerini test etmek için:

```bash
pytest test_api.py -v
```

## 🔧 Karşılaşılabilecek Sorunlar ve Çözümleri

1. **Port Çakışması**:
   ```bash
   uvicorn api:app --port 8001 --reload
   ```

2. **CORS Hatası**:
   `api.py`'ye CORS middleware ekleyin:
   ```python
   from fastapi.middleware.cors import CORSMiddleware
   
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

3. **ModuleNotFoundError**:
   ```bash
   pip install -r requirements.txt
   ```

---

**Not:** API'yi kullanmadan önce sunucunun çalıştığından emin olun (`uvicorn api:app --reload`).