from flask import Blueprint, render_template

food = Blueprint ("main", __name__)

@food.route("/")
def index():
    return render_template("index.html")

@food.route("/add")
def add():
    return render_template("add.html")

@food.route ("/view")
def view():
    return render_template("view.html")