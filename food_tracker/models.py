from .extensions import db

log_food = db.Table('log_food',
    db.Column('log_id', db.Integer, db.ForeignKey('log.id'), primary_key=True),
    db.Column('food_id', db.Integer, db.ForeignKey('food.id'), primary_key =True)
    
)

# Creating Food class to recieve all variables required to create a food, all values are not nullable.
class Food(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False)
    proteins = db.Column(db.Integer, nullable = False)
    carbs = db.Column(db.Integer, nullable = False)
    fats = db.Column(db.Integer, nullable = False)

    # Property function to add the total calories, 4 calories per carb and protein, 9 per fat
    @property
    def calories(self):
        return self.proteins * 4 + self.carbs * 4 + self.fats * 9

#Allows us to log a new date to our tracker
class Log(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, nullable = False)
    foods = db.relationship('Food', secondary=log_food, lazy="dynamic")