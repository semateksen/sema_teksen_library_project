# 📚 Kütüphane Yönetim Sistemi - 2. Aşama (Harici API ile Veri Zenginleştirme)

Bu proje, Global AI Hub Python 202 Bootcamp kapsamında geliştirilmiş bir Kütüphane Yönetim Sistemidir. Sistem, kitapları ISBN numaralarıyla takip edebilen, Open Library API entegrasyonu bulunan ve verileri JSON formatında saklayan bir konsol uygulamasıdır.

## 🌟 Özellikler

- **Kitap Ekleme**: ISBN numarasıyla Open Library API'den otomatik kitap bilgisi çekme
- **Kitap Silme**: ISBN numarasıyla kitap kaldırma
- **Kitap Listeleme**: Tüm kitapları detaylı şekilde görüntüleme
- **Kitap Arama**: ISBN ile kitap arama
- **Veri Kalıcılığı**: Tüm veriler JSON dosyasında saklanır
- **ISBN Doğrulama**: 10-13 haneli ISBN kontrolü
- **Yayın Yılı Kontrolü**: 1400-günümüz yılı aralığında yayın yılı kontrolü

## 📂 Proje Yapısı


    library-project/
    │── library.py              # Ana kütüphane kodu
    │── main.py                 # Çalıştırılacak ana dosya
    │── test_library.py         # Testler
    │── requirements.txt        # Gereken paketler
    │── library.json            # Kitapların kaydedildiği dosya (otomatik oluşur)  
    │── README.md               # Proje açıklama dosyası


## 🛠️ Kurulum

### Ön Koşullar
- Python 3.8 veya üzeri
- pip paket yöneticisi

### Adım Adım Kurulum

1. **Repoyu Klonlama**:
   ```bash
   git clone https://github.com/semateksen/sema_teksen_library_project.git
   cd sema_teksen_library_project/library_project_stage2
   ```

2. **Sanal Ortam Oluşturma (Opsiyonel ama Tavsiye Edilir)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. **Gerekli Paketlerin Yüklenmesi**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Kullanım

### Terminal Uygulamasını Çalıştırma

Proje dizinindeyken aşağıdaki komutu çalıştırın:

```bash
python main.py
```

### Menü Seçenekleri

Uygulama başladığında aşağıdaki menüyü göreceksiniz:

```
Kütüphane Uygulaması
1. Kitap Ekle (ISBN ile)
2. Kitap Sil (ISBN ile)
3. Kitapları Listele
4. Kitap Ara (ISBN ile)
5. Çıkış
Seçiminizi yapınız (1-5): 
```

#### 1. Kitap Ekleme
Sadece ISBN numarasını girin (10-13 haneli). Sistem:
- ISBN geçerliliğini kontrol eder
- Kitabın kütüphanede olup olmadığını kontrol eder
- Open Library API'den kitap bilgilerini çeker
- Yayın yılını kontrol eder
- Kitabı kütüphaneye ekler

Örnek:
```
ISBN giriniz (10-13 haneli): 9780061120084
Kitap başarıyla eklenmiştir: To Kill a Mockingbird by Harper Lee (ISBN: 9780061120084, Published: 1960)
```

#### 2. Kitap Silme
Silmek istediğiniz kitabın ISBN numarasını girin.

#### 3. Kitapları Listeleme
Kütüphanedeki tüm kitapları listeler.

#### 4. Kitap Arama
ISBN ile kitap arama yapar.

#### 5. Çıkış
Uygulamadan çıkar.

## � Karşılaşılabilecek Sorunlar ve Çözümler

1. **API Error: 302 Found Hatası**:
   - Sebep: Open Library bazı ISBN'ler için yönlendirme yapıyor
   - Çözüm: Kodun en güncel versiyonunu kullanın (`follow_redirects=True` parametresi eklendi)

2. **Kitap Bulunamadı Hatası**:
   - Sebep: ISBN Open Library'de kayıtlı değil veya API geçici olarak ulaşılamıyor
   - Çözüm: ISBN'i kontrol edip tekrar deneyin veya farklı bir ISBN deneyin

3. **Geçersiz Yayın Yılı**:
   - Sebep: API'den gelen yayın yılı 1400'den küçük veya güncel yıldan büyük
   - Çözüm: Sistem otomatik olarak güncel yılı atayacaktır

## 🤝 Katkıda Bulunma

Katkıda bulunmak isterseniz:
1. Repoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/your-feature`)
3. Değişikliklerinizi commit edin (`git commit -am 'Add some feature'`)
4. Branch'i pushlayın (`git push origin feature/your-feature`)
5. Pull Request açın

---