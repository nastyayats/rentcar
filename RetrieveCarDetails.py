import requests
import json
from hamcrest import *
import random
from jsonschema import validate

# Retreive token
def retrieveToken(scope):
    payload = {'client_id': 'f2a1ed52710d4533bde25be6da03b6e3', 'client_secret': 'ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q', 'scope':scope}
    r = requests.post('http://localhost:5000/v1/token', data=json.dumps(payload))
    print(r.text)
    return r.json().get('auth_token')


read_token = retrieveToken('R')
write_token = retrieveToken('W')

# # Add car to the list
def addCar():
    # old_list = retrieveCarsList()
    headers = {'Content-Type': 'application/json', 'auth_token': write_token}
    payload = {'brand': 'Toyota', 'model': 'Yaris', 'power_rating':400, 'daily_price':400}
    # payload = '{\"brand\":\"Aa\", \"model\":\"Bb\", \"power_rating\":1, \"daily_price\":1}'
    r = requests.post('http://localhost:5000/v1/cars', headers=headers, data=json.dumps(payload))
    print('Add car')
    print(r.text)
    # car_id = str(getCarId(old_list, retrieveCarsList()).pop())
    # print('Car with id {} is added'.format(car_id))
    # return car_id

# addCar()

def delete_car(write_token, car_id):
    headers = {'Content-Type': 'application/json', 'auth_token': write_token}
    response = requests.delete('http://localhost:5000/v1/cars/' + str(car_id), headers=headers)
    print('Delete car')
    print(response.text)
    return response

# delete_car(write_token, 3)


# Retrieve a list of cars
def retrieveCarsList(read_token):
    headers = {'Content-Type': 'application/json', 'auth_token': read_token}
    r = requests.get('http://localhost:5000/v1/cars', headers=headers)
    print(r.text)
    return r

# retrieveCarsList(read_token)

def create_car_data_model(brand, id, price, model, power):
    data = {'brand': brand, 'car_id': id, 'daily_price': price, 'model': model, 'power_rating': power}
    return data



# def verify_cars_list(r, number):
#     data = r.json().get('data')
#     assert_that(len(data), equal_to(number))
#     i = random.choice(range(0, number))
#
# verify_cars_list(retrieveCarsList(read_token), 3)


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
def retrieveCar(car_id):
    headers = {'Content-Type': 'application/json', 'auth_token': read_token}
    r = requests.get('http://localhost:5000/v1/cars/' + car_id, headers=headers)
    print('Get car')
    print(r.text)

# retrieveCar('3')

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

