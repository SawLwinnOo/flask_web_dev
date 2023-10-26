from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(20))
    email = db.Column(db.String(40))
    password = db.Column(db.String(20))

    def __init__(self, username, email, password):
        self.user_name = username
        self.email = email
        self.password = password


    def __repr__(self):
        return f"User('{self.user_name}', '{self.email}', '{self.password}')"




@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
