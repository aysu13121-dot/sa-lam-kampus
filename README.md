# 💊 Sağlam Kampus - Python (FastAPI) Backend

**Sprint 1: Initial MVP Setup** tapşırığı çərçivəsində `Sağlam Kampus` platforması üçün hazırlanmış REST API servisi.

---

## 🚀 Layihəni İşə Salma Qaydası

### 1. Tələb olunan paketləri quraşdırın:
```bash
pip install -r requirements.txt
```

### 2. Serveri başladın:
```bash
python run.py
```
*(və ya birbaşa uvicorn ilə)*:
```bash
uvicorn app.main:app --reload --port 8000
```

### 3. İnteraktiv Sənədləşmə və Test İnterfeysi:
Server işə düşdükdən sonra brauzerdə açın:
* **Swagger UI (Canlı Test):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc Sənədləri:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* **Health Check:** [http://127.0.0.1:8000/api/health](http://127.0.0.1:8000/api/health)

---

## 📋 API Endpoint-ləri Cədvəli

| Metod | Endpoint | Təsvir | Giriş İcazəsi |
|---|---|---|---|
| `GET` | `/api/health` | Serverin statusunu yoxlamaq | Hər kəs |
| `POST` | `/api/auth/signup` | Yeni istifadəçi qeydiyyatı (Sign Up) | Hər kəs |
| `POST` | `/api/auth/login` | Sistemə giriş və JWT almaq (Login) | Hər kəs |
| `GET` | `/api/auth/me` | Cari istifadəçi məlumatları | Bearer Token |
| `GET` | `/api/categories` | Kataloq kateqoriyaları və ikonları | Hər kəs |
| `GET` | `/api/products` | Məhsulların siyahısı və ehtiyat statusu | Hər kəs |
| `GET` | `/api/products/{id}` | ID üzrə məhsul detalları | Hər kəs |
| `POST` | `/api/products` | Kataloqa yeni məhsul əlavə et | Bearer Token |
| `PATCH` | `/api/products/{id}/stock` | Məhsulun ehtiyat sayını yeniləmək | Bearer Token |
| `GET` | `/api/reviews` | Bütün rəylər və orta reytinq | Hər kəs |
| `POST` | `/api/reviews` | Yeni rəy/fikir göndərmək (Rəy formu) | Hər kəs |
| `POST` | `/api/orders` | Ehtiyat sifariş siyahısını təsdiqləmək | Hər kəs |
| `GET` | `/api/orders` | Bütün sifarişlərin siyahısı | Hər kəs |
| `GET` | `/api/analysis` | Müalicə nəticələrinin analitik statistikası | Hər kəs |

---

## 🔑 Test İstifadəçi Məlumatları (Default Hesablar)

* **Admin Hesabı:**
  * Email: `aysu@saglamkampus.az`
  * Şifrə: `kampus123`
* **Tələbə Hesabı:**
  * Email: `telebe@saglamkampus.az`
  * Şifrə: `kampus123`
