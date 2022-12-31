from uuid import uuid4
from flask import request, make_response
from apihelpers import check_endpoint_info, check_data_sent
import secrets
import json
from dbhelpers import run_statement

def post():
    is_valid = check_endpoint_info(request.json, ['email', 'first_name','last_name', 'password'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    token = secrets.token_hex(nbytes=None)
    salt = uuid4().hex

    results = run_statement('CALL add_client(?,?,?,?,?,?)', [request.json.get('email'), request.json.get('first_name'),               
    request.json.get('last_name'), request.json.get('password'), salt, token])

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

def patch():
    is_valid = check_endpoint_info(request.headers, ['token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 500)

    client_info = run_statement('CALL get_client_by_token(?)', [request.headers.get('token')])
    if(type(client_info) != list or len(client_info) != 1):
        return make_response(json.dumps(client_info, default=str), 400)
    
    # update_client_info = uci
    uci = check_data_sent(request.json, client_info[0], ['first_name', 'last_name', 'email', 
    'password', 'username'])

    if(request.json.get('password') != None):
        salt = uuid4().hex
        results = run_statement('CALL edit_client_with_password(?,?,?,?,?,?,?)',[ uci['first_name'], 
        uci['last_name'], uci['email'], uci['password'], salt, uci['username'], 
        request.headers.get('token')])
    else:
        results = run_statement('CALL edit_client(?,?,?,?,?,?)', [uci['first_name'], 
        uci['last_name'], uci['email'], uci['password'], uci['username'], 
        request.headers.get('token')])

    if(type(results) == list and results[0]['row_updated'] == 1):
        return make_response(json.dumps(results[0], default=str), 200)
    elif(type(results) == list and results[0]['row_updated'] == 0):
        return make_response(json.dumps(results[0],default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)


def delete():
    is_valid = check_endpoint_info(request.json, ['password'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    is_valid_token = check_endpoint_info(request.headers, ['token'])
    if(is_valid_token != None):
        return make_response(json.dumps(is_valid_token, default=str), 400)

    results = run_statement('CALL delete_client(?,?)', [request.json.get('password'), 
    request.headers.get('token')])

    if(type(results) == list and results[0]['row_updated'] == 1):
        return make_response(json.dumps(results[0], default=str), 200)
    elif(type(results) == list and results[0]['row_updated'] == 0):
        return make_response(json.dumps(results[0], default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occured.", default=str), 500)