'''
    E-com-store: it is probably exactly as you think.
    By: James R. Brown
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title="EComStore", message="You Made it")

if __name__ == '__main__':
    app.run(debug=True)
