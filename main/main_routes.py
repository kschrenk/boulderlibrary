import sys
from flask import Blueprint, render_template, redirect, jsonify, abort, flash
from flask import current_app as app
from database.models import Gym, State, City, db
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


@main_bp.route('/gyms/<int:id>', methods=["GET"])
def public_gyms_in_state(id):
    '''
    Returns a json with all gyms in state
    :param id: int.
    '''
    error = False
    try:
        # creates a dictionary with cities and gyms
        query = City.query.filter_by(state_id = id).order_by(City.name).all()
        dic_of_gyms = {}
        for city in query:
            gyms_in_city = city.gyms
            formatted_gyms = []
            for gym in gyms_in_city:
                formatted_gyms.append(gym.formatted())
            dic_of_gyms[city.name] = formatted_gyms
    except Exception:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(422)
    else:
        return jsonify(dic_of_gyms)

