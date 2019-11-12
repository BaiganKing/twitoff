"""Minimal flash app"""
from flash import Flask

#Make the application
app = Flash(__name__)

#make the route
@app.route("/")

#define a function
def hello():
    return render_template('home.html')

#creating another route
@app.route("/about")

def preds():
    return render_template('about.html')
