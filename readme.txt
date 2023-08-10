# Product Catalog Application

This application is a product catalog built with Svelte and Flask. It allows users to search for products, add them to a list, specify quantities, and export the list with total cost per product and for the overall list.

## Features

- User-friendly product catalog with search and alternative search options
- Ability to select multiple products and add them to a list
- Ability to add quantities to the selected products
- Ability to export the list with total cost per product and for the overall list

## Installation

1. Clone the repository
2. Install the dependencies using `pip install -r requirements.txt`
3. Run the application using `python src/main.py`

## Usage

1. Open the application in your web browser.
2. Browse the product catalog.
3. Use the 'Search' button to search for a product online.
4. Use the 'Alternative Search' button to search for an alternative product.
5. Select the checkbox next to a product to add it to your list.
6. Enter a quantity for the selected product.
7. Click the 'Export' button to export your list to an Excel file. The file will include the total cost per product and for the overall list.

## Dependencies

- Flask: Used for creating the web application and handling requests.
- SQLAlchemy: Used for database operations.
- Google Custom Search JSON API: Used for product search functionality.
- openpyxl: Used for exporting the list with total cost to Excel.
- Svelte: Used for building the user interface.

## Files

- `src/main.py`: Main application file.
- `src/database.py`: Handles database operations.
- `src/product.py`: Defines the product schema and handles product-related operations.
- `src/search.py`: Handles product search functionality.
- `src/export.py`: Handles exporting the list with total cost to Excel.
- `src/templates/index.html`: Main page template.
- `src/templates/product.html`: Product page template.
- `src/static/css/styles.css`: CSS styles for the web pages.
- `src/static/js/main.js`: JavaScript file for handling user interactions.
- `src/static/img/product_images`: Directory for storing product images.
- `requirements.txt`: Lists all the Python dependencies required for the project.
- `deployment_instructions.txt`: Provides instructions for deploying the application.

## Deployment

Please refer to `deployment_instructions.txt` for detailed deployment instructions.