from uuid import uuid4
from flask import request, make_response
from apihelpers import check_endpoint_info, check_data_sent
import secrets
import json
from dbhelpers import run_statement

def post():
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)

    is_valid = check_endpoint_info(request.json, ['name', 'description', 'price'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL add_menu_item(?,?,?,?)', [request.json.get('name'), 
    request.json.get('description'), request.json.get('price'), 
    request.headers.get('token')])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)


def get():
    is_valid = check_endpoint_info(request.args, ['restaurant_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL get_menu_items_by_restaurant_id(?)', 
    [request.args.get('restaurant_id')])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results, default=str), 200)
    elif(type(results) == list and len(results) == 0):
        return make_response(json.dumps("Wrong restaurant id.", default=str), 
        400)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)


def patch():
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)

    is_valid = check_endpoint_info(request.json, ['menu_item_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    # menu item info = mi
    mi = run_statement('CALL get_menu_item_by_id(?,?)', [request.json.get('menu_item_id'), 
    request.headers.get('token')])

    # update menu item = umi
    umi = check_data_sent(request.json, mi[0], ['name', 'description', 'price'])

    results = run_statement('CALL edit_menu_item(?,?,?,?,?)', [request.json.get('menu_item_id'), 
    umi['name'], umi['description'], umi['price'], request.headers.get('token')])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results[0], default=str), 200)
    elif(type(results) == list and len(results) == 0):
        return make_response(json.dumps("Wrong token and/or menu item id.", default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)
    

def delete():
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)
    
    is_valid = check_endpoint_info(request.json, ['menu_item_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL delete_menu_item(?,?)', [request.json.get('menu_item_id'), request.headers.get('token')])

    if(type(results) == list and results[0]['row_updated'] == 1):
        return make_response(json.dumps(results[0], default=str), 200)
    elif(type(results) == list and results[0]['row_updated'] == 0):
        return make_response(json.dumps("Wrong token and/or menu item id.", default=str), 400)
    else:
        return make_response(json.dumps("Sorry, an error has occurred.", default=str), 500)