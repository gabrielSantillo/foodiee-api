from uuid import uuid4
from flask import request, make_response
from apihelpers import check_endpoint_info
import secrets
import json
from dbhelpers import run_statement

def post():
    is_valid = check_endpoint_info(request.json, ['email', 'first_name','last_name', 'username', 'password'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    token = secrets.token_hex(nbytes=None)
    salt = uuid4().hex

    results = run_statement('CALL add_client(?,?,?,?,?,?,?)', [request.json.get('email'), request.json.get('first_name'),               
    request.json.get('last_name'), request.json.get('username'), request.json.get('password'), salt, token])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results[0], default=str), 200)
    elif(results.startswith('Duplicate entry')):
        return make_response(json.dumps(results, default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occured.", default=str), 500)


def get():
    is_valid = check_endpoint_info(request.args, ['client_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL get_client(?)', [request.args.get('client_id')])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results[0], default=str), 200)
    elif (type(results) == list and len(results) == 0):
        return make_response(json.dumps("Sorry, this client doesn't exist.", default=str), 400)
    else:
        return make_response(json.dumps('Sorry, an error has occurred.', default=str), 500)