import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from database.models import setup_db, User, db

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

  # endpoints

  @app.route('/')
  def public_index():
    message = "App is running"

    return jsonify({
      "success":True,
      "message": message
    })

  return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)


