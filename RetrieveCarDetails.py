import requests
import json
import RetrieveToken
from hamcrest import *
import random
from jsonschema import validate

read_token = RetrieveToken.retrieveToken('R')
write_token = RetrieveToken.retrieveToken('W')

# Retrieve a list of cars
def retrieveCarsList(read_token):
    headers = {'Content-Type': 'application/json', 'auth_token': read_token}
    r = requests.get('http://localhost:5000/v1/cars', headers=headers)
    # print(r.text)
    return r

def create_car_data_model(brand, id, price, model, power):
    data = {'brand': brand, 'car_id': id, 'daily_price': price, 'model': model, 'power_rating': power}
    return data

def verify_car_data(car_data):
    data_expected = create_car_data_model('s', 1, 1, 's', 1)
    car_data['brand'] = 's'
    car_data['car_id'] = 1
    car_data['daily_price'] = 1
    car_data['model'] = 's'
    car_data['power_rating'] = 1
    assert_that(car_data, equal_to(data_expected))

def verify_car_data_json(car_data):
    schema = {
        'type': 'object',
        'properties': {
            'brand': {'type': 'string'},
            'model': {'type': 'string'},
            'car_id': {'type': 'number'},
            'daily_price': {'type': 'number'},
            'power_rating': {'type': 'number'},
        },
    }
    validate(car_data, schema)




#
# def verify_cars_list(r, number):
#     data = r.json().get('data')
#     assert_that(len(data), equal_to(number))
#     i = random.choice(range(0, number))
#     verify_car_data(data[i])
#
# verify_cars_list(retrieveCarsList(read_token), 3)
#
# def create_expected_cars_list_data(r, number):
#     data = r.json().get('data')
#     assert_that(len(data), equal_to(number))
#     data_expected = create_car_data_model('s', 1, 1, 's', 1)
#     i = random.choice(range(0, number))
#     data[i]['brand'] = 's'
#     data[i]['car_id'] = 1
#     data[i]['daily_price'] = 1
#     data[i]['model'] = 's'
#     data[i]['power_rating'] = 1
#     assert_that(data[i], equal_to(data_expected))
#
#
# create_expected_cars_list_data(retrieveCarsList(read_token), 3)


def verify_car_parameters(r, name, values):
    data = r.json().get('data')
    values_expected = list()
    values_received = list()
    for x in values.split(','):
        values_expected.append(x.strip())
    for x in range(0, len(data)):
        values_received.append(str(data[x].get(name)))
    values_expected.sort()
    values_received.sort()
    assert_that(values_expected, equal_to(values_received))

# verify_car_parameters(retrieveCarsList(read_token), 'brand', 'Ford, Ford, Volkswagen')


def create_expected_car_data(brand, id, price, model, power):
    data = {'brand': brand, 'car_id': id, 'daily_price': price, 'model': model, 'power_rating': power}
    payload = {'data': data, 'success': True}
    print(json.dumps(payload))



# create_expected_car_data('smth', 2, 300, 'other', 200)


def getCarId(old_list, new_list):
    old_ids = list()
    new_ids = list()
    for x in old_list:
        old_ids.append(x.get('car_id'))
    for x in new_list:
        new_ids.append(x.get('car_id'))
    return set(new_ids).difference(old_ids)
#
#
# # Retrieve car with car_id=1
# def retrieveCar(car_id):
#     headers = {'Content-Type': 'application/json', 'auth_token': read_token}
#     r = requests.get('http://localhost:5000/v1/cars/' + car_id, headers=headers)
#     # print(r.text)
# # retrieveCar('1')
#
# # Add car to the list
def addCar():
    # old_list = retrieveCarsList()
    headers = {'Content-Type': 'application/json', 'auth_token': write_token}
    payload = {'brand': 'Toyota', 'model': 'Yaris', 'power_rating':400, 'daily_price':400}
    r = requests.post('http://localhost:5000/v1/cars', headers=headers, data=json.dumps(payload))
    print(r.text)
    # car_id = str(getCarId(old_list, retrieveCarsList()).pop())
    # print('Car with id {} is added'.format(car_id))
    # return car_id


newCar = addCar()
#
# # Remove a car from the list
# def removeCar(car_id):
#     headers = {'Content-Type': 'application/json', 'auth_token': write_token}
#     r = requests.delete('http://localhost:5000/v1/cars/' + car_id, headers=headers)
#     print(r.text)
#
# # removeCar('5')
#
#
# #bug - response 200 if car with id is not found, but response body is
#
# # {
# #   "errorMessage": "application crashed",
# #   "success": false
# # }
#
# #bug - impossible to add more then some number of cars - to investigate
#
# #bug - inconsistency in spec - hourrate vs daily_price
#
# bug - price = 0:
# "errorMessage": "INTERNAL SERVER ERROR",
# "success": false
#
#     read_token = RetrieveToken.retrieveToken('R')
#     write_token = RetrieveToken.retrieveToken('W')
#
#
#
#
#
# @then('response contains car {parameter} {values}')
# def step_impl(context, parameter, values):
#     verify_car_parameters(context.response, parameter, values)

def verify_car_parameters(r, parameter, values):
    data = r.json().get('data')
    values_expected = list()
    values_received = list()
    for x in values.split(','):
        values_expected.append(x.strip())
    for x in range(0, len(data)):
        values_received.append(str(data[x].get(parameter)))
    values_expected.sort()
    values_received.sort()
    assert_that(values_expected, equal_to(values_received))

