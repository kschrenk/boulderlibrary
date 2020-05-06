# Run in development mode
export FLASK_APP=app.py
export FLASK_DEBUG=True
export FLASK_ENV=development

# Environment variables for local dev
export DATABASE_URL='postgresql://schrenkk@localhost:5432/myclimbinggym'
export SQLALCHEMY_TRACK_MODIFICATIONS=False

# Auth0
export AUTH0_DOMAIN='dev-wd714d8h.eu.auth0.com' 
export API_AUDIENCE='boulder'