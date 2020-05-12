import sys
import os
import json
from flask import Blueprint, render_template, session, redirect,url_for
from flask import current_app as app
from user.auth import requires_auth, auth0
from six.moves.urllib.parse import urlencode

user_bp = Blueprint('user_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/user')


@user_bp.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect('/user/dashboard')


@user_bp.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=os.environ['CALLBACK_URL'])


@user_bp.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('dashboard.html', userinfo=session['profile'], userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))


@user_bp.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for( 'main_bp.public_home' , _external=True), 'client_id': os.environ['CLIENT_ID']}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

