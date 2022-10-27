# Flask Import with:
# Flask pips for additional options
# render template for html page
# redirect to a specified html page
# flash to give user input on outcome of interaction
# request option to allow for a request to a login form
from flask import Flask, render_template, redirect, flash, request, url_for, session
# Jinja2 import for option to imbed into html
import jinja2
# Importing the melons.py for use of the @app.route endpoints
import melons
# Import to create a llogin form
from forms import LoginForm
# Importing to validate registered customer details for user functionaliyt
import customers


# Used to create the main application
app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined  # for debugging purposes
app.secret_key = 'dev' # temp key location for session functionality

# Routes options to html
@app.route("/")
def homepage():
    return render_template("base.html")


# a html page to allow a user to login
@app.route("/login", methods=["GET", "POST"])
def login():
    # Assist user to log-in
    form = LoginForm(request.form)

    if form.validate_on_submit():
        # form submited with valid data
        username = form.username.data
        password = form.password.data

        # Verify username exists in registration
        user = customers.get_by_username(username)

        if not user or user['password'] != password:
            flash("Invalid username or password")
            return redirect('/login')

        # Session cookies used to track logged-in users actions for better UX
        session["username"] = user['username']
        flash("Logged in.")
        return redirect("/melons")

    #Form submission issue or data invalid
    return render_template("login.html", form=form)


# Funciton to allow user to log-out
@app.route("/logout")
def logout():
    del session["username"]
    flash("Logged out.")
    return redirect("/login")


# A html page returning ALL melons in the dictionary
@app.route("/melons")
def all_melons():
    melon_list = melons.get_all()
    return render_template("all_melons.html", melon_list=melon_list)


# A html page to display details about a single melon
@app.route("/melon/<melon_id>")
def melon_details(melon_id):
    melon = melons.get_by_id(melon_id)
    return render_template("melon_details.html", melon=melon)


# An endpoint to add a specified melon to the cart from the melon_details.html to the cart.html
@app.route("/add_to_cart/<melon_id>")
def add_to_cart(melon_id):
    
    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    
    cart[melon_id] = cart.get(melon_id, 0) + 1
    session.modified = True
    flash(f"Melon {melon_id} successfully added to cart.")
    print(cart)

    return redirect("/cart")

# A html page displaying cart details
@app.route("/cart")
def show_shopping_cart():
    
    order_total = 0
    cart_melons = []


    # GET cart dictionary from open session (cookies)
    cart = session.get("cart", {})
    
    for melon_id, quantity in cart.items():
        melon = melons.get_by_id(melon_id)

        total_cost = quantity * melon.price
        order_total += total_cost

        melon.quantity = quantity
        melon.total_cost = total_cost

        cart_melons.append(melon)
    
    return render_template("cart.html", cart_melons=cart_melons, order_total=order_total)


# function linked to a btn to empty the session["cart"] dictionary
@app.route("/empty-cart")
def empty_cart():
    session["cart"] = {}

    return redirect("/cart")


# Execute code when file runs as Script and application runner
if __name__ == "__main__":
    app.run(debug=True, port=8000, host="localhost")
