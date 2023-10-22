from e_commerce import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    #fetch data form database
    #manage data to sho
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/product')
def product():
    return render_template('product.html')