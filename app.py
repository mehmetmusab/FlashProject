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
                {"product_no": "1", "description": "Product 1", "price": 10.99, "image": "product1.jpg", "category": "Category A"},
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
