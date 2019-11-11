"""Minimal flash app"""
from flash import Flask

#Make the application
app = Flash(__name__)

#make the route
@app.route("/")

#define a function
def hello():
    return "Hello world!"
