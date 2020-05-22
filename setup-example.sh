# ------------------------------------------- #
# Necessary env variables for local dev

# e.g.: export DATABASE_URL='postgresql://schrenkk@localhost:5432/myclimbinggym'
export DATABASE_URL= '<YOUR POSTGRESQL DATABASE URL>'
export SQLALCHEMY_TRACK_MODIFICATIONS=False

# Tokens
export ADMIN_TOKEN = ''
export USER_TOKEN = ''


# ------------------------------------------- #
# Testing

# e.g.: export DATABASE_BASE_URL='postgresql://schrenkk@localhost:5432/'
export DATABASE_BASE_URL='<THE POSTGRESQL BASE URL WITHOUT THE DATABASE NAME'

# export DATABASE_TEST_NAME='boulderlibrary_test'
export DATABASE_TEST_NAME='<DATABASE TEST NAME>'


# ------------------------------------------- #
# Flask (optional)

# Run flask in development mode
export FLASK_APP=app.py
export FLASK_DEBUG=True
export FLASK_ENV=development

