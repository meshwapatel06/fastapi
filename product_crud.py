# from urllib import
from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional
# from models.productModel import Product
# from routers.productRouter import ProductRouter

app = FastAPI()
## Hellooooo
## Helloooooooooo


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

# Create product
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


# Get product
@app.get('/products')
def get_products(response: Response):
    try:
        response.status_code = 200
        return {'isSuccess':True, 'message' : 'Product Display Successfully', 'products': products}
    except Exception as e:
        response.status_code = 500
        return{'isSuccess' : False, 'message' : 'Error Creating Product'}


# Get by id
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

# Delete Product
@app.delete('/deleteproduct/{productid}')
def delete_product(productid: int, response: Response):
    try:
        response.status_code = 200
        for product in products:
            if product.id == productid:
                products.remove(product)
                return {'isSuccess': True, 'message': 'Product Deleted Successfully', 'product': product}
        response.status_code = 404
        return {'isSuccess':False, 'message' : 'Product not found'}
    
    except Exception as e:
        response.status_code = 500

        return {'isSuccess': False, 'message': str(e)}

# Update Product
# @app.put('/updateproduct/{productid}')
# def update_product(productid: int,updated_product: Product, response: Response):
#     try:
#         response.status_code = 200
#         for product in products:
#             if product.id == productid:
#                 product.name = updated_product.name
#                 product.price = updated_product.price
#                 product.description = updated_product.description

#                 return {'isSuccess': True, 'message': 'Product Updated Successfully', 'product': product}

#         response.status_code = 404
#         return {'isSuccess': False, 'message': 'Product not found'}

#     except Exception as e:
#         response.status_code = 500
#         return {'isSuccess': False, 'message': str(e)}





