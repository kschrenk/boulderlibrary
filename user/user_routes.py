import os
import sys
from flask import current_app as app
from flask import Blueprint, request, abort, jsonify
from database.models import db, User, Gym
from auth import require_auth, AuthError


user_bp=Blueprint('user_bp', __name__, url_prefix='/user')


@user_bp.route('/create', methods=['POST'])
def public_create_user():
    data = request.get_json()
    error = False
    try: 
        new_user = User(
            name=str(data['user']),
            last_name=str(data['last_name'])
            )
        new_user.insert()
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
            "message": 'User was successfully added to database.'
        })


@user_bp.route('/<int:id>/favourites', methods=['GET'])
@require_auth('get:favourite_gyms')
def get_favourite_gyms(payload, id):
    error = False
    try:
        response = []
        user = User.query.get(id)
        favourite_gyms = user.gyms
        for gym in favourite_gyms:
            response.append(gym.formatted())
    except Exception:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error: 
        abort(422)
    else:
        return jsonify(response)


@user_bp.route('/favourites/add', methods=['POST'])
@require_auth('favor:gyms')
def add_favourite_gym(payload):
    body = request.get_json()
    error = False
    try:
        user = User.query.get(body['user_id'])
        gym_to_add = Gym.query.get(body['gym_id'])
        user.gyms.append(gym_to_add)
        db.session.commit()
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
            "message": "Gym added to favourite gyms."
        })


@user_bp.route('favourites/remove', methods=['DELETE'])
@require_auth('remove:favourite_gyms')
def remove_favourite_gym(payload):
    body = request.get_json()
    error = False
    try:
        user = User.query.get(body['user_id'])
        gym_to_remove = Gym.query.get(body['gym_id'])
        user.gyms.remove(gym_to_remove)
        db.session.commit()
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
            "message": "Gym successfully removed from users favourites."
        })
