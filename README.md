

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
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
'''