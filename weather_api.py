import pandas as pd
import numpy as np
import requests as req
import time
import json
import random
from pprint import pprint
from collections import OrderedDict

def API_Call():
    base_url = "http://api.openweathermap.org/data/2.5/weather?q=new%20york,us&appid=25f70f11d823a01fb8cf2860c0e875c1"
    NY = req.get(base_url).json()
    NY_list = str(NY)
    DF = pd.DataFrame(NY_list)
    return DF

