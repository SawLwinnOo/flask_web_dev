from e_commerce import app, con
from flask import render_template, request, url_for, redirect

@app.route('/login')
def login():
    cur = con.cursor()
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    cur = con.cursor()
    name = request.form['user_name']
    email = request.form['email']
    password= request.form['password']
    cur.execute('''INSERT INTO Users (user_name, email, password) VALUES (%s, %s, %s)''', (name, email, password))
    con.commit()
    cur.close()
    con.close()

    return redirect(url_for('home.html'))