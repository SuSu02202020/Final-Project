from flask import Flask, render_template, redirect,url_for
from flask_pymongo import PyMongo
import subway

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/app.py"
mongo = PyMongo(app)

# posts = [    {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/bottom_3")
def bottom_3():
    return render_template('about.html', title='About')


@app.route("/bottom_4")
def bottom_4():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)