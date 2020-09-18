from flask import Blueprint, render_template


#Register blueprint
frontend = Blueprint('frontend', __name__)

#Route for frontend
@frontend.route('/')
def index():
    return render_template('ranky.html')