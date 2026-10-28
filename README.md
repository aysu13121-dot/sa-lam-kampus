# 💊 Sağlam Kampus - Sprint 2: Core Features Integration (50% Completion)

Bu layihə **Universitet Tibb Məntəqəsi və Ehtiyat İdarəetmə Sistemi** üçün hazırlanmış tam inteqrasiyalı REST API və müasir Veb Tətbiqdir. **Data Analitika** ixtisası tələbələri üçün xüsusi olaraq zəngin statistik modullar, təsadüfi dataset generatoru, CSV kütləvi yükləmə və ixrac (export) xüsusiyyətləri ilə təmin edilmişdir.

---

## 🎯 Sprint 2 Çərçivəsində Görülmüş İşlər və Tələblər (Acceptance Criteria)

✅ **50% Layihə İnteqrasiyası:** Backend REST API və Frontend SPA tam inteqrasiya olunmuşdur.  
✅ **Tam CRUD Əməliyyatları:**
  * **Kataloq & Dərmanlar:** Əlavə etmə, oxuma, tam redaktə, ehtiyatı dəyişmə və silmə (`/api/products`).
  * **Tələbə Müraciətləri Jurnalı:** Qəbul qeydi, şikayət, göstərilən yardım, dərman sərfiyyatı və silmə (`/api/visits`).
  * **Ehtiyat Sifarişləri / Tələbnamələr:** Səbət sistemi, status yeniləmə ('delivered' olduqda anbara avtomatik əlavə) (`/api/orders`).
  * **Rəy və Təkliflər:** Ulduz qiymətləndirməsi və rəy idarəsi (`/api/reviews`).  
✅ **📊 Data Analitika Xüsusiyyətləri:**
  * **🎲 Təsadüfi Data Generatoru:** Slider ilə istənilən sayda realistik dərman və tələbə müraciəti generasiyası (`POST /api/data/generate`).
  * **📁 CSV Kütləvi Yükləmə (Upload):** Excel/Pandas ilə hazırlanmış `.csv` faylını birbaşa bazaya yükləmək (`POST /api/data/upload/csv`).
  * **📥 CSV İxracı (Export):** Dərmanlar və müraciətlər bazasını Pandas / PowerBI / Tableau üçün dərhal CSV formatında yükləmə (`GET /api/data/export/products/csv`).
  * **📈 Təsviri Statistika:** Mean stock, mean demand, coverage ratio, kateqoriya və fakültə üzrə paylanma göstəriciləri (`GET /api/analysis/metrics`).  
✅ **Müasir Dizayn Sistemi:** Responsive, mobil dostu, interaktiv toast bildirişləri, boş (empty) və yüklənmə (loading) vəziyyətləri.  
✅ **İnteraktiv Swagger / OpenAPI:** Bütün yeni endpoint-lər təsvirləri və nümunəvi parametrləri ilə sənədləşdirilmişdir.

---

## 🚀 Layihəni Lokal Mühitdə İşə Salma Qaydası

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

### 3. Brauzerdə daxil olun:
* **💻 Əsas Veb İnterfeys (Frontend):** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **📄 Swagger UI (Canlı API Test):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **📚 ReDoc Sənədləri:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* **🩺 Health Check:** [http://127.0.0.1:8000/api/health](http://127.0.0.1:8000/api/health)

---

## 🔑 Test İstifadəçi Məlumatları (Default Hesablar)

* **Admin Hesabı:**
  * Email: `aysu@saglamkampus.az`
  * Şifrə: `kampus123`
* **Tələbə Hesabı:**
  * Email: `telebe@saglamkampus.az`
  * Şifrə: `kampus123`

---

## 📋 Əsas API Endpoint-ləri Cədvəli

| Metod | Endpoint | Təsvir | Modul |
|---|---|---|---|
| `GET` | `/` | SPA Veb İnterfeysini açır | Frontend |
| `GET` | `/docs` | İnteraktiv Swagger UI sənədləşməsi | OpenAPI |
| `GET` | `/api/health` | Serverin işlək statusunu yoxlayır | Health |
| `POST` | `/api/auth/login` | Sistemə giriş və JWT token almaq | Autentifikasiya |
| `POST` | `/api/auth/signup` | Yeni istifadəçi qeydiyyatı | Autentifikasiya |
| `GET` | `/api/auth/me` | Cari daxil olmuş istifadəçi profili | Autentifikasiya |
| `GET` | `/api/categories` | Kateqoriyalar siyahısı və ikonlar | Kataloq |
| `GET` | `/api/products` | Dərmanların siyahısı və filtrlər (axtarış, status) | Kataloq (CRUD) |
| `GET` | `/api/products/{id}` | ID üzrə tək məhsul detalları | Kataloq (CRUD) |
| `POST` | `/api/products` | Yeni dərman / ləvazimat əlavə et | Kataloq (CRUD) |
| `PUT` | `/api/products/{id}` | Məhsul məlumatlarını tam yenilə | Kataloq (CRUD) |
| `PATCH` | `/api/products/{id}/stock` | Ehtiyat miqdarını sürətli yenilə | Kataloq (CRUD) |
| `DELETE` | `/api/products/{id}` | Məhsulu bazadan sil | Kataloq (CRUD) |
| `GET` | `/api/visits` | Tələbə tibbi müraciətləri siyahısı | Müraciətlər (CRUD) |
| `POST` | `/api/visits` | Yeni tələbə müraciəti qeyd et | Müraciətlər (CRUD) |
| `PUT` | `/api/visits/{id}` | Müraciət qeydini yenilə | Müraciətlər (CRUD) |
| `DELETE` | `/api/visits/{id}` | Müraciəti sil | Müraciətlər (CRUD) |
| `GET` | `/api/orders` | Bütün ehtiyat sifarişləri / tələbnamələr | Sifarişlər (CRUD) |
| `POST` | `/api/orders` | Yeni tələbnamə sifarişi göndər | Sifarişlər (CRUD) |
| `PATCH` | `/api/orders/{id}/status` | Sifariş statusunu yenilə (təhvil verildikdə anbara daxil olur) | Sifarişlər (CRUD) |
| `DELETE` | `/api/orders/{id}` | Sifarişi ləğv et / sil | Sifarişlər (CRUD) |
| `POST` | `/api/data/generate` | Data Analitika üçün təsadüfi dataset yarat | Data Alətləri |
| `POST` | `/api/data/upload/csv` | CSV faylı ilə kütləvi dərman yüklə | Data Alətləri |
| `GET` | `/api/data/export/products/csv` | Dərmanlar bazasını CSV kimi ixrac et | Data Alətləri |
| `GET` | `/api/data/export/visits/csv` | Müraciətlər bazasını CSV kimi ixrac et | Data Alətləri |
| `GET` | `/api/data/sample-csv` | Doldurmaq üçün nümunə CSV şablonu yüklə | Data Alətləri |
| `POST` | `/api/data/reset` | Bazanı ilkin demo vəziyyətinə sıfırla | Data Alətləri |
| `GET` | `/api/analysis` | Xəstəliklər üzrə sağalma analizi | Analitika |
| `GET` | `/api/analysis/metrics` | Təsviri statistik göstəricilər | Analitika |
| `GET` | `/api/reviews` | Bütün rəylər və orta ulduz reytinqi | Rəylər (CRUD) |
| `POST` | `/api/reviews` | Yeni rəy göndər | Rəylər (CRUD) |
| `DELETE` | `/api/reviews/{id}` | Rəyi sil | Rəylər (CRUD) |
