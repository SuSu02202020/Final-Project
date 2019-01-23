
from flask import Flask, render_template, request, redirect, jsonify,  url_for
# from flask_mysqldb import MySQL
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
import subway
#################################################
# Database Setup
#################################################
# engine = create_engine("sqlite:///total_passengers.sqlite")


# reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Create our session (link) from Python to the DB
# session = Session(engine)

# # import yaml
# inspector = inspect(engine)
# inspector.get_table_names()
# columns = inspector.get_columns('total_passengers')
# for column in columns:
#     print(column["name"], column["type"])


app = Flask(__name__)

# config db
# db = yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']

# mysql = MySQL(app)

#  rootes
@app.route("/")
def Home():
    return render_template('Home.html')

@app.route("/bottom_1")
def ML_1():
    sqlcolum = subway.sub_data()
    return sqlcolum
    # return render_template('home.html')


@app.route("/bottom_2")
def ML_2():
    return render_template('about.html')

# @app.route('/', methods=['GET', 'POST'])
# def index():    


@app.route("/bottom_3")
def bottom_3():
    return render_template('leaflet.html')


@app.route("/bottom_4")
def bottom_4():
    return render_template('Tableau.html')

if __name__ == '__main__':
    app.run(debug=True)