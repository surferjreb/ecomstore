'''
    E-com-store: it is probably exactly as you think.
    By: James R. Brown
'''
from flask import Flask
from flask import render_template, url_for
from store_items import StoreItems

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html', title="EComStore", message="Welcome")

@app.route("/products")
def products():
    items = StoreItems().STORE_ITEMS
    return render_template('products.html', title="products", items=items)

@app.route("/products/<item>")
def product_view(item):
    pass

@app.route("/login")
def login():
    pass

@app.route("/cart")
def view_cart():
    pass

@app.route("/cart/add_to_cart/<int:id>")
def add_to_cart(item_id):
    pass

@app.route("/checkout")
def checkout():
    pass


if __name__ == '__main__':
    app.run(debug=True)
