from flask import Blueprint, request, jsonify
from ..models import Product, Cart
from .services import get_Product
from flask_cors import cross_origin

api = Blueprint('api', __name__, url_prefix='/api')



@api.post('/products')
def add_product():
    new_product = request.get_json()
    product = [] # define and initialize the list
    new_product_id = len(product) + 1
    new_product['product_id'] = new_product_id
    product.append(new_product)

    return jsonify({'product': new_product}), 201

@api.get('/products')
@cross_origin()
def all_Products():
    products = Product.query.all()
    response = []
    for p in products:
        response.append(p.to_dict())
    return {'data' : response}


@api.get('/product12345')
def getProduct():
    product = get_Product()
    for p in product['product']:
        new_p = Product(p['product_id'], p['title'], p['price'], p['description'], p['category'])
        new_p.saveProduct()
    print(product)
    return{
        'status' : 'ok',
        'data' : product
    }

@api.get('/product/<int:product_id>')
def getSingleProduct(product_id):
    p = Product.query.get(product_id)
    if p:
        product = p.to_dict()
        return {
            'status' : 'ok',
            'data' : product
        }
    return {
        'status' : 'NOT ok',
        'message' : 'That product is not available!'
    }

@api.post('/createprduct')
def createProductAPI():
    data = request.json

    title = data['title']
    price = data['price']
    description = data['description']
    category = data['category']
    img_url = data['img_url']

    new = Product(title, price, description, category, img_url)
    new.saveProduct()
    return {
        'status' : 'ok',
        'message' : 'New product has been created!'
    }

@api.get('/product/item/<int:user_id>')
def getPostsByUser(user_id):
    product = Product.query.filter(Product.user_id == user_id).all()
    if product:
        return {
            'status' : 'ok',
            'product' : [p.to_dict() for p in product]
        }
    return {
        'status' : 'NOT ok',
        'message' : 'No product available to return from the ID'
    }