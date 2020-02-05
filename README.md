# Flask Rest API

Simple Flask REST API that connects to a simulated Library database. Allows users to place requests on books in the Library with the intent of being emailed at the point in time which they become available. 

Notes:  
A Book table is seeded with the following titles at runtime for some validation purposes.  

['Dune', 'Blindsight', 'Anathem', 'Cryptonomicon', 'Foundation']  

The current database is meant to be switched to PostGres in a docker container. As a result, tests are currently run against the same database that the endpoints are targetting and you may experience some issues. 


## Requirements
Docker

You will need to create a .env file at the root directory of this project. Example: 

.env

```
FLASK_DEBUG=True  
SQLALCHEMY_DATABASE_URI=sqlite:///../tmp/test.sqlite  
SQLALCHEMY_TRACK_MODIFICATIONS=False  
```

#### Build
```
docker build -t flask-rest-api .
```

#### Run
```
docker run -d --rm --env-file=.env --name flask-container -p 5000:5000 flask-rest-api
```

#### Test
```
docker exec -it flask-container py.test
```


## Endpoints

URL:  
### /request  

Method:  
### [GET]

Returns all Requests

Status code: 200
Success Response:
```
{
  "data": [
    {
      "email": "email@gmail.com",
      "id": 1,
      "timestamp": "2020-02-05T22:29:35",
      "title": "Foundation"
    },
    {
      "email": "email@gmail.com",
      "id": 2,
      "timestamp": "2020-02-05T22:30:05",
      "title": "Foundation"
    },
    {
      "email": "email@gmail.com",
      "id": 3,
      "timestamp": "2020-02-05T22:57:25",
      "title": "Dune"
    }
  ],
  "status": "success"
}
```

### [POST]

Adds a new Request to the database. Returns the request object with an id and timestamp.

Params:
- email {string} the email address of the requesting user. Email must be a valid email format.
- title {string} the title of the requested book. Title must exist in the Book table. 

Example request body:
```
{
	"title": "Dune",
	"email": "email@gmail.com"
}
```

Status code: 200  
Success Response:
```
{
  "data": {
    "email": "email@gmail.com",
    "id": 5,
    "timestamp": "2020-02-05T23:04:35",
    "title": "Dune"
  },
  "status": "success"
}
```
Example failure response for invalid email format  
Status code: 400
```
{
  "data": {
    "email": "Email provided is not in a valid format."
  },
  "status": "fail"
}
```
Example failure response for invalid title  
Status code: 404
```
{
  "data": {
    "title": "Book Dune2 not found in Library"
  },
  "status": "fail"
}
```
---

URL:  
### /request/:id

Method:  
### [GET]

Returns a single request by id

Params:  
id {url path param}: id of the request to query

Sample request to /request/3

Success response  
Status code: 200

```
{
  "data": {
    "email": "email@gmail.com",
    "id": 3,
    "timestamp": "2020-02-05T22:30:05",
    "title": "Foundation"
  },
  "status": "success"
}
```
Example failure response  
Status code: 404
```
{
  "message": "Title with ID: 35 not found",
  "status": "error"
}
```


Method:  
### [DELETE]

Params:  
id {url path param}: id of the request to delete

Success response  
Status code: 200

```
{
  "data": "",
  "status": "success"
}
```