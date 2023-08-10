import App from './App.svelte';

let selectedProducts = [];
let totalCost = 0;

function searchProduct(product) {
    // Implement search functionality using Google Custom Search JSON API
}

function alternativeSearch(product) {
    // Implement alternative search functionality
}

function selectProduct(product, quantity) {
    selectedProducts.push({ product, quantity });
    totalCost += product.cost * quantity;
}

function exportList() {
    // Implement export functionality using openpyxl
    // The exported list should include the total cost per product and for the overall list
}

const app = new App({
    target: document.body,
    props: {
        searchProduct,
        alternativeSearch,
        selectProduct,
        exportList,
        products: [], // This should be replaced with the actual list of products from the database
        selectedProducts,
        totalCost
    }
});

export default app;