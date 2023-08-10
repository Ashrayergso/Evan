```python
from openpyxl import Workbook
from flask import send_file
from .database import get_all_products

def create_export():
    wb = Workbook()
    ws = wb.active

    # Add headers
    headers = ['Product Name', 'Product Number', 'Product Cost', 'Product Link', 'Quantity', 'Total Cost']
    ws.append(headers)

    # Get all products
    products = get_all_products()

    # Add products to the worksheet
    for product in products:
        row = [product.name, product.number, product.cost, product.link, product.quantity, product.cost * product.quantity]
        ws.append(row)

    # Save the workbook to a file
    wb.save('product_list.xlsx')

def download_export():
    create_export()
    return send_file('product_list.xlsx', as_attachment=True)
```