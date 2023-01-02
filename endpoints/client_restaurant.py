from uuid import uuid4
from flask import request, make_response
from apihelpers import check_endpoint_info, check_data_sent
import secrets
import json
from dbhelpers import run_statement

####################
# THIS IS THE FILE THAT THE I MAKE THE GET REQUEST TO GET ALL RESTAURANTS IN THE DB


def get():

    results = run_statement('CALL get_all_restaurants()')

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('Sorry, an error has occurred.', default=str), 500)