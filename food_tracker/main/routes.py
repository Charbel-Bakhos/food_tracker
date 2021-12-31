from flask import Blueprint, render_template
from sqlalchemy.ext.declarative.api import comparable_using, request

main = Blueprint ("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/add")
def add():
    return render_template("add.html")

@main.route("/add", methods=["POST"])
def add_post():
    food_name = request.form.get("food-name")
    proteins = request.form.get("protein")
    fats = request.form.get("fat")
    carbs = request.form.get("carbs")
    return f"<h1>{ food_name } - { proteins } - { carbs } - { fats }</h1>"

@main.route ("/view")
def view():
    return render_template("view.html")