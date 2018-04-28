import requests
import json

url = 'http://localhost:5000/v1/cars'


def prepare_car_data(brand, model, power, price):
    return json.dumps({'brand': brand, 'model': model, 'power_rating':power, 'daily_price':price})


def send_car_creation_request(write_token, payload):
    headers = {'Content-Type': 'application/json', 'auth_token': write_token}
    response = requests.post(url, headers=headers, data=payload)
    print('Response for car creation request is received with code {}'.format(response.status_code))
    print(response.text)
    return response


def get_id_of_created_car(old_list, new_list):
    old_ids = [x.get('car_id') for x in old_list]
    new_ids = [x.get('car_id') for x in new_list]
    return set(new_ids).difference(old_ids)


# could be moved to car_retrieval module
def get_last_car_id(data):
    # Function is used to retrieve car, that definitely exist in system and can be used in tests
    # todo: add exception for empty data
    return data[-1].get('car_id')