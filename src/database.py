```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    product_number = db.Column(db.String(50), nullable=False)
    product_cost = db.Column(db.Float, nullable=False)
    product_link = db.Column(db.String(200), nullable=False)
    product_image = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.product_number}', '{self.product_cost}', '{self.product_link}', '{self.product_image}')"

db.create_all()
```