# Installing Dependecies

## Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

## Virtual Environment


## PIP Dependencies


## Configuration Variables

To initiate the App run the setup.sh. This will set the configuration variables.

```bash
. setup.sh
```

## Setup the database

To initialize the database run
'''
createdb myclimbinggym
'''

Than initialize the database with the manager.py
'''
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
'''

# Testing
At first create a new database for testing.
```bash
createdb boulderlibrary_test
```

To test again drop the database and create it again.
```bash
dropdb boulderlibrary_test && createdb boulderlibrary_test
psql boulderlibrary_test < boulderlibrary.psql
```