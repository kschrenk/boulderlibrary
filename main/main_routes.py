from flask import Blueprint, render_template, redirect, jsonify, abort
from flask import current_app as app
from database.models import Gym, State
# Jinja2
from jinja2 import TemplateNotFound

main_bp = Blueprint('main_bp', __name__, 
    template_folder='templates',
    static_folder='static',
    url_prefix='/main')


@main_bp.route('/', methods=["GET"])
def public_home():
    return render_template('home.html')
    

@main_bp.route('/gyms', methods=["GET"])
def public_gyms():
    query = State.query.order_by(State.name).all()
    return render_template('gyms.html', states=query)

