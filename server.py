"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

# from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
# app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


#You also need get methods for your front end to get data from tables to present to the user
#paint, canvase, and weather GET methods. You will use these GET endpoints on the frontend to 
# display this info from your databse on the forms (as dropdowns)

@app.route('/get_paint_types')
def get_paint_types():
""" Returns object of PaintTypes from database"""
    paint_types = crud.get_paint_types()

    return jsonify(paint_types)

# POst methods gather info from the front end to give eto the datbase
@app.route('/creation_form', methods=["POST"])
def collect_painting_input():
    """Gathering info from the creation form for the user to create a dry time"""

    painting_name = request.form.get("painting_name")
    canvas_type = request.form.get("canvas_id")
    weather_condition = request.form.get("weather_id")
    paint_type = request.form.get("paint_id")

    creation_form = crud.create_creation_form(painting_name, canvas_type, weather_condition, paint_type)

    return jsonify(creation_form)   


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)





