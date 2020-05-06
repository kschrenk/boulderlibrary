from flask import Blueprint, render_template
from flask import current_app as app

admin_bp = Blueprint('admin_bp', __name__,
                     template_folder='templates',
                     static_folder='static')


@admin_bp.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

    