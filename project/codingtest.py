import csv
import pandas as pd
import sqlite3
import sqlalchemy


df = pd.read_csv("products.csv")


def database():
    connection = sqlite3.connect('sample.db')
    cur = connection.cursor()
    cur.execute('CREATE TABLE allproducts(name TEXT,no_of_products INTEGER)')
    connection.commit()


def datas():
    new = df.groupby('name').size().reset_index(name="no_of_products")
    engine = sqlalchemy.create_engine('sqlite:///sample.db')
    new.to_sql('allproducts', engine, if_exists='append', index=False)
    pd.read_sql('allproducts', engine)


database()
datas()
