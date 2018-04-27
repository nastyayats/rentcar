from behave import *
from hamcrest import *
import validatejson
from getcarslist import get_cars_list, verify_car_ids_unique
from getcar import get_car, verify_car_parameters
from addcar import get_last_car_id


@given('car with car_id exists in app')
def step_impl(context):
    response = get_cars_list(context.read_token)
    context.car_id= get_last_car_id(response.json().get('data'))


@given('car with car_id is absent in app')
def step_impl(context):
    response = get_cars_list(context.read_token)
    context.car_id = get_last_car_id(response.json().get('data')) + 1


@when('send request to get car with car_id {car_id}')
def step_impl(context, car_id):
    context.response = get_car(car_id, context.read_token)
    context.car_id = car_id


@when('send request to get car with car_id')
def step_impl(context):
    context.response = get_car(context.car_id, context.read_token)


@when('send request to get cars list')
def step_impl(context):
    context.response = get_cars_list(context.read_token)


@then('get car response is valid')
def step_impl(context):
    validatejson.get_car_response_success(context.response.json())


@then('response contains car {brand}, {model} with power rating {power:d} and daily price {price:d}')
def step_impl(context, brand, model, power, price):
    data = context.response.json().get('data')
    verify_car_parameters(data, brand, model, power, price)


@then('get cars list response is valid and contains {number} cars with unique ids')
def step_impl(context, number):
    validatejson.get_cars_list_response_success(context.response.json())
    data = context.response.json().get('data')
    if number != 'N':
        assert_that(len(data), equal_to(int(number)))
    verify_car_ids_unique(data)

