```python
from flask import Flask, request
from googleapiclient.discovery import build

app = Flask(__name__)

# Google Custom Search JSON API key and CX
API_KEY = "YOUR_API_KEY"
CX = "YOUR_CX"

def search_product(product_name):
    service = build("customsearch", "v1", developerKey=API_KEY)
    res = service.cse().list(q=product_name, cx=CX).execute()
    return res['items']

@app.route('/search', methods=['POST'])
def search():
    product_name = request.form.get('product_name')
    results = search_product(product_name)
    return {'results': results}

def alternative_search(product_name):
    # Implement alternative search logic here
    pass

@app.route('/alternative_search', methods=['POST'])
def alternative_search_route():
    product_name = request.form.get('product_name')
    results = alternative_search(product_name)
    return {'results': results}
```