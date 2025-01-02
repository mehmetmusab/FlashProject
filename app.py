from flask import Flask, render_template, request, redirect, url_for
from models import db, Product  # db ve model import ediliyor

app = Flask(__name__)

# Flask config ayarları
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Veritabanı bağlantısı
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Gereksiz uyarıları kapat

# Veritabanı bağlantısı
db.init_app(app)

@app.route('/')
def home():
    # Ana sayfa: Ürünleri veritabanından çekme
    products = Product.query.all()  # Ürünleri al
    return render_template('home.html', products=products)

@app.route('/search')
def search():
    search_query = request.args.get('q')  # Arama sorgusunu al
    if search_query:
        # Ürünler üzerinde arama yap
        products = Product.query.filter(
            Product.product_no.like(f'%{search_query}%') |
            Product.description.like(f'%{search_query}%') |
            Product.category.like(f'%{search_query}%')
        ).all()
    else:
        # Arama sorgusu boşsa, tüm ürünleri göster
        products = Product.query.all()
    
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Ürün detay sayfası: Seçilen ürünü ID'ye göre çekme
    product = Product.query.get_or_404(product_id)  # Ürünü ID'ye göre al
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    # Veritabanı ve tabloları oluştur
    with app.app_context():
        db.create_all()  # Veritabanı ve tablolar oluşturulacak
        
        # Veritabanında ürün yoksa, ürünleri ekle
        if not Product.query.first():

            
            products = [
                {"product_no": "1", "product_name": "Classic Crewneck Sweatshirt", "price": 15.99, "image": "product1.jpg", "category": "Category A", "description": "A timeless and comfortable crewneck sweatshirt, perfect for casual wear or layering. Made from a soft and durable cotton blend, this sweatshirt features a classic design with ribbed cuffs and hem for a snug fit. Ideal for everyday use, this sweatshirt offers both comfort and style."},
                {"product_no": "2", "product_name": "Flowing Midi Skirt", "price": 15.99, "image": "product2.jpg", "category": "Category B", "description": "A stylish and versatile midi skirt, perfect for adding a touch of elegance to any outfit. This skirt features a flattering A-line silhouette and is made from a lightweight and flowy fabric for a comfortable fit and graceful movement. Suitable for various occasions, from casual outings to more formal events."},
                {"product_no": "3", "product_name": "Slim Fit Chino Trousers", "price": 20.99, "image": "product3.jpg", "category": "Category A", "description": "A pair of modern and stylish slim fit chino trousers, offering both comfort and a contemporary look. These trousers are crafted from a durable cotton blend with a touch of stretch for a comfortable fit and freedom of movement. Perfect for both casual and smart-casual occasions."},
                {"product_no": "4", "product_name": "Elegant Evening Dress", "price": 25.99, "image": "product4.jpg", "category": "Category C", "description": "A sophisticated and elegant evening dress, perfect for special occasions, parties, or formal events. This dress features a flattering design, crafted from luxurious materials, and designed to make you feel confident and glamorous. Available in various colors and sizes."},
                {"product_no": "5", "product_name": "Multi-Purpose Utility Backpack", "price": 30.99, "image": "product5.jpg", "category": "Category B", "description": "A versatile and durable utility backpack, perfect for everyday use, travel, or outdoor adventures. This backpack features multiple compartments for organized storage, padded shoulder straps for comfort, and is made from water-resistant materials to protect your belongings."},
                {"product_no": "6", "product_name": "Premium Leather Wallet", "price": 35.99, "image": "product6.jpg", "category": "Category C", "description": "A high-quality and stylish leather wallet, crafted from genuine leather for durability and a luxurious feel. This wallet features multiple card slots, a bill compartment, and a coin pocket, offering ample storage for your essentials. A perfect gift for yourself or a loved one."},
                {"product_no": "7", "product_name": "Comfortable Cotton T-Shirt", "price": 40.99, "image": "product7.jpg", "category": "Category A", "description": "A classic and comfortable cotton t-shirt, perfect for everyday wear. Made from soft and breathable cotton, this t-shirt offers a relaxed fit and is ideal for layering or wearing on its own. Available in a variety of colors."},
                {"product_no": "8", "product_name": "Stylish Canvas Tote Bag", "price": 45.99, "image": "product8.jpg", "category": "Category B", "description": "A trendy and practical canvas tote bag, perfect for carrying your essentials in style. This bag is made from durable canvas material and features spacious compartments, sturdy handles, and a stylish design. Ideal for shopping, work, or everyday use."},
                {"product_no": "9", "product_name": "Modern Stainless Steel Watch", "price": 50.99, "image": "product9.jpg", "category": "Category C", "description": "A sleek and modern stainless steel watch, perfect for adding a touch of sophistication to any outfit. This watch features a durable stainless steel case and band, a precise quartz movement, and a minimalist design. A timeless accessory for any occasion."},
                {"product_no": "10", "product_name": "Warm Wool Beanie Hat", "price": 55.99, "image": "product10.jpg", "category": "Category A", "description": "A warm and cozy wool beanie hat, perfect for keeping you warm during the colder months. This hat is made from soft and insulating wool, and features a classic design that complements any winter outfit. Provides excellent protection from the cold and wind."},
            ]


            # products = [ 
            # {"product_no": "sweatshirt", "name": "Kadın sweatshirt, rahat ve şık tasarım.", "price": 10.99, "image": "product0.jpg", "category": "Category A"},
            # {"product_no": "etek", "name": "Kadın eteği, günlük kullanım için ideal.", "price": 15.99, "image": "product2.jpg", "category": "Category B"},
            # {"product_no": "pantolon", "name": "Erkek pantolonu, rahat ve dayanıklı.", "price": 20.99, "image": "product3.jpg", "category": "Category A"},
            # {"product_no": "ceket", "name": "Şık erkek ceketi, her ortamda kullanıma uygun.", "price": 25.99, "image": "product4.jpg", "category": "Category C"},
            # {"product_no": "elbise", "name": "Kadın elbisesi, zarif tasarım ve rahat kumaş.", "price": 30.99, "image": "product5.jpg", "category": "Category B"},
            # {"product_no": "mont", "name": "Kışlık mont, soğuk hava için mükemmel koruma.", "price": 35.99, "image": "product6.jpg", "category": "Category C"},
            # {"product_no": "gömlek", "name": "Erkek gömleği, günlük ve iş kullanımı için uygun.", "price": 40.99, "image": "product7.jpg", "category": "Category A"},
            # {"product_no": "ayakkabı", "name": "Spor ayakkabı, rahatlık ve şıklık bir arada.", "price": 45.99, "image": "product8.jpg", "category": "Category B"},
            # {"product_no": "çanta", "name": "Kadın çantası, günlük kullanım için ideal.", "price": 50.99, "image": "product9.jpg", "category": "Category C"},
            # {"product_no": "şapka", "name": "Unisex şapka, güneşten korunmak için şık bir seçenek.", "price": 55.99, "image": "product10.jpg", "category": "Category A"},
            # ]

            for product_data in products:
                product = Product(**product_data)
                db.session.add(product)

            db.session.commit()  # Değişiklikleri kaydet
            print("Ürünler başarıyla eklendi.")
            from flask_sqlalchemy import SQLAlchemy
    app.run(debug=True)
    from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask uygulamasını başlatma
app = Flask(__name__)

# Veritabanı yapılandırması
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Veritabanı adı ve URI'si
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # İzleme özelliği kapalı

# SQLAlchemy ile Flask uygulamasını bağlama
db = SQLAlchemy(app)

# Veritabanı modeli
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_no = db.Column(db.String(50), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(50), nullable=False)

# Ana dosya olarak çalıştırıldığında
if __name__ == "__main__":
    app.run(debug=True)

