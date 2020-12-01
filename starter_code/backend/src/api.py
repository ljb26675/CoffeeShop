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
uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
#db_drop_and_create_all()

# ROUTES
'''
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['GET'])
def get_drinks():

    drinks = [drink.short() for drink in Drink.query.all() if drink]

    if drinks is None:
        abort(404)


    return jsonify({
        'success': True,
        'drinks': drinks
    })


'''
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

    if drinks is None:
        abort(404)

    return jsonify({
        'success': True,
        'drinks': drinks
    })


'''
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
    try:
        body = request.get_json()
        req_title = body.get('title', None)
        req_recipe = body.get('recipe', None)

        drink = Drink(title=req_title, recipe=json.dumps(req_recipe))
        drink.insert()

        drinks = Drink.query.filter(Drink.title == req_title).one_or_none()
        drinks = drinks.long()

        return jsonify({
            'success': True,
            'drinks': drinks
        })
    except:
        abort(422)

'''
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
    try: 
        # get drink to update
        drinks = Drink.query.filter(Drink.id == drink_id).one_or_none()

        # error check if none with that id exist
        if drinks is None:
            abort(404)

        #update it
        body = request.get_json()
        req_title = body.get('title', None)
        req_recipe = body.get('recipe', None)

        if req_title:
            drinks.title = req_title

        if req_recipe:
            drinks.recipe = json.dumps(req_recipe)

        drinks.update()

        drinks = drinks.long()

        return jsonify({
            'success': True,
            'drinks': drinks
        })
    except:
        abort(422) #error out if encounter exceptin


'''
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
    # grab the one we want to delete
    drinks = Drink.query.filter(Drink.id == drink_id).one_or_none()

    # error check if none with that id exist
    if drinks is None:
        abort(404)

    # delete and commit
    drinks.delete()

    # check to make sure its gone
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()
    # check if null here
    if drink:
        abort(404)

    return jsonify({
        'success': True,
        'delete': drink_id
    })


# Error Handling
'''
Error handler for unprocessable
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
Error Handler for 404
'''
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


'''
Error Handler for AuthError
'''
""" @app.errorhandler(AuthError)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized"
    }), 401 """