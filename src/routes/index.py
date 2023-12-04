from flask import Blueprint, render_template, request, redirect, url_for

ind = Blueprint('index', __name__)

@ind.route('/')
def index():
    return render_template('index.html')
