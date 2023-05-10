from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import current_user
from ..models import Product, Cart

cart = Blueprint('cart', __name__, template_folder='cart_templates')

@cart.route('/my-cart')
def viewMyCart():
    products = Cart.query.order_by(Product.product_id).all()
    return render_template('my_cart.html', products=products)

@cart.route('/add/<int:product_id>')
def addToCart(product_id):
    product = Product.query.filter_by(product_id=product_id).first()
    product.saveToCart(current_user)
    product_name=product.title
    flash(f"{product_name} has been added!")
    return redirect(url_for('homePage'))

@cart.route('/remove/<int:product_id>')
def removeFromCart(product_id):
    product = Cart.query.filter_by(product_id=product_id).first()
    product.deleteFromCart(current_user)
    product_name=product.title
    flash(f"{product_name} has been Removed!")
    return redirect(url_for('homePage'))

@cart.route('/view-singe-item/<int:product_id>')
def viewSingleProduct(product_id):
    product = Product.query.get(product_id)
    return render_template('single_product.html',product=product)

@cart.route('/view-all-products')
def viewAllProducts():
    products = Product.query.order_by(Product.product_id).all()
    return render_template('all_products.html', products=products)

