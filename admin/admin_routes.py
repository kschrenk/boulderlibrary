import os
import sys
from flask import current_app as current_app
from flask import Blueprint, request, abort, jsonify
from database.models import Gym, State, City, db, get_gym
from auth import require_auth, AuthError

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/gyms/create', methods=["POST"])
@require_auth('create:gyms')
def create_gym(payload):
    '''
    Adds a new gym to the database.
    :INPUT: JSON. Example: 
        {
            "name":"<STRING: GYMS NAME>",
            "address": "<STRING: STREET AND NUMBER>",
            "city": <INT: CITY ID>,
            "website": "<STRING: WEBSITE>",
            "category": <INT: CATEGORY ID>,
            "status": "<STRING: STATUS>"
        }
    '''
    body = request.get_json()
    error = False
    try:        
        gym = Gym(
            name=str(body['name']),
            address=str(body['address']),
            city_id=int(body['city']),
            website=str(body['website']),
            category_id=int(body['category']),
            status_description=str(body['status'])
        )
        gym.insert()
    except Exception:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(422)
    else:
        return jsonify({
            "success": True,
            "message": "Gym successfully added to database"
        })


@admin_bp.route('/gyms/<int:id>', methods=["PATCH"])
@require_auth('update:gyms')
def edit_gym(payload, id):
    '''
    Edit a gym with its id.
    :param id: int.
    '''
    error = False
    try:
        data = request.get_json()
        gym = get_gym(id)
        if gym is None:
            abort(404)
        else: 
            gym.name = str(data['name'])
            gym.address = str(data['address'])
            gym.city_id = int(data['city'])
            gym.website = str(data['website'])
            gym.category_id = int(data['category'])
            gym.status_description = str(data['status'])
            gym.update()
    except Exception:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(422)
    else: 
        return jsonify({
            "success": True,
            "message":  "Gym successfully edited"
        })

    
@admin_bp.route('/gyms/<int:id>', methods=["DELETE"])
@require_auth('delete:gyms')
def delete_gym(payload, id):
    '''
    Delete the gym.
    :param id: int.
    '''
    error = False
    try:
        gym_to_delete = get_gym(id)
        gym_to_delete.delete()
    except Exception:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(422)
    else: 
        return jsonify({
            "success": True,
            "message":  "Gym successfully deleted"
        })

