from flask import request, make_response
from apihelpers import check_endpoint_info
import json
from dbhelpers import run_statement

# get request for the endpoint restaurant-order
def get():
    # verify if the data expected to be sent was sent indeed
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)

    # calling a procedure that get all orders related to a restaurant
    results = run_statement('CALL get_all_restaurant_order(?)', [request.headers.get('token')])

    # if results is a list and the length of results is different than zero, return a success response
    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results, default=str), 200)
    # if results is a list and the length of results is different equalts to zero, return a failure response
    elif(type(results) == list and len(results) == 0):
        return make_response(json.dumps(results, default=str), 400)
    # otherwise, return a db failure response
    else:
        return make_response(json.dumps("Sorry an error has occurred"), 500)