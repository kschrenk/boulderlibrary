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
    render_template) 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Data
from database.models import (
    setup_db,
    db,
    User, City, State, Category, Gym, Status)
from database.data import (
    Country
)

# Blueprints
from main.main_routes import main_bp 
from admin.admin_routes import admin_bp

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
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    
    # setup CORS
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # -------------------------------------------------------------------- #
    # App data.
    # -------------------------------------------------------------------- #
    '''
    Data to initialize the database. 
    This includes:
        * Cities and States
        * Status descriptions (open or closed)
        * Categories (Boulder or rope climbing gyms)
    '''

    # load cities and states
    if (len(State.query.all()) == 0) and (len(City.query.all()) == 0):
        c1 = Country('Germany')
        c1_info = c1.get_states_and_cities()  
        try:   
            for state in list(c1_info.keys()):
                new_state = State(name=state)
                db.session.add(new_state)
            for state in list(c1_info.keys()):
                state_in_table = State.query.filter(State.name == state).one_or_none()
                if state_in_table is None:
                    print('Could not add cities')
                else:
                    for city in c1_info[state]:
                        new_city = City(name=city, state_id=state_in_table.id)
                        db.session.add(new_city)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(422)  
    else:
        print('=> Cities and States are loaded')

    
    # load status description
    if len(Status.query.all()) == 0:
        db.session.add_all([
            Status(description='open'),
            Status(description='closed')
        ])
        db.session.commit()
    else:
        print('=> Status Description are loaded')


    # load categories
    if len(Category.query.all()) == 0:
        db.session.add_all([
            Category(description='Boulder'),
            Category(description='Rope climbing'),
            Category(description='Boulder and rope climbing')
        ])
        db.session.commit()
    else:
        print('=> Categories are loaded')


    # -------------------------------------------------------------------- #
    # Controller.
    # -------------------------------------------------------------------- #
    
    @app.route('/')
    def index():
        return redirect(url_for( 'main_bp.all_gyms' ))


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


