from behave import *
from getcarslist import get_cars_list
from addcar import create_car, add_car, get_new_car_id
import validatejson


@when('create car with brand {brand}, model {model}, power rating {power:d} and daily price {price:d}')
def step_impl(context, brand, model, power, price):
    context.payload = create_car(brand, model, power, price)


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
    validatejson.add_car_response_success(context.response.json())
