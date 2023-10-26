import psycopg2


def db_connection():
    connection = psycopg2.connect(database="flask_db", user="postgres",
                                  password="master", host="localhost", port="5432")

    return connection

con =db_connection()
cur = con.cursor()
cur.execute( '''CREATE TABLE IF NOT EXISTS Users (id serial PRIMARY KEY, user_name varchar(20), email varchar(40), password varchar(20));''')

con.commit()

cur.close()
con.close()