#Importing Libraries
import pandas as pd
import numpy as np
import pyspark.sql.functions as func
import datetime as dt
import re
import time
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import seaborn as sns
<<<<<<< HEAD
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

engine = create_engine("sqlite:///total_passengers.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Create our session (link) from Python to the DB
session = Session(engine)

inspector = inspect(engine)
inspector.get_table_names()
df = []
columns = inspector.get_columns('total_passengers')

def sub_data ():
    for column in columns:

        df.append (column["name"])


    return str(df)
=======

>>>>>>> Engy
