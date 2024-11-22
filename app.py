'''
    E-com-store: it is probably exactly as you think.
    By: James R. Brown
'''
from flask import Flask
from flask import render_template, url_for, request, redirect
import flask_login
from store_items import StoreItems
from user import User

app = Flask(__name__)
app.secret_key = 'super secret'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

users = {'foo@bar.tld': {'password': 'secret'}}

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = request.form['email']
    if email in users and request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect('/products')

    return 'Bad login'

@app.route("/cart")
def view_cart():
    pass

@app.route("/cart/add-item/<item>")
def add_item(item=None):
    if flask_login.current_user.is_authenticated:
        flask_login.current_user.cart.append(item)
    else:
        user = User()
        user.cart.append(item)

    return redirect('/products')

@app.route("/checkout")
def checkout():
    pass

app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

if __name__ == '__main__':
    app.run(debug=True)
