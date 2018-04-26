from behave import *
import requests
import json
from hamcrest import *
from validatejson import validate_get_car_response_success_json, validate_get_cars_list_response_success, \
    validate_add_car_response_success_json, validate_delet_car_success_json

def get_token(scope):
    payload = {'client_id': 'f2a1ed52710d4533bde25be6da03b6e3', 'client_secret': 'ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q', 'scope':scope}
    r = requests.post('http://localhost:5000/v1/token', data=json.dumps(payload))
    return r.json().get('auth_token')


def get_cars_list(read_token):
    headers = {'Content-Type': 'application/json', 'auth_token': read_token}
    response = requests.get('http://localhost:5000/v1/cars', headers=headers)
    print(response.text)
    return response



def verify_car_parameters(data, brand, model, power, price):
    assert_that(data.get('brand'), equal_to(brand))
    assert_that(data.get('model'), equal_to(model))
    assert_that(data.get('power_rating'), equal_to(power))
    assert_that(data.get('daily_price'), equal_to(price))


def create_car(brand, model, power, price):
    return {'brand': brand, 'model': model, 'power_rating':power, 'daily_price':price}


def get_car(car_id, read_token):
    headers = {'Content-Type': 'application/json', 'auth_token': read_token}
    response = requests.get('http://localhost:5000/v1/cars/' + car_id, headers=headers)
    print(response.text)
    return response

def add_car(write_token, payload):
    headers = {'Content-Type': 'application/json', 'auth_token': write_token}
    response = requests.post('http://localhost:5000/v1/cars', headers=headers, data=json.dumps(payload))
    print(response.text)
    return response


def delete_car(write_token, car_id):
    headers = {'Content-Type': 'application/json', 'auth_token': write_token}
    response = requests.delete('http://localhost:5000/v1/cars/' + car_id, headers=headers)
    print(response.text)
    return response


def car_id_is_absent_in_app(car_id, read_token):
    response = get_car(str(car_id), read_token)
    assert_that(response.status_code, equal_to(404))
    response = get_cars_list(read_token)
    ids_list = list()
    for x in response.json().get('data'):
        ids_list.append(x.get('car_id'))
    assert_that(car_id not in ids_list)


def get_new_car_id(old_list, new_list):
    old_ids = list()
    new_ids = list()
    for x in old_list:
        old_ids.append(x.get('car_id'))
    for x in new_list:
        new_ids.append(x.get('car_id'))
    return set(new_ids).difference(old_ids)


def verify_car_ids_unique(data):
    ids = list()
    for x in data:
        ids.append(x.get('car_id'))
    assert_that(len(ids) == len(set(ids)))

def get_last_car_id(data):
    return data[-1].get('car_id')

@given('app contains default cars list')
def step_impl(context):
    pass #add app restart here


@when('send request to get cars list')
def step_impl(context):
    context.response = get_cars_list(context.read_token)


@then('receive response with code {code:d}')
def step_impl(context, code):
   assert_that(context.response.status_code, equal_to(code))


@then('get cars list response is valid and contains {number} cars with unique ids')
def step_impl(context, number):
    validate_get_cars_list_response_success(context.response.json())
    data = context.response.json().get('data')
    if number != 'N':
        assert_that(len(data), equal_to(int(number)))
    verify_car_ids_unique(data)


@then('get car response is valid')
def step_impl(context):
    validate_get_car_response_success_json(context.response.json())


@then('response contains car {brand}, {model} with power rating {power:d} and daily price {price:d}')
def step_impl(context, brand, model, power, price):
    data = context.response.json().get('data')
    verify_car_parameters(data, brand, model, power, price)


@when('send request to get car with car_id {car_id}')
def step_impl(context, car_id):
    context.response = get_car(car_id, context.read_token)


@given('create car with brand {brand}, model {model}, power rating {power:d} and daily price {price:d}')
def step_impl(context, brand, model, power, price):
    context.payload = create_car(brand, model, power, price)
    context.read_token = get_token('R')
    context.write_token = get_token('W')


@when('send request to add car')
def step_impl(context):
    context.response = add_car(context.write_token, context.payload)


@when('send request to add car and retrieve its car_id')
def step_impl(context):
    old_list = get_cars_list(context.read_token).json().get('data')
    add_car(context.write_token, context.payload)
    new_list = get_cars_list(context.read_token).json().get('data')
    context.car_id = str(get_new_car_id(old_list, new_list).pop())

@then('add car response is valid')
def step_impl(context):
    validate_add_car_response_success_json(context.response.json())
    

@given('tokens retrieved')
def step_impl(context):
    context.read_token = get_token('R')
    context.write_token = get_token('W')


@then('response contains error message: {error_message}')
def step_impl(context, error_message):
    if 'car_id' in error_message:
        error_message.replace('car_id', context.car_id)
    assert_that(context.response.json().get('errorMessage'), equal_to(error_message))


@when('send request to delete car with car_id')
def step_impl(context):
    context.response = delete_car(context.write_token, str(context.car_id))


@then('delete car response is valid')
def step_impl(context):
    validate_delet_car_success_json(context.response.json())


@given('car with car_id exists in app')
def step_impl(context):
    response = get_cars_list(context.read_token)
    context.car_id= get_last_car_id(response.json().get('data'))


@then('car with car_id is absent in app')
def step_impl(context):
    car_id_is_absent_in_app(context.car_id, context.read_token)


@given('car_id is absent in app')
def step_impl(context):
    response = get_cars_list(context.read_token)
    context.car_id = get_last_car_id(response.json().get('data')) + 1





