```python
from flask import Flask, request, jsonify
from database import db, Product

app = Flask(__name__)

@app.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], product_number=data['product_number'], 
                          product_cost=data['product_cost'], product_link=data['product_link'], 
                          product_image=data['product_image'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'New product created!'}), 201

@app.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({'name': product.name, 'product_number': product.product_number, 
                        'product_cost': product.product_cost, 'product_link': product.product_link, 
                        'product_image': product.product_image}), 200
    else:
        return jsonify({'message': 'Product not found!'}), 404

@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get(product_id)
    if product:
        product.name = data['name']
        product.product_number = data['product_number']
        product.product_cost = data['product_cost']
        product.product_link = data['product_link']
        product.product_image = data['product_image']
        db.session.commit()
        return jsonify({'message': 'Product updated!'}), 200
    else:
        return jsonify({'message': 'Product not found!'}), 404

@app.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted!'}), 200
    else:
        return jsonify({'message': 'Product not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```