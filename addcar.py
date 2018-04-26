import requests
import json


def create_car(brand, model, power, price):
    return {'brand': brand, 'model': model, 'power_rating':power, 'daily_price':price}


def add_car(write_token, payload):
    headers = {'Content-Type': 'application/json', 'auth_token': write_token}
    response = requests.post('http://localhost:5000/v1/cars', headers=headers, data=json.dumps(payload))
    print('Add car')
    print(response)
    return response


def get_new_car_id(old_list, new_list):
    old_ids = list()
    new_ids = list()
    for x in old_list:
        old_ids.append(x.get('car_id'))
    for x in new_list:
        new_ids.append(x.get('car_id'))
    return set(new_ids).difference(old_ids)


def get_last_car_id(data):
    return data[-1].get('car_id')