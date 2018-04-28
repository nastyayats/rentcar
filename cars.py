import requests
import json
from hamcrest import assert_that, equal_to


url = 'http://localhost:5000/v1/cars'


def set_request_headers(token):
    return {'Content-Type': 'application/json', 'auth_token': token}


def prepare_car_data(brand, model, power, price):
    return json.dumps({'brand': brand, 'model': model, 'power_rating':power, 'daily_price':price})


def send_car_creation_request(w_token, payload):
    response = requests.post(url, headers=set_request_headers(w_token), data=payload)
    print('Response for car creation request is received with code {}'.format(response.status_code))
    print(response.text)
    return response


def get_id_of_created_car(old_list, new_list):
    old_ids = [x.get('car_id') for x in old_list]
    new_ids = [x.get('car_id') for x in new_list]
    return set(new_ids).difference(old_ids)


def send_car_retrieval_request(car_id, r_token):
    response = requests.get(url + '/' + car_id, headers=set_request_headers(r_token))
    print('Response to car retrieval request for car with id {} is received with code {}'.format(car_id, response.status_code))
    print(response.text)
    return response


def verify_car_data(data, brand, model, power, price):
    assert_that(data.get('brand'), equal_to(brand))
    assert_that(data.get('model'), equal_to(model))
    assert_that(data.get('power_rating'), equal_to(power))
    assert_that(data.get('daily_price'), equal_to(price))


def send_cars_list_retrieval_request(r_token):
    response = requests.get(url, headers=set_request_headers(r_token))
    print('Response to cars list retrieval requestis received with code {}'.format(response.status_code))
    print(response.text)
    return response


def get_car_ids(data):
    return [x.get('car_id') for x in data]


def get_last_car_id(data):
    # Function is used to retrieve car, that definitely exist in system and can be used in tests
    # todo: add exception for empty data
    return data[-1].get('car_id')


def verify_car_ids_uniqueness(data):
    ids = get_car_ids(data)
    assert_that(len(ids) == len(set(ids)))


def send_car_removal_request(w_token, car_id):
    response = requests.delete(url + '/' + car_id, headers=set_request_headers(w_token))
    print('Response to car removal request for car with id {} is received with code {}'.format(car_id, response.status_code))
    print(response.text)
    return response



def verify_car_removal(car_id, r_token):
    # Verify that removed car can't be retrieved by car_id:
    response = send_car_retrieval_request(str(car_id), r_token)
    assert_that(response.status_code, equal_to(404))
    # Verify that removed car is absent in cars list:
    response = send_cars_list_retrieval_request(r_token)
    ids_list = [x.get('car_id') for x in response.json().get('data')]
    assert_that(car_id not in ids_list)



