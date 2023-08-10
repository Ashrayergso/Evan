```python
from flask import Flask, render_template, request, redirect, url_for
from database import create_database
from product import create_product, add_product_to_list
from search import create_search, search_product_in_database
from export import create_export, export_list_to_excel

app = Flask(__name__)

@app.route('/')
def index():
    create_database()
    products = create_product()
    return render_template('index.html', products=products)

@app.route('/search', methods=['POST'])
def search():
    product_name = request.form.get('product_name')
    create_search()
    search_results = search_product_in_database(product_name)
    return render_template('product.html', products=search_results)

@app.route('/add', methods=['POST'])
def add_to_list():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    add_product_to_list(product_id, quantity)
    return redirect(url_for('index'))

@app.route('/export', methods=['POST'])
def export():
    create_export()
    export_list_to_excel()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```