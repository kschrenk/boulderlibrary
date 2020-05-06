from flask import Blueprint, render_template, redirect, jsonify, abort
from flask import current_app as app
from database.models import Gym
# Jinja2
from jinja2 import TemplateNotFound

main_bp = Blueprint('main_bp', __name__, 
    template_folder='templates',
    static_folder='static',
    url_prefix='/main')


@main_bp.route('/gyms', methods=["GET"])
def get_gyms():
    ''' Returns a JSON with all gyms '''
    try:
        data = Gym.query.all()
        body = []
        for gym in data: 
            body.append(gym.formatted())
        
        return render_template('main.html', gyms=body)
    
    except TemplateNotFound:
        abort(404)

    