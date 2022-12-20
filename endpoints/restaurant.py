from uuid import uuid4
from flask import request, make_response
from apihelpers import check_endpoint_info, check_data_sent
import secrets
import json
from dbhelpers import run_statement

def post():
    is_valid = check_endpoint_info(request.json, ['name', 'address', 'phone_number', 'email', 'password', 
    'bio', 'city'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    token = secrets.token_hex(nbytes=None)
    salt = uuid4().hex

    results = run_statement('CALL add_restaurant(?,?,?,?,?,?,?,?,?)', [request.json.get('name'),        
    request.json.get('address'), request.json.get('phone_number'), request.json.get('email'), 
    request.json.get('password'), salt, request.json.get('bio'), request.json.get('city'), token])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results[0], default=str), 200)
    elif(results.startswith('Duplicate entry')):
        return make_response(json.dumps(results, default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)


def get():
    is_valid = check_endpoint_info(request.args, ['restaurant_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL get_restaurant_by_id(?)', [request.args.get('restaurant_id')])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results[0], default=str), 200)
    elif(type(results) == list and len(results) == 0):
        return make_response(json.dumps("Wrong restaurant id.", default=str), 400)
    else:
        return make_response(json.dumps('Sorry, an error has occurred.', default=str), 500)