import os
import sys
from flask import current_app as current_app
from flask import Blueprint
from database.models import Gym, State, City, db

admin_bp = Blueprint('admin_bp', __name__)

# @admin_bp('gyms/<int:id>')
# def private_edit_gyms():

#     return jsonify()