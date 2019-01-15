import flask
from flask import request, jsonify
import weather_api

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/weather', methods=['GET'])
def weather():
    wetherData = weather_api.API_Call()
    return wetherData

if __name__ == "__main__":
   app.run(debug=True)