# Flask Import with:
# Flask pips for additional options
# render template for html page
# redirect to a specified html page
# flash to give user input on outcome of interaction
# request option to allow for a request to a login form
from flask import Flask, render_template, redirect, flash, request, url_for
# Jinja2 import for option to imbed into html
import jinja2
# Importing the melons.py for use of the @app.route endpoints
import melons


# Used to create the main application
app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined  # for debugging purposes


# Routes options to html
@app.route("/")
def homepage():
    return render_template("base.html")


# A html page returning ALL melons in the dictionary
@app.route("/melons")
def all_melons():
    melon_list = melons.get_all()
    return render_template("all_melons.html", melon_list=melon_list)


# A html page to display details about a single melon
@app.route("/melons/<melon_id>")
def melon_details(melon_id):
    return render_template("melon_details.html")


# A html page displaying cart details
@app.route("/cart")
def show_shopping_cart():
    return render_template("cart.html")


# An endpoint to add a melon to the cart
@app.route("/add_to_cart/<melon_id>")
def add_to_cart(melon_id):
    return f"{melon_id} added to cart"


# Execute code when file runs as Script and application runner
if __name__ == "__main__":
    app.run(debug=True, port=8000, host="localhost")
