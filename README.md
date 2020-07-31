# Boulder Library API

Nowadays climbers all around the world want to be up-to-date about their favourite climbing gyms. The Boulder Library API lists climbing gyms in different countries and enables climbers to follow their favourites.

This project is based on a python flask backend that communicates with a postgresql database. The API is hosted on Heroku. The frontend development will be one of the future tasks so to test the api use cURL or Postman.

## Getting Started

### Installing Dependecies


#### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### Virtual Environment
Once you installed the latest python version setup a virtual environment and activate it. See [further instructions](https://docs.python.org/3/tutorial/venv.html "Python Tutorials") on how to create virtual environments.
```
. venv/bin/activate
```

#### PIP Dependencies
All the dependecies are listed in the requirements.txt. The following commands will install all required packages.
```bash
pip3 install -r requirements.txt
```


### Environment Variables
The app is configured by env variables that are stores in the setup-example.sh. Just rename it to setup.sh and execute it with
```bash
. example.sh
```


### Setup the database
For the database you need to have Postgresql installed. If you use Mac Os just use [Homebrew](https://formulae.brew.sh/formula/postgresql). But there are other ways for Mac and Windows. After installing postgresql create a new database with:
```bash
createdb boulderlibrary
```

To insert some data into yur boulderlibrary database just import the dump in the database directory with
```bash
psql boulderlibrary < path/to/database.sql
```

After setting up the database run the migrations.
```
python3 manage.py db migrate
python3 manage.py db upgrade
```

### Run the server
We are ready to go. To launch the app just execute
```bash
flask run
```
and the app will start run in development mode on your local environment.


## Testing
There are unittests in the test_app.py to test the different endpoints. They are based on the [unittest framework](https://docs.python.org/3/library/unittest.html) and sure the quality of the app. To initialize the test follow the instructions.
```bash
createdb boulderlibrary_test
psql boulderlibrary_test < boulderlibrary.psql
python3 test_app.py
```

To test again drop the database and create it again.
```bash
dropdb boulderlibrary_test && createdb boulderlibrary_test && psql boulderlibrary_test < boulderlibrary.psql && python3 test_app.py
```


## API Reference

### Data Endpoints
The boulderlibrary is based on city and state data. To gather the necessary information for a country developers need to initialize the data. There is already a JSON stored in the database directory for Germany that was gathered at the [Rest Countries Api](https://restcountries.eu/). To initialize the country data in your database you can eather import the boulderlibrary.psql or you send the post request to the endpoint.

With the first init also the categories and different status get initialized. When there is already data in the database it just checks and reponses with 'already loaded'.

#### POST '/data/init'

```
Body
{
	"country": "Germany"
}

Response
{
    'country': 'Cities and states initialized.',
    'status': 'Status initialized',
    'categories': 'Categories initialized'
}

```


### Public Endpoints

#### GET '/gyms'
Returns a list with all gyms in the database.

```
[
  {
    "address": "Landsberger Str. 185",
    "category": "Boulder",
    "city": "Munich",
    "id": 2,
    "name": "Einstein",
    "status": "closed",
    "website": "https://muenchen.einstein-boulder.com/"
  },
  {
    "address": "Hanne-Hiob-Straße 4",
    "category": "Boulder",
    "city": "Munich",
    "id": 1,
    "name": "Boulderwelt Ost",
    "status": "open",
    "website": "https://www.boulderwelt-muenchen-ost.de/"
  }, ...
]
```

#### GET '/gyms/<int:id>'
Returns the gym with the correspondent id.
```
[
  {
    "address": "Hanne-Hiob-Straße 4",
    "category": "Boulder",
    "city": "Munich",
    "id": 1,
    "name": "Boulderwelt Ost",
    "status": "open",
    "website": "https://www.boulderwelt-muenchen-ost.de/"
  }
]
```

#### GET /state/<int:id>/gyms
Returns all gyms in the state.
```
{
  "Miltenberg": [],
  "Mindelheim": [],
  "Munich": [
    {
      "address": "Landsberger Str. 185",
      "category": "Boulder",
      "city": "Munich",
      "id": 2,
      "name": "Einstein",
      "status": "closed",
      "website": "https://muenchen.einstein-boulder.com/"
    },
    {
      "address": "Hanne-Hiob-Straße 4",
      "category": "Boulder",
      "city": "Munich",
      "id": 1,
      "name": "Boulderwelt Ost",
      "status": "open",
      "website": "https://www.boulderwelt-muenchen-ost.de/"
    },
    {
      "address": "West-Straße 8",
      "category": "Boulder",
      "city": "Munich",
      "id": 9,
      "name": "Boulderwelt West",
      "status": "closed",
      "website": "https://www.boulderwelt-muenchen-west.de/"
    }
  ],
  "Nuremberg": [
    {
      "address": "Gebertstraße 9",
      "category": "Boulder",
      "city": "Nuremberg",
      "id": 6,
      "name": "Cafe Kraft",
      "status": "closed",
      "website": "https://cafekraft.de/"
    }
  ],
  "Regensburg": [
    {
      "address": "Im Gewerbepark A46",
      "category": "Boulder",
      "city": "Regensburg",
      "id": 16,
      "name": "Boulderwelt Regensburg",
      "status": "closed",
      "website": "https://www.boulderwelt-regensburg.de/"
    }
  ]
}
```

### User Endpoints

#### POST 'user/create'
Creates a new user.
```
{
  "message": "User was successfully added to database.",
  "success": true
}
```

#### GET 'user/<int:id>/favourites'
Displays the users favourite gyms.
```
[
  {
    "address": "Hanne-Hiob-Straße 4",
    "category": "Boulder",
    "city": "Munich",
    "id": 1,
    "name": "Boulderwelt Ost",
    "status": "open",
    "website": "https://www.boulderwelt-muenchen-ost.de/"
  },
  {
    "address": "Im Gewerbepark A46",
    "category": "Boulder",
    "city": "Regensburg",
    "id": 16,
    "name": "Boulderwelt Regensburg",
    "status": "closed",
    "website": "https://www.boulderwelt-regensburg.de/"
  }
]
```

#### POST 'user/favourites/add'
Adds a favourite gym to the user.
```
{
  "message": "Gym added to favourite gyms.",
  "success": true
}
```

#### DELETE 'user/favourites/remove'
Deletes a gym from the user's favourites.
```
{
  "message": "Gym successfully removed from users favourites.",
  "success": true
}
```

### Admin Endpoints

#### POST '/gyms/create'
Creates a new gym in the database.
```
Body JSON example to include in post request:
{
	"name":"DAV Schuppen",
	"address": "West-Straße 3",
	"city": 111,
	"website": "https://www.dav-schuppen.de/",
	"category": 1,
	"status": "closed"
}

Response
{
  "message": "Gym successfully added to database",
  "success": true
}
```

#### PATCH '/gyms/<int:id>'
Updates a gym.
```
Body JSON example to include in patch request:
{
	"name":"DAV Schuppen",
	"address": "West-Straße 3",
	"city": 25,
	"website": "https://www.dav-schuppen.de/",
	"category": 1,
	"status": "closed"
}

Response:
{
  "message": "Gym successfully edited",
  "success": true
}
```

#### DELETE '/gyms/<int:id>'
Deletes a gym in the database.
```
{
  "message": "Gym successfully deleted",
  "success": true
}
```



