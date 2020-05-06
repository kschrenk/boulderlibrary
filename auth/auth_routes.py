from flask import Blueprint, render_template
from flask import current_app as app

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', url_prefix='/login')

@auth_bp.route('/', methods=['GET'])
def login():
    return render_template('login.html')

    