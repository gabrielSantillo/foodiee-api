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
    elif(results.startswith("Duplicate entry")):
        image_path = os.path.join('restaurant_images', filename)
        os.remove(image_path)
        return make_response(json.dumps(results, default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)


def get():
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)

    is_valid = check_endpoint_info(request.args, ['file_name'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL get_restaurant_images(?,?)', [request.args.get('file_name'),          
    request.headers.get('token')])

    if(type(results) != list):
        return make_response(json.dumps(results, default=str), 500)
    elif(len(results) == 0):
        return make_response(json.dumps("Wrong file name or wrong token.", default=str), 400)

    return send_from_directory('restaurant_images', results[0]['file_name'])


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

    image = run_statement('CALL get_restaurant_image_by_id(?,?)', [request.form.get('image_id'), 
    request.headers.get('token')])

    # Make sure something came back from the DB that wasn't an error
    if (type(image) != list):
        return make_response(json.dumps(image), 500)
    elif (len(image) == 0):
            return make_response(json.dumps("This image id is invalid.."), 400)


    filename = save_file(request.files['file_name'])
    if (filename == None):
        return make_response(json.dumps("Sorry, something has gone wrong"), 500)

    results = run_statement('CALL edit_restaurant_image(?,?,?)', [filename, 
    request.form.get('image_id'), request.headers.get('token')])

    if(type(results) == list and results[0]['row_updated'] == 1):
        image_path = os.path.join('restaurant_images', image[0]['file_name'])
        os.remove(image_path)

        return make_response(json.dumps(results[0], default=str), 200)
    elif(type(results) == list and results[0]['row_updated'] == 0):
        return make_response(json.dumps("Wrong image id or wrong token.", default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)