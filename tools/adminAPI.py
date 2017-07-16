import json
import requests
from test_common import *
from datetime import timedelta

def get_surprises():
    '''!!!WORKS FOR DEV-only
    !!! ASK FOR BETTER ARCHITECTURE'''
    response = requests.get('http://52.53.195.1:8080/v1.0/surprises', auth=('user', 'pass'))
    return response.text

def add_surprises(period=1, number_surprises=1):
    '''
    Add exact number of surprises with exact period
    !!! NEED TO FINISHED
    '''
    surprises_list = get_surprises()
    for i in range(number_surprises):
        surprises_list = surprises_list.append({"number: 77", "date : 20170808"})
    return surprises_list


def get_featured():
    '''CHECK if a class neeeded
    ADD servers'''
    featured_list = []
    get_pure_ids('featured')
    return featured_list

def send_featrued():
    '''CREATE appropriate FEATURED effects sample'''
    pass

def get_env_variables():
    '''CHECK if a class neeeded
    ADD servers'''
    response = requests.get('http://52.53.195.1:8080/v1.0/properties', auth=('user', 'pass'))
    env_variables = json.loads(response.text)
    return env_variables

def get_pure_ids(request):
    response_list = []
    response = requests.get('http://52.53.195.1:8080/v1.0/'+request, auth=('user', 'pass'))
    raw_list = response.text.split('"')
    for element in raw_list:
        if (len(element) == 64):
            response_list.append(element)
    return response_list

def get_next_surprise(dt):
    '''
    ReWrite method to deal if nextsuprise isn't stated by env_var
    '''
    env_vars = get_env_variables()
    next_surpise = dt + timedelta(days=int(env_vars['AUTO_NEXT_SURPRISE_INTERVAL']), seconds=1)
    return (next_surpise)


if __name__ == '__main__':
    # response = get_surprises()
    # print(response)
    # response = get_featured()
    # print(response)
    response = get_env_variables()
    print(response)
    response = get_next_surprise(dt)
    print(response)