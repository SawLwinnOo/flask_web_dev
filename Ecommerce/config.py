class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:master@localhost:5432/flask_db"
