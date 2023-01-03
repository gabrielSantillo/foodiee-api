from flask import request, make_response, send_from_directory
from apihelpers import check_endpoint_info, save_menu_file
import json
from dbhelpers import run_statement
import os

def get():
    is_valid = check_endpoint_info(request.args, ['file_name'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL get_menu_image(?)', [request.args.get('file_name')])

    if(type(results) != list):
        return make_response(json.dumps(results, default=str), 500)
    elif(len(results) == 0):
        return make_response(json.dumps("Wrong file name.", default=str), 400)

    return send_from_directory('menu_item_images', results[0]['file_name'])


def post():
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)

    is_valid = check_endpoint_info(request.form, ['menu_item_id', 'description'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    is_valid_file = check_endpoint_info(request.files, ['uploaded_file'])
    if(is_valid_file != None):
        return make_response(json.dumps(is_valid_file, default=str), 400)

    filename = save_menu_file(request.files['uploaded_file'])
    if(filename == None):
        return make_response(json.dumps("Sorry, an error has occurred", default=str), 500)

    results = run_statement('CALL add_menu_item_image(?,?,?,?)', [request.form.get('menu_item_id'), filename, request.form['description'], request.headers.get('token')])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results[0], default=str), 200)
    elif(type(results) == list and len(results) == 0):
        image_path = os.path.join('restaurant_menu_images', filename)
        os.remove(image_path)
        return make_response(json.dumps("Wrong token.", default=str), 400)
    elif(results.startswith("Duplicate entry")):
        image_path = os.path.join('restaurant_menu_images', filename)
        os.remove(image_path)
        return make_response(json.dumps(results, default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)

def pacth():
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)

    is_valid = check_endpoint_info(request.form, ['image_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    is_valid_file = check_endpoint_info(request.files, ['file_name'])
    if(is_valid_file != None):
        return make_response(json.dumps(is_valid_file, default=str), 400)

    image = run_statement('CALL get_menu_item_image_by_id(?)', [request.form.get('image_id')])

    if (type(image) != list):
        return make_response(json.dumps(image), 500)
    elif (len(image) == 0):
        return make_response(json.dumps("This image id is invalid.."), 400)

    filename = save_menu_file(request.files['file_name'])
    if (filename == None):
        return make_response(json.dumps("Sorry, something has gone wrong"), 500)

    results = run_statement('CALL edit_menu_item_image(?,?,?)', [filename, request.form.get('image_id'), 
    request.headers.get('token')])

    if(type(results) == list and results[0]['row_updated'] == 1):
        image_path = os.path.join('restaurant_menu_images', image[0]['file_name'])
        os.remove(image_path)

        return make_response(json.dumps(results[0], default=str), 200)
    elif(type(results) == list and results[0]['row_updated'] == 0):
        return make_response(json.dumps("Wrong image id or wrong token.", default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)