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
        
        # Ürünleri veritabanına ekle
        products = [
            {"product_no": "sweatshirt", "description": "kadın" "Product 1", "price": 10.99, "image": "product1.jpg", "category": "Category A"},
            {"product_no": "2", "description": "Product 2", "price": 15.99, "image": "product2.jpg", "category": "Category B"},
            {"product_no": "3", "description": "Product 3", "price": 20.99, "image": "product3.jpg", "category": "Category A"},
            {"product_no": "4", "description": "Product 4", "price": 25.99, "image": "product4.jpg", "category": "Category C"},
            {"product_no": "5", "description": "Product 5", "price": 30.99, "image": "product5.jpg", "category": "Category B"},
            {"product_no": "6", "description": "Product 6", "price": 35.99, "image": "product6.jpg", "category": "Category C"},
            {"product_no": "7", "description": "Product 7", "price": 40.99, "image": "product7.jpg", "category": "Category A"},
            {"product_no": "8", "description": "Product 8", "price": 45.99, "image": "product8.jpg", "category": "Category B"},
            {"product_no": "9", "description": "Product 9", "price": 50.99, "image": "product9.jpg", "category": "Category C"},
            {"product_no": "10", "description": "Product 10", "price": 55.99, "image": "product10.jpg", "category": "Category A"},
        ]

        for product_data in products:
            product = Product(**product_data)
            db.session.add(product)

        db.session.commit()  # Değişiklikleri kaydet
        print("Ürünler başarıyla eklendi.")

    app.run(debug=True)
