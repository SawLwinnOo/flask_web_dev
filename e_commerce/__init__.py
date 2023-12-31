from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
from e_commerce import routes
