from flask import Blueprint, render_template, request, redirect, url_for
from food_tracker.models import Food, Log
from food_tracker.extensions import db

from datetime import datetime



main = Blueprint ("main", __name__)

# Home page of the food tracker app
@main.route("/")
def index():
    logs = Log.query.order_by(Log.date.desc()).all()

    log_dates = []
    # For loop to count proteins, carbs, fats and calories for each date separately
    for log in logs:
        proteins = 0
        carbs = 0
        fats = 0
        calories = 0
        # For loop to add together the maronutrients and calories for each specific date
        for food in log.foods:
            proteins += food.proteins
            carbs += food.carbs
            fats += food.fats
            calories += food.calories
        #Adding the final numbers to the main  page    
        log_dates.append({
            "log_date": log,
            "proteins": proteins,
            "carbs": carbs,
            "fats": fats,
            "calories": calories
        })

    return render_template("index.html", log_dates= log_dates)

# This function allows the user to create a new date to log their food
@main.route("/create_log", methods=["POST"])
def create_log():
    date = request.form.get("date")
    # Makes sure each date is displayed correctly
    log = Log(date = datetime.strptime(date, "%Y-%m-%d"))
    db.session.add(log)
    db.session.commit()
    return redirect(url_for("main.view", log_id=log.id))


@main.route("/add")
def add():
    foods = Food.query.all()
    return render_template("add.html", foods=foods, food =None)

# Allows user to add a new food
@main.route("/add", methods=["POST"])
def add_post():
    #Creating the form for users to fill
    food_name = request.form.get("food-name")
    proteins = request.form.get("protein")
    fats = request.form.get("fat")
    carbs = request.form.get("carbohydrates")
    #Creating the ID for each specific food
    food_id = request.form.get("food_id")

    #Allows the user to update an existing food record
    if food_id:
        food = Food.query.get_or_404(food_id)
        food.name = food_name
        food.proteins = proteins
        food.carbs = carbs
        food.fats = fats
    #If no existing food id is provided, the user will add a new food to the app
    else:    
        new_food = Food(name=food_name, proteins=proteins, carbs=carbs, fats=fats)
        db.session.add(new_food)

    db.session.commit()
    return redirect(url_for("main.add"))

#Allows user to delete a food item
@main.route("/delete_food/<int:food_id>")
def delete_food(food_id):
    food = Food.query.get(food_id)
    db.session.delete(food)
    db.session.commit()
    return redirect(url_for("main.add"))


@main.route("/edit_food/<int:food_id>")
def edit_food(food_id):
    food = Food.query.get_or_404(food_id)
    foods = Food.query.all()
    return render_template("add.html", food = food, foods=foods)

# Creating the view page once a user clicks on a specific date in the log
@main.route ("/view/<int:log_id>")
def view(log_id):
    log = Log.query.get_or_404(log_id)
    foods = Food.query.all()
    # Create dict to have totals of macronutrients
    totals = {
        "protein": 0,
        "carbs":0,
        "fat":0,
        "calories": 0
    }
    #For loop to add up total macronutrients
    for food in log.foods:
        totals["protein"] += food.proteins
        totals["carbs"] += food.carbs
        totals["fat"] += food.fats
        totals["calories"] += food.calories

    return render_template("view.html", foods = foods, log=log, totals=totals)

# When a user adds the food to the log, not only will it get stored in the database it will also be placed into the log and shown on screen for that date
@main.route ("/add_food_to_log/<int:log_id>", methods=["POST"])
def add_food_to_log(log_id):
    log = Log.query.get_or_404(log_id)
    selected_food = request.form.get("food-select")
    food = Food.query.get(int(selected_food))
    log.foods.append(food)
    db.session.commit()
    return redirect(url_for("main.view", log_id=log_id))

# Allows user to remove a food from the log
@main.route("/remove_food_from_log/<int:log_id>/<int:food_id>")
def remove_food_from_log(log_id, food_id):
    log = Log.query.get(log_id)
    food = Food.query.get(food_id)
    log.foods.remove(food)
    db.session.commit()
    return redirect(url_for("main.view", log_id=log_id))