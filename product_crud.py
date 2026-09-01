# from urllib import
from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional
# from models.productModel import Product
# from routers.productRouter import ProductRouter

app = FastAPI()


# 200 - Ok
# 201 - Created
# 400 - Bad Request
# 403 - ForBidden
# 404 - Not Found
# 500 - Server Error

class Product(BaseModel):
    id : Optional[int] = None
    name: str
    price: float
    description: str
products = []
id = 0

@app.post('/products')
def create_product(product: Product, response: Response):
    global id
    try:
        id += 1
        product.id = id
        products.append(product)
        response.status_code = 201
        return {'isSuccess':True, 'message' : 'Product Created Successfully', 'product': product}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : str(e)}

@app.get('/products')
def get_products(response: Response):
    try:
        response.status_code = 200
        return {'isSuccess':True, 'message' : 'Product Display Successfully', 'products': products}
    except Exception as e:
        response.status_code = 500
        return{'isSuccess' : False, 'message' : 'Error Creating Product'}

@app.get('/getproductID/{productid}')
def get_productID(productid: int, response: Response):
    try:
        response.status_code = 200
        for product in products:
            if product.id == productid:
                return {'isSuccess':True,  'product': product}

        response.status_code = 404
        return {'message' : 'Product not found', 'isSuccess' : False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : 'Error Creating Product'}




