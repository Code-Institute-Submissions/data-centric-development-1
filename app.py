# Import Modules

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Environment Variables

app.config["MONGO_DBNAME"] = 'holiday_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

# Get (Read) Holidays

@app.route("/")
@app.route("/get_holidays")
def get_holidays():
    return render_template("holidays.html", holidays=mongo.db.holidays.find().sort("depart_date"))

# Add Holiday
    
@app.route("/add_holiday")
def add_holiday():
    return render_template("addholiday.html", categories=mongo.db.categories.find())

@app.route("/insert_holiday", methods=["POST"])
def insert_holiday():
    holidays = mongo.db.holidays
    holidays.insert_one(request.form.to_dict())
    return redirect(url_for("get_holidays"))

# Edit (Update) Holiday

@app.route("/edit_holiday/<holiday_id>")
def edit_holiday(holiday_id):
    the_holiday = mongo.db.holidays.find_one({"_id": ObjectId(holiday_id)})
    all_categories = mongo.db.categories.find()
    return render_template("editholiday.html", holiday=the_holiday, categories=all_categories)

@app.route("/update_holiday/<holiday_id>", methods=["POST"])
def update_holiday(holiday_id):
    holidays = mongo.db.holidays
    holidays.update( {'_id': ObjectId(holiday_id)},
    {
        'holiday_title':request.form.get('holiday_title'),
        'category_name':request.form.get('category_name'),
        'holiday_description': request.form.get('holiday_description'),
        'nights': request.form.get('nights'),
        'depart_date':request.form.get('depart_date')
    })
    return redirect(url_for("get_holidays"))

# Delete Holiday

@app.route("/delete_holiday/<holiday_id>")
def delete_holiday(holiday_id):
    mongo.db.holidays.remove({'_id': ObjectId(holiday_id)})
    return redirect(url_for("get_holidays"))

# Get (Read) Categories

@app.route("/get_categories")
def get_categories():
    return render_template("categories.html", categories=mongo.db.categories.find().sort("category_name"))

# Edit (Update) Category

@app.route("/edit_category/<category_id>")
def edit_category(category_id):
    return render_template("editcategory.html", category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))

@app.route("/update_category/<category_id>", methods=["POST"])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for("get_categories"))

# Delete Category

@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for("get_categories"))

# Add Category

@app.route("/insert_category", methods=["POST"])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for("get_categories"))

@app.route("/add_category")
def add_category():
    return render_template("addcategory.html")

# If Statement with Debug Mode On

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
    