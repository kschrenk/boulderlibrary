from flask import current_app as app
from flask import jsonify, redirect, render_template, session, url_for, flash

from functools import wraps
import json
import os
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Authentification
oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id=os.environ['CLIENT_ID'],
    client_secret=os.environ['CLIENT_SECRET'],
    api_base_url=os.environ['API_BASE_URL'],
    access_token_url=os.environ['ACCESS_TOKEN_URL'],
    authorize_url=os.environ['AUTHORIZE_URL'],
    client_kwargs={
        'scope': 'openid profile email',
    },
)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            flash('You are currently logged out. Login first to visit your Dashboard.')
            #Redirect to Login page here
            return redirect('/')
        return f(*args, **kwargs)
    
    return decorated



