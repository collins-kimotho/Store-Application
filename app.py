from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Writing the Models
class Customer(db.Model):
    id = db.Model(db.Integer, primary_key = True)
    first_name
    last_name
    address
    city
    postcode
    email

class Order (db.Model):
    id = db.Model(db.Integer, primary_key = True)
    order_date
    shipped_date
    delivered_date
    coupon_date


class Product (db.Model):
    id = db.Model(db.Integer, primary_key = True)
    name
    price



if __name__ == '__main__':
    app.run(debug=True)