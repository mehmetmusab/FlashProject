from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Veritabanı bağlantı ayarları
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # SQLite veritabanı kullanımı
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Gereksiz uyarıları kapatma

db = SQLAlchemy(app)

# Ürün modelini tanımlama
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Otomatik artan birincil anahtar
    product_no = db.Column(db.String(50), unique=True, nullable=False)  # Ürün numarası
    product_name = db.Column(db.String(50), unique=True, nullable=False)  # Ürün numarası
    description = db.Column(db.String(255), nullable=False)  # Ürün açıklaması
    price = db.Column(db.Float, nullable=False)  # Ürün fiyatı
    image = db.Column(db.String(255), nullable=True)  # Ürün resmi (opsiyonel)
    category = db.Column(db.String(100), nullable=False)  # Ürün kategorisi

    def __repr__(self):
        return f'<Product {self.product_no} - {self.description}>'

# Uygulama çalıştırıldığında veritabanı ve tablolar oluşturulacak
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Veritabanı ve tabloları oluşturur
        
        # Eğer veritabanında ürün yoksa, ürünleri ekle
        if not Product.query.first():
            products = [
                {"product_no": "1", "product_name": "Classic Crewneck Sweatshirt", "price": 15.99, "image": "product1.jpg", "category": "Category A", "description": "A timeless and comfortable crewneck sweatshirt..."},
                {"product_no": "2", "product_name": "Flowing Midi Skirt", "price": 15.99, "image": "product2.jpg", "category": "Category B", "description": "A stylish and versatile midi skirt..."},
                {"product_no": "3", "product_name": "Slim Fit Chino Trousers", "price": 20.99, "image": "product3.jpg", "category": "Category A", "description": "A pair of modern and stylish slim fit chino trousers..."},
                {"product_no": "4", "product_name": "Elegant Evening Dress", "price": 25.99, "image": "product4.jpg", "category": "Category C", "description": "A sophisticated and elegant evening dress..."},
                {"product_no": "5", "product_name": "Multi-Purpose Utility Backpack", "price": 30.99, "image": "product5.jpg", "category": "Category B", "description": "A versatile and durable utility backpack..."},
                {"product_no": "6", "product_name": "Premium Leather Wallet", "price": 35.99, "image": "product6.jpg", "category": "Category C", "description": "A high-quality and stylish leather wallet..."},
                {"product_no": "7", "product_name": "Comfortable Cotton T-Shirt", "price": 40.99, "image": "product7.jpg", "category": "Category A", "description": "A classic and comfortable cotton t-shirt..."},
                {"product_no": "8", "product_name": "Stylish Canvas Tote Bag", "price": 45.99, "image": "product8.jpg", "category": "Category B", "description": "A trendy and practical canvas tote bag..."},
                {"product_no": "9", "product_name": "Modern Stainless Steel Watch", "price": 50.99, "image": "product9.jpg", "category": "Category C", "description": "A sleek and modern stainless steel watch..."},
                {"product_no": "10", "product_name": "Warm Wool Beanie Hat", "price": 55.99, "image": "product10.jpg", "category": "Category A", "description": "A warm and cozy wool beanie hat..."}
            ]
            
            for product_data in products:
                product = Product(**product_data)
                db.session.add(product)

            db.session.commit()  # Değişiklikleri kaydet
            print("Ürünler başarıyla eklendi.")

