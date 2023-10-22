from flask import Flask

#routes registration
app = Flask(__name__)
from e_commerce import routes

