from fastapi import FastAPI
from model import Product

app = FastAPI()

@app.get('/')
def greet():
    return 'Hello'

products = [
    Product(id=1, name='Laptop', des='Works', price=560, quantity=20),
    Product(id=2, name='Laptop', des='Works', price=560, quantity=20),
    Product(id=3, name='Laptop', des='Works', price=560, quantity=20),
    Product(id=4, name='Laptop', des='Works', price=560, quantity=20),
    Product(id=5, name='Laptop', des='Works', price=560, quantity=20)
]

@app.get('/products')
def  get_all_prod(): 
    return products

@app.get('/product/{id}')
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return 'Product Not Found'

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put('/product')
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Added"
    return "No Product Found"


@app.delete('/product')
def update_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "No Product Found"