# Boulder Library API

Nowadays climbers all around the world want to be up-to-date about their favourite climbing gyms. The Boulder Library API lists climbing gyms in different countries and enables climbers to follow their favourite gyms.

This project is based on a python flask backend that communicates with a postgresql database. The API is hosted on Heroku. The frontend development will be on of the future tasks so to test the api use cURL or Postman.

## Getting Started

### Installing Dependecies

#### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment
Once you installed the latest python version setup a virtual environment and activate it. See [further instructions](https://docs.python.org/3/tutorial/venv.html "Python Tutorials") on how to create virtual environments.

#### PIP Dependencies
All the dependecies are listed in the requirements.txt. The following commands will install all required packages.
```bash
pip3 install -r requirements.txt
```

### Environment Variables

To initiate the app first open the setup-example.sh and insert the necessary variables. Afterwards you can rename it to 'setup.sh' or whatever name you prefer. To set env variables run:

```bash
. setup.sh
```

### Setup the database

To initialize the database run
```bash
createdb <YOUR DATABASE NAME>
```

After setting up the database run the migrations.
```
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```

### Run the server

Finally run the local development server by executing:

```bash
flask run
```


## Testing
At first create a new database for testing.
```bash
createdb boulderlibrary_test
```

To test again drop the database and create it again.
```bash
dropdb boulderlibrary_test && createdb boulderlibrary_test
psql boulderlibrary_test < boulderlibrary.psql
```


## API Reference

### Endpoints

+ GET