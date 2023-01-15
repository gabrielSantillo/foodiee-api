from flask import request, make_response
from apihelpers import check_endpoint_info
import secrets
import json
from dbhelpers import run_statement

def get():
    is_valid = check_endpoint_info(request.headers, ['token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL get_client_token(?)', [request.headers.get('token')])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results[0], default=str), 200)
    elif (type(results) == list and len(results) == 0):
        return make_response(json.dumps("Sorry, this token doesn't exist or isn't validated.", default=str), 400)
    else:
        return make_response(json.dumps('Sorry, an error has occurred.', default=str), 500)