# Run in development mode
export FLASK_APP=app.py
export FLASK_DEBUG=True
export FLASK_ENV=development

# Environment variables for local dev
export SECRET_KEY='kd/keilJKAI921578_dsl%g'
export DATABASE_BASE_URL='postgresql://schrenkk@localhost:5432/'
export SQLALCHEMY_TRACK_MODIFICATIONS=False

# Auth0
export CLIENT_ID='Xdlw5tLFRthjh9o57e25HnFyjIkm3Ddh'
export CLIENT_SECRET='4ujS23WXt7eRdIjKgyO4DFsHCADvarPk7ScxXmNo6O65e-O9_8bMtFx9gvp-mX4F'
export API_BASE_URL='https://dev-wd714d8h.eu.auth0.com'
export ACCESS_TOKEN_URL='https://dev-wd714d8h.eu.auth0.com/oauth/token'
export AUTHORIZE_URL='https://dev-wd714d8h.eu.auth0.com/authorize'
export CALLBACK_URL='http://localhost:5000/user/callback'
export AUTH0_DOMAIN='dev-wd714d8h.eu.auth0.com' 
export API_AUDIENCE='boulder'