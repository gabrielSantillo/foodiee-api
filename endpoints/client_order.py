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
            order_id = run_statement('CALL add_order(?,?)', [request.headers.get('token'), request.json.get('restaurant_id')])
            if(type(order_id) == list and order_id[0]['order_id'] == 0):
                return make_response(json.dumps("Wrong token.", default=str), 400)
        else:
            return make_response(json.dumps("At least one of these menu items id doesn't belong to the restaurant.", default=str), 400)
    else:
        return make_response(json.dumps("Wrong restaurant id", default=str), 400)

    
    for id in items_id:
        items_added = run_statement('CALL add_item_to_order(?,?)', [order_id[0]['order_id'], id])


        # if item_added at 'row_updated" is 1, return a success response
    if(type(items_added) == list and items_added[0]['row_updated'] == 1):
        return make_response(json.dumps(order_id[0], default=str), 200)
    # otherwise, return a db failure response
    else:
        return make_response(json.dumps("Sorry, an error has occurred."), 500)