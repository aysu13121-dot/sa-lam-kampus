from datetime import datetime
from app.security import hash_password

def calculate_stock_status(stock: int, monthly_demand: int):
    """HTML-dəki status hesablaması:
       ratio >= 1.5 -> Kifayətdir (ok)
       ratio >= 0.9 -> Azalır (warn)
       ratio < 0.9  -> Az qalıb (bad)
    """
    if monthly_demand <= 0:
        ratio = 1.5
    else:
        ratio = stock / monthly_demand
    
    percentage = min(100, round((stock / monthly_demand) * 50)) if monthly_demand > 0 else 100

    if ratio >= 1.5:
        return "Kifayətdir", "ok", percentage
    elif ratio >= 0.9:
        return "Azalır", "warn", percentage
    else:
        return "Az qalıb", "bad", percentage

# Kateqoriyalar
CATEGORIES = [
    {"id": 0, "name": "Hamısı", "icon": "🏥"},
    {"id": 1, "name": "Ağrı və qızdırma", "icon": "🌡️"},
    {"id": 2, "name": "Soyuqdəymə", "icon": "🤧"},
    {"id": 3, "name": "Mədə-bağırsaq", "icon": "🫄"},
    {"id": 4, "name": "Allergiya", "icon": "🌼"},
    {"id": 5, "name": "Yara və sarğı", "icon": "🩹"},
    {"id": 6, "name": "Cihazlar", "icon": "🩺"}
]

# İlkin məhsullar
INITIAL_RAW_PRODUCTS = [
    {"id": 1, "name": "Paracetamol tabletləri", "icon": "💊", "category_id": 1, "stock": 40, "monthly_demand": 60},
    {"id": 2, "name": "Ibuprofen tabletləri", "icon": "💊", "category_id": 1, "stock": 55, "monthly_demand": 45},
    {"id": 3, "name": "Buz kisəsi", "icon": "🧊", "category_id": 1, "stock": 30, "monthly_demand": 12},
    {"id": 4, "name": "Boğaz pastilləri", "icon": "🍬", "category_id": 2, "stock": 25, "monthly_demand": 50},
    {"id": 5, "name": "Burun spreyi", "icon": "💧", "category_id": 2, "stock": 18, "monthly_demand": 30},
    {"id": 6, "name": "Öskürək siropu", "icon": "🧴", "category_id": 2, "stock": 20, "monthly_demand": 22},
    {"id": 7, "name": "Aktivləşdirilmiş kömür", "icon": "⚫", "category_id": 3, "stock": 70, "monthly_demand": 35},
    {"id": 8, "name": "Oral rehidratasiya duzu", "icon": "🧂", "category_id": 3, "stock": 15, "monthly_demand": 28},
    {"id": 9, "name": "Antihistamin tabletləri", "icon": "🌿", "category_id": 4, "stock": 22, "monthly_demand": 40},
    {"id": 10, "name": "Gözlər üçün damcı", "icon": "👁️", "category_id": 4, "stock": 30, "monthly_demand": 14},
    {"id": 11, "name": "Yara plastırı", "icon": "🩹", "category_id": 5, "stock": 150, "monthly_demand": 120},
    {"id": 12, "name": "Antiseptik məhlul", "icon": "🧪", "category_id": 5, "stock": 12, "monthly_demand": 30},
    {"id": 13, "name": "Steril bint", "icon": "🧻", "category_id": 5, "stock": 60, "monthly_demand": 25},
    {"id": 14, "name": "Termometr", "icon": "🌡️", "category_id": 6, "stock": 6, "monthly_demand": 4},
    {"id": 15, "name": "Qan təzyiqi ölçən", "icon": "🩺", "category_id": 6, "stock": 2, "monthly_demand": 3},
    {"id": 16, "name": "Birdəfəlik əlcək", "icon": "🧤", "category_id": 5, "stock": 200, "monthly_demand": 90}
]

def format_product(raw):
    cat = next((c for c in CATEGORIES if c["id"] == raw["category_id"]), None)
    status_label, status_level, percentage = calculate_stock_status(raw["stock"], raw["monthly_demand"])
    return {
        **raw,
        "category_name": cat["name"] if cat else "Digər",
        "status": status_label,
        "status_level": status_level,
        "meter_percent": percentage
    }

INITIAL_PRODUCTS = [format_product(p) for p in INITIAL_RAW_PRODUCTS]

INITIAL_USERS = [
    {
        "id": "usr_admin",
        "full_name": "Aysu Məmmədova",
        "email": "aysu@saglamkampus.az",
        "password": hash_password("kampus123"),
        "role": "admin",
        "created_at": datetime.utcnow().isoformat()
    },
    {
        "id": "usr_student",
        "full_name": "Tələbə İstifadəçi",
        "email": "telebe@saglamkampus.az",
        "password": hash_password("kampus123"),
        "role": "student",
        "created_at": datetime.utcnow().isoformat()
    }
]

INITIAL_REVIEWS = [
    {
        "id": "rev_1",
        "author": "Aysel K.",
        "topic": "Tibb məntəqəsi ideyası",
        "rating": 5,
        "comment": "Kampus daxilində belə məntəqənin olması və ehtiyatın onlayn bilinməsi çox əla ideyadır!",
        "created_at": datetime.utcnow().isoformat()
    },
    {
        "id": "rev_2",
        "author": "Anonim",
        "topic": "Məhsul kataloqu",
        "rating": 4,
        "comment": "Plastır və antiseptik ehtiyatı daim bol olmalıdır, təşəkkürlər.",
        "created_at": datetime.utcnow().isoformat()
    }
]

INITIAL_ANALYSIS = [
    {
        "disease": "Qrip və soyuqdəymə",
        "patient_group": "Tələbələr (18-24 yaş)",
        "sample_size": 120,
        "healed_percent": 78,
        "improved_percent": 17,
        "side_effect_percent": 5,
        "summary": "Müalicə alan 120 tələbədən 78%-i tam sağalıb, 5%-də yüngül yuxululuq yan təsiri qeydə alınıb."
    },
    {
        "disease": "Mövsümi allergiya",
        "patient_group": "Bütün yaş qrupları",
        "sample_size": 65,
        "healed_percent": 62,
        "improved_percent": 30,
        "side_effect_percent": 8,
        "summary": "Antihistamin preparatları 92% ümumi yaxşılaşma təmin edir."
    },
    {
        "disease": "Mədə-bağırsaq narahatlığı",
        "patient_group": "İmtahan sessiyası dövrü",
        "sample_size": 85,
        "healed_percent": 84,
        "improved_percent": 14,
        "side_effect_percent": 2,
        "summary": "Rehidratasiya və pəhriz dəstəyi ilə sürətli sağalma müşahidə olunur."
    }
]

class Database:
    def __init__(self):
        self.users = list(INITIAL_USERS)
        self.products = list(INITIAL_PRODUCTS)
        self.reviews = list(INITIAL_REVIEWS)
        self.orders = []
        self.analysis = list(INITIAL_ANALYSIS)

    # İstifadəçilər
    def find_user_by_email(self, email: str):
        return next((u for u in self.users if u["email"].lower() == email.lower()), None)

    def find_user_by_id(self, user_id: str):
        return next((u for u in self.users if u["id"] == user_id), None)

    def create_user(self, full_name: str, email: str, password_hash: str, role: str = "student"):
        new_user = {
            "id": f"usr_{len(self.users) + 1}_{int(datetime.utcnow().timestamp())}",
            "full_name": full_name,
            "email": email.lower(),
            "password": password_hash,
            "role": role,
            "created_at": datetime.utcnow().isoformat()
        }
        self.users.append(new_user)
        return new_user

    # Məhsullar
    def get_products(self, category_id: int | None = None, search: str | None = None):
        res = self.products
        if category_id is not None and category_id != 0:
            res = [p for p in res if p["category_id"] == category_id]
        if search:
            s = search.lower()
            res = [p for p in res if s in p["name"].lower() or s in p["category_name"].lower()]
        return res

    def get_product_by_id(self, product_id: int):
        return next((p for p in self.products if p["id"] == product_id), None)

    def create_product(self, name: str, icon: str, category_id: int, stock: int, monthly_demand: int):
        new_id = max([p["id"] for p in self.products], default=0) + 1
        raw = {
            "id": new_id,
            "name": name,
            "icon": icon,
            "category_id": category_id,
            "stock": stock,
            "monthly_demand": monthly_demand
        }
        prod = format_product(raw)
        self.products.append(prod)
        return prod

    def update_stock(self, product_id: int, new_stock: int):
        prod = self.get_product_by_id(product_id)
        if not prod:
            return None
        prod["stock"] = new_stock
        status_label, status_level, percentage = calculate_stock_status(prod["stock"], prod["monthly_demand"])
        prod["status"] = status_label
        prod["status_level"] = status_level
        prod["meter_percent"] = percentage
        return prod

    # Kateqoriyalar
    def get_categories(self):
        return CATEGORIES

    # Rəylər
    def get_reviews(self):
        return self.reviews

    def create_review(self, author: str, topic: str, rating: int, comment: str):
        rev = {
            "id": f"rev_{len(self.reviews) + 1}_{int(datetime.utcnow().timestamp())}",
            "author": author.strip() if author and author.strip() else "Anonim",
            "topic": topic,
            "rating": rating,
            "comment": comment.strip(),
            "created_at": datetime.utcnow().isoformat()
        }
        self.reviews.insert(0, rev)
        return rev

    # Sifarişlər
    def create_order(self, items: list, ordered_by: str):
        order_id = f"ord_{len(self.orders) + 1}_{int(datetime.utcnow().timestamp())}"
        total_items = sum(item["quantity"] for item in items)
        new_order = {
            "id": order_id,
            "items": items,
            "total_items": total_items,
            "status": "pending",
            "ordered_by": ordered_by,
            "created_at": datetime.utcnow().isoformat()
        }
        self.orders.append(new_order)
        return new_order

    def get_orders(self):
        return self.orders

    # Analiz
    def get_analysis(self):
        return self.analysis

db = Database()
