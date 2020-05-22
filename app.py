import os
import sys

# Flask
from flask import (
    Flask,
    request,
    abort,
    jsonify,
    abort,
    redirect,
    url_for,
    render_template
)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Data
from database.models import (
    setup_db,
    db,
    User,
    City,
    State,
    Category,
    Gym,
    Status
    )
from database.data import (
    Country
)

# Blueprints
from main.main_routes import main_bp as main
from admin.admin_routes import admin_bp as admin
from user.user_routes import user_bp as user

# Authentification
from auth import AuthError


# -------------------------------------------------------------------- #
# Flask App.
# -------------------------------------------------------------------- #
def create_app(test_config=None):

    # -------------------------------------------------------------------- #
    # App config.
    # -------------------------------------------------------------------- #

    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    # register blueprints
    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(user)

    # setup CORS
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # -------------------------------------------------------------------- #
    # Controller.
    # -------------------------------------------------------------------- #

    @app.route('/')
    def index():
        return redirect(url_for('main_bp.public_all_gyms'))

    @app.route('/data/init', methods=['POST'])
    def initialize_data():
        '''
        This endpoint initializes country data
        with all states and cities in each country.
        '''
        body = request.get_json()
        response = {}
        error = False
        try:
            if 'country' in body:
                new_country = body['country']

                # init cities and states in country
                if (len(State.query.all()) == 0) and (len(City.query.all()) == 0):
                    c1 = Country(new_country)
                    c1_info = c1.get_states_and_cities()
                    for state in list(c1_info.keys()):
                        new_state = State(name=state)
                        db.session.add(new_state)
                    for state in list(c1_info.keys()):
                        query = State.query.filter(State.name == state)
                        state_in_table = query.one_or_none()
                        if state_in_table is None:
                            print('Could not add cities')
                        else:
                            for city in c1_info[state]:
                                new_city = City(
                                    name=city,
                                    state_id=state_in_table.id
                                    )
                                db.session.add(new_city)
                    db.session.commit()
                    response['country'] = 'Cities and states initialized.'
                else:
                    response['country'] = 'already loaded'

                # init status description
                if len(Status.query.all()) == 0:
                    db.session.add_all([
                        Status(description='open'),
                        Status(description='closed')
                    ])
                    db.session.commit()
                    response['status'] = 'Status initialized'
                else:
                    response['status'] = 'already loaded'

                # init categories
                if len(Category.query.all()) == 0:
                    db.session.add_all([
                        Category(description='Boulder'),
                        Category(description='Rope climbing'),
                        Category(description='Boulder and rope climbing')
                    ])
                    db.session.commit()
                    response['categories'] = 'Categories initialized'
                else:
                    response['categories'] = 'already loaded'

            else:
                response['message'] = 'Wrong JSON format'

        except Exception:
            error = True
            db.session.rollback()
            print(sys.exc_info)
        finally:
            db.session.close()
        if error:
            abort(422)
        else:
            return jsonify(response)

    # -------------------------------------------------------------------- #
    # Error handler.
    # -------------------------------------------------------------------- #

    @app.errorhandler(401)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
            }), 404

    @app.errorhandler(404)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
            }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
            }), 422

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
