from flask import request, make_response
from apihelpers import check_endpoint_info, organize_response, match_ids
import json
from dbhelpers import run_statement

def post():
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)

    is_valid = check_endpoint_info(request.json, ['menu_items', 'restaurant_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    # restaurant menu item ids = ids
    ids = run_statement('CALL get_menu_items_by_restaurant_id(?)', [request.json.get('restaurant_id')])

    items_id = request.json.get('menu_items')

    if(type(ids) == list and len(ids) != 0):
        if(match_ids(items_id, ids)):
            order_id = run_statement('CALL ')