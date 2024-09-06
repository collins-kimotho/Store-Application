from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Writing the Models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100),nullable=False)
    last_name = db.Column(db.String(100),nullable=False)
    address = db.Column(db.String(100),nullable=False)
    city = db.Column(db.String(100),nullable=False)
    postcode = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),nullable=False, unique=True)
    
    orders = db.relationship('Order', backref = 'customer')
    
order_product = db.Table('order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
    )

class Order (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shipped_date = db.Column(db.DateTime)
    delivered_date = db.Column(db.DateTime)
    coupon_date = db.Column(db.String(50))

    products = db.relationship('Product', secondary=order_product)



class Product (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),nullable=False)



if __name__ == '__main__':
    app.run(debug=True)