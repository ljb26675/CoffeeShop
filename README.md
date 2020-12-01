# CoffeeShop app

cd starter/backend

virtualenv env
source env/Scripts/activate

pip install -r requirements.txt

be inside src/ for backend
FLASK_APP=api.py FLASK_ENV=development python -m flask run

AttributeError: module 'time' has no attribute 'clock' In SQLAlchemy python 3.8.2

    I had this issue with SQLAlchemy 1.2.10. Upgrading to the current version (1.3.18 as of now) fixed the problem

    pip install sqlalchemy --upgrade

if getting can't find flask, run flask like python -m flask run


- in frontend
    npm install
- had to look up answer to probelm when running npm start
- had to make sure package.json looked like gabe's original:
https://github.com/udacity/FSND/blob/master/projects/03_coffee_shop_full_stack/starter_code/frontend/package.json
- then npm install again
- then npm start worked



https://lb-fullstack.us.auth0.com/authorize?audience=drink&response_type=token&client_id=xWmsdCdfrXsYMd2qwMtCpuyqlwu3CL0X&redirect_uri=http://127.0.0.1:8080/login-results

running frontend
cd to frontend
ionic serve (make sure ionic downloaded)

WORKING ON?
 - currently working on making sure the api calls actually work, like for adding a drink

# Coffee Shop
This project is the Coffee Shop project for the Udacity Fullstack nanodegree course. Using authentication,
only certain users should be able to perform certain actions on the coffee shop.

## Getting Started
### Pre-requisites and Local Development
Make sure you have have Python3, pip, node, and ionic installed on your local machines.

#### Backend
- From the backend folder, create your virtual env:
`python -m virtualenv env`
- Source that virtual env:
`source env/Scripts/activate` (Windows)
`source env/bin/activate` (Mac)
- Install the requirements:
`pip install -r requirements.txt`

You will need to import the postman included called starter_code\backend\udacity-fsnd-udaspicelatte.postman_collection.json

You can also comment and uncomment line 20 in starter_code\backend\src\api.py to clean out the database.


- To run the app:
```
export FLASK_APP=src/api.py
export FLASK_ENV=development
flask run
```

If you get this error: 

```
c:\users\linse\onedrive\desktop\fullstack\thirdproject\03_coffee_shop_full_stack\starter_code\backend\env\scripts\python.exe: No module named C:\Users\linse\OneDrive\Desktop\fullstack\ThirdProject\03_coffee_shop_full_stack\starter_code\backend\env\Scripts\flask
```
Instead of running `flask run` try `python -m flask run`. This was an error I encountered even though I have flask.


These commands put the application in development and directs our application to use the api.py file in our src folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the Flask documentation.

The application is run on http://localhost:5000/ by default and is a proxy in the frontend configuration.

### Frontend
From the frontend folder, run the following commands to download dependencies:

```
npm install // only once to install dependencies
```

In `./src/environments/environments.ts`, it contains my Auth0 configurations.

To run: 

```
ionic serve
```

By default, the frontend will run on http://localhost:8100/

## Tests
In order to run tests navigate to the backend folder and import this postman collection:
`starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`

You will need to right click on the manager and barista folders -> edit, to update their jwt to the one you get 
when you login to the app. They expire after some time.

## API Reference

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend
    app is hosted at the default, `http://localhost:5000/`, which is set as a proxy in the frontend config.
- Authentication: This application requires manager and barista permissions for some access, but allows 
normal users to view the drinks. The postman collection should contain valid JWTs for manager and barista.

## Error Handling
Errors are returned as JSON ojects in the following format:
```
{
    "success": False,
    "error": 401,
    "message": "unauthorized"
    
}
```
The api will return 4 error types when requests fail:
- 404: Resource Not Found
- 422: Not Processable
- 401: Unauthorized

## Endpoints Glossary
1. [GET /drinks](#get-drinks "Goto get-drinks")
2. [GET /drinks-detail](#get-drinksdetail "Goto get-drinksdetail")
3. [POST /drinks](#post-drinks "Goto post-drinks")
4. [PATCH /drinks/<id>](#patch-drinks_id "Goto patch-drinks_id")
5. [DELETE /drinks/<id>](#delete-drinks_id "Goto delete-drinks_id")

## Endpoints
### GET /drinks
- General:
    - returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
- Sample (from postman collection): 
    `http://localhost:5000/drinks`

    ```
    {
    "drinks": [
        {
            "id": 3,
            "recipe": [
                {
                    "color": "red",
                    "parts": 1
                }
            ],
            "title": "juice"
        }
      ]
    }
    ```

### GET /drinks-detail
- General:
    - Returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure.
    - Authorized users: managers and baristas
- Sample (from postman collection): `http://localhost:5000/drinks-detail`
    
    ```
    { "drinks": [ { "id": 3, "recipe": [ { "color": "red", "name": "red", "parts": 1 } ], "title": "juice" } ], "success": true }
    ```

### POST /drinks
- General:
    - Returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink or appropriate status code indicating reason for failure
    - Authorized users: managers 
- Sample (from postman collection): 
POST `http://localhost:5000/drinks` ...

```
{
    "drinks": {
        "id": 7,
        "recipe": [
            {
                "color": "yellow",
                "name": "lemons",
                "parts": 1
            }
        ],
        "title": "lemonade"
    },
    "success": true
}
```

### PATCH /drinks/<id>
- General:
    - Returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink or appropriate status code indicating reason for failure
    - Authorized users: managers 
- Sample (from postman collection):
PATCH `http://localhost:5000/drinks/7` ...
```
{
    "drinks": {
        "id": 7,
        "recipe": [
            {
                "color": "yellow",
                "name": "lemons",
                "parts": 1
            }
        ],
        "title": "lemonade v2.0"
    },
    "success": true
}
```

### DELETE /drinks/<id>
- General:
    - Returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
    or appropriate status code indicating reason for failure
    - Authorized users: managers 
- Sample (from postman collection):
DELETE `http://localhost:5000/drinks/7` ...

```
{
    "delete": 7,
    "success": true
}
```