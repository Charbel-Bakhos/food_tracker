## Charbel Bakhos 
## Calorie Tracker app
<hr>

Welcome to my calorie tracking app. It is designed to allow users to reach their fitness and health goals by keeping track of the amount of calories they ingest per day.

The app currently has three pages:
- Home page
- Date in food log
- Add Food page

From the home page, the user will input a date to add to their log. Let's say the user will be tracking the current days food, they will use the current date. Once they add the date they will be taken to a page viewing only that specific date where they can add food that they have previously stored in the tracker. It will then display the total protein, carbs, fat and calories for the day, and list each individual item with its macronutrients.

If the user navigates to the "Add Food Item" page, they will be prompted for 4 not nullable items. The user must input into each form before hitting submit. A good way to do this is to check the nutritional information near the barcode of the food you are eating, or search it online! When a food is added, it is stored under Existing food items with its details, and options to edit or delete the item. Once an item is logged, it can be added to a day in the tracker via the dates page.

To run the app:
- Clone the github repository to a folder of your choice
- Create a virtual environment ```virtualenv venv```
- Run ```pip install -r requirements.txt``` to install all required modules
- Run ```flask run```
- Find the address that flask is running from, type this into your browser and go ahead!


<hr>

## NOTES
- All styling was found via bootstrap templates online
- HTML pages were slightly edited to match the code under the routes.py and models.py codes
- App is not currently fully functional. A food item can not be added twice or app with throw an error. There is currently no error handling in the app
