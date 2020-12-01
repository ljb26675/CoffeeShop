import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
import json

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
#db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks', methods=['GET'])
def get_drinks():

    drinks = [drink.short() for drink in Drink.query.all() if drink]

    """ if drinks is None:
            abort(404)
    else: """
    return jsonify({
        'success': True,
        'drinks': drinks
    })


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_details(payload):

    drinks = [drink.long() for drink in Drink.query.all() if drink]

    return jsonify({
        'success': True,
        'drinks': drinks
    })


'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(payload):

    """ body = request.get_json()

    req_title = body.get('title', None)
    req_recipe = body.get('recipe', None)

    drink = Drink(title=req_title, recipe=req_recipe) """ 

    body = request.get_json()
    req_title = body.get('title', None)
    req_recipe = body.get('recipe', None)

    drink = Drink(title=req_title, recipe=json.dumps(req_recipe))
    drink.insert()

    drinks = Drink.query.filter(Drink.title == req_title).one_or_none()
    drinks = drinks.long()

    #drink = body.get('drink', None)

    return jsonify({
        'success': True,
        'drinks': drinks
    })


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, drink_id):

    # get drink to update
    drinks = Drink.query.filter(Drink.id == drink_id).one_or_none()

    #update it
    body = request.get_json()
    req_title = body.get('title', None)
    req_recipe = body.get('recipe', None)

    if(req_title):
        drinks.title = req_title

    if(req_recipe):
        drinks.recipe = json.dumps(req_recipe)

    drinks.update()

    drinks = drinks.long()

    return jsonify({
        'success': True,
        'drinks': drinks
    })


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, drink_id):
    drinks = Drink.query.filter(Drink.id == drink_id).one_or_none()
    drinks.delete()

    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    return jsonify({
        'success': True,
        'drinks': drink
    })


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 

    UNCOMMENT THIS ONE WHEN YOU ARE GOOD WITH AUTHORIZATION -- IT MAKES IT HARD TO DEBUG
'''
""" @app.errorhandler(AuthError)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized"
    }), 401 """