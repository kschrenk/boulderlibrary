import os
import sys
from flask import current_app as current_app
from flask import Blueprint, request, abort, jsonify
from database.models import Gym, State, City, db

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/gyms/create', methods=["POST"])
def edit_gyms():
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
            name=body['name'],
            address=body['address'],
            city_id=body['city'],
            website=body['website'],
            category_id=body['category'],
            status_description=body['status']
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

