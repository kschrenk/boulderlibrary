import os
from flask import (
    Flask, 
    request, 
    abort, 
    jsonify, 
    abort)
    
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from database.models import (
    setup_db,
    db, 
    User, City, State)

def create_app(test_config=None):
  
    # create and configure the app
    
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    # setup CORS

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # -------------------------------------------------------------------- #
    # Controllers.
    # -------------------------------------------------------------------- #

    @app.route('/')
    def public_index():
        message = "App is running"

        return jsonify({
        "success":True,
        "message": message
        })


    @app.route('/user')
    def public_user():
        list_of_users = []
        all_users = User.query.all()
        for user in all_users:
            list_of_users.append(user.name)

        return jsonify({
        "message": "success",
        "user": list_of_users
        })


    @app.route('/climbing-gyms/create', methods=["POST"])
    def create_gym():
        try: 
            incoming_data = request.get_json()
            print(incoming_data)
            name = incoming_data['name']

            return jsonify({
                "success": True,
                "message": f"Successfully added {name} to Database"
            })
        
        except KeyError:
            abort(422)
        
    # -------------------------------------------------------------------- #
    # error handler
    # -------------------------------------------------------------------- #

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422



    return app

      
APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)


