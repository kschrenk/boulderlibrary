import os
import sys
from flask import current_app as app
from flask import Blueprint, request, abort, jsonify
from database.models import db, User
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


