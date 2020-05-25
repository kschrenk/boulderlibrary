import sys
from flask import Blueprint, render_template, redirect, jsonify, abort, flash
from flask import current_app as app
from database.models import Gym, State, City, db

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/gyms', methods=["GET"])
def public_all_gyms():
    '''
    Displays all gyms in the database
    :returns: JSON.
    '''
    body = []
    error = False
    try:
        query = Gym.query.order_by(Gym.city_id.name).all()
        for gym in query:
            body.append(gym.formatted())
    except Exception:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(422)
    else:
        return jsonify(body)


@main_bp.route('/gyms/<int:id>', methods=["GET"])
def public_gym(id):
    '''
    Returns the gym by id.
    :param id: int:
    '''
    error = False
    try:
        query = Gym.query.filter(Gym.id == id).one_or_none()
        if query is None:
            abort(404)
        body = [query.formatted()]
    except Exception:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(422)
    else:
        return jsonify(body)


@main_bp.route('/state/<int:id>/gyms', methods=["GET"])
def public_gyms_in_state(id):
    '''
    Returns a json with all gyms in state
    :param id: int.
    '''
    error = False
    try:
        query = City.query.filter_by(state_id = id).order_by(City.name).all()
        # creates a dictionary with cities and gyms
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








