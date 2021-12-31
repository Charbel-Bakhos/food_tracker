from flask import Blueprint

food = Blueprint ("main", __name__)

@food.route("/")
def index():
    return "blueprint test"