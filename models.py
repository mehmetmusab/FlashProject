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
        
        # Ürünleri veritabanına ekle
#         products = [
           
#     {"product_no": "sweatshirt", "description": "Kadın sweatshirt, rahat ve şık tasarım.", "price": 10.99, "image": "product0.jpg", "category": "Category A"},
#     {"product_no": "etek", "description": "Kadın eteği, günlük kullanım için ideal.", "price": 15.99, "image": "product2.jpg", "category": "Category B"},
#     {"product_no": "pantolon", "description": "Erkek pantolonu, rahat ve dayanıklı.", "price": 20.99, "image": "product3.jpg", "category": "Category A"},
#     {"product_no": "ceket", "description": "Şık erkek ceketi, her ortamda kullanıma uygun.", "price": 25.99, "image": "product4.jpg", "category": "Category C"},
#     {"product_no": "elbise", "description": "Kadın elbisesi, zarif tasarım ve rahat kumaş.", "price": 30.99, "image": "product5.jpg", "category": "Category B"},
#     {"product_no": "mont", "description": "Kışlık mont, soğuk hava için mükemmel koruma.", "price": 35.99, "image": "product6.jpg", "category": "Category C"},
#     {"product_no": "gömlek", "description": "Erkek gömleği, günlük ve iş kullanımı için uygun.", "price": 40.99, "image": "product7.jpg", "category": "Category A"},
#     {"product_no": "ayakkabı", "description": "Spor ayakkabı, rahatlık ve şıklık bir arada.", "price": 45.99, "image": "product8.jpg", "category": "Category B"},
#     {"product_no": "çanta", "description": "Kadın çantası, günlük kullanım için ideal.", "price": 50.99, "image": "product9.jpg", "category": "Category C"},
#     {"product_no": "şapka", "description": "Unisex şapka, güneşten korunmak için şık bir seçenek.", "price": 55.99, "image": "product10.jpg", "category": "Category A"},
# ]


        for product_data in products:
            product = Product(**product_data)
            db.session.add(product)

        db.session.commit()  # Değişiklikleri kaydet
        print("Ürünler başarıyla eklendi.")

    app.run(debug=True)
