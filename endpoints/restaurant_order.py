from flask import request, make_response
from apihelpers import check_endpoint_info, organize_restaurant_response
import json
from dbhelpers import run_statement

# get request for the endpoint restaurant-order
def get():
    # verify if the data expected to be sent was sent indeed
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)

    # calling a procedure that get all orders related to a restaurant
    results = run_statement('CALL get_all_restaurant_orders(?)', [request.headers.get('token')])

    # if results is a list and the length of results is different than zero, return a success response
    if(type(results) == list and len(results) != 0):
        better_response = organize_restaurant_response(results)
        return make_response(json.dumps(better_response, default=str), 200)
    # if results is a list and the length of results is different equalts to zero, return a failure response
    elif(type(results) == list and len(results) == 0):
        return make_response(json.dumps(results, default=str), 400)
    # otherwise, return a db failure response
    else:
        return make_response(json.dumps("Sorry an error has occurred"), 500)



# patch request for the endpoint restaurant-order
def patch():
    # verify if the data expected to be sent was sent indeed
    is_valid_header = check_endpoint_info(request.headers, ['token'])
    if(is_valid_header != None):
        return make_response(json.dumps(is_valid_header, default=str), 400)
    # verify if the data expected to be sent was sent indeed
    is_valid = check_endpoint_info(request.json, ['order_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    # grabbing the value of is_confirmed and is_complete if they were sent
    confirm_order = request.json.get('is_confirmed')
    complete_order = request.json.get('is_complete')
    # if confirm_order is different than zero and complete_order is equals to zero call a procedure that will confirm an order
    if(confirm_order != None and complete_order == None):
        results =  run_statement('CALL confirm_order(?,?,?)', [request.headers.get('token'), request.json.get('order_id'), request.json.get('is_confirmed')])
    # if confirm_order is equals to zero and complete_order is different than zero call a procedure that will complete an order
    elif(confirm_order == None and complete_order != None):
        results = run_statement('CALL complete_order(?,?,?)', [request.headers.get('token'), request.json.get('order_id') ,request.json.get('is_complete')])
    # if none of the variables was sent, send a message to the user to let them know it
    elif(confirm_order == None and complete_order == None):
        return make_response(json.dumps("No data sent, either to confirm or to complete an order."), 400)
    # if both of the variables was sent, let the user know that he needs to first confirm an order to then complete it
    elif(confirm_order != None and complete_order != None):
        return make_response(json.dumps("You should first confirm an order, then complete it."), 400)

    # if results is a list return a success message
    if(type(results) == list):
        return make_response(json.dumps(results[0], default=str), 200)
    # if the message send back from the db starts with "Incorrect integer value" le tthe user know that the data must be sent either true or false
    elif(results.startswith("Incorrect integer value:")):
        return make_response(json.dumps("Send true or false to confirm or complete your order."), 400)
    # otherwise, return a db failure response
    else:
        return make_response(json.dumps("Sorry, an error has occurred"), 500)