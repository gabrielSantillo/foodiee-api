from flask import request, make_response, send_from_directory
from apihelpers import check_endpoint_info, save_file
import json
from dbhelpers import run_statement
import os

def post():
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)

    is_valid = check_endpoint_info(request.form, ['restaurant_id', 'description'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    is_valid_file = check_endpoint_info(request.files, ['uploaded_file'])
    if(is_valid_file != None):
        return make_response(json.dumps(is_valid_file, default=str), 400)

    filename = save_file(request.files['uploaded_file'])
    if(filename == None):
        return make_response(json.dumps("Sorry, an error has occurred", default=str), 500)

    results = run_statement('CALL add_restaurant_image(?,?,?)', [request.form['restaurant_id'], filename, 
                request.form['description']])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results[0], default=str), 200)
    elif(type(results) == list and len(results) == 0):
        return make_response(json.dumps(results, default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)