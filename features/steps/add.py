from behave import *
from getcarslist import get_cars_list
from addcar import create_car, add_car, get_new_car_id
import validatejson
from hamcrest import assert_that


@given('create car with brand {brand}, model {model}, power rating {power:d} and daily price {price:d}')
def step_impl(context, brand, model, power, price):
    context.payload = create_car(brand, model, power, price)


@given('create car with payload {payload}')
def step_impl(context, payload):
    context.payload = payload
    print('Payload: {}'.format(payload))


@when('send request to add car')
def step_impl(context):
    context.response = add_car(context.write_token, context.payload)


@when('send requests to add {number:d} cars and verify cars added')
def step_impl(context, number):
    old_list = get_cars_list(context.read_token).json().get('data')
    for x in range(0, number):
        add_car(context.write_token, context.payload)
    new_list = get_cars_list(context.read_token).json().get('data')
    assert_that(len(new_list) == len(old_list) + number)


@when('send request to add car and retrieve its car_id')
def step_impl(context):
    old_list = get_cars_list(context.read_token).json().get('data')
    context.response = add_car(context.write_token, context.payload)
    new_list = get_cars_list(context.read_token).json().get('data')
    assert_that(len(new_list) == len(old_list) + 1)
    context.car_id = str(get_new_car_id(old_list, new_list).pop())


@then('add car response is valid')
def step_impl(context):
    validatejson.add_car_response_success(context.response.json())
