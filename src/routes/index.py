from flask import Blueprint, render_template

ind = Blueprint('index', __name__)

@ind.route('/')
def index():
    return render_template('index.html')
