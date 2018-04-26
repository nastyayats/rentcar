from behave import *
from hamcrest import *
import validatejson
from gettoken import get_token
from getcarslist import get_cars_list, verify_car_ids_unique
from getcar import get_car, verify_car_parameters
from addcar import create_car, add_car, get_new_car_id, get_last_car_id
from deletecar import delete_car, car_id_is_absent_in_app


@given('tokens retrieved')
def step_impl(context):
    context.read_token = get_token('R')
    context.write_token = get_token('W')


@given('car with car_id exists in app')
def step_impl(context):
    response = get_cars_list(context.read_token)
    context.car_id= get_last_car_id(response.json().get('data'))


@given('car with car_id is absent in app')
def step_impl(context):
    response = get_cars_list(context.read_token)
    context.car_id = get_last_car_id(response.json().get('data')) + 1


@given('app contains default cars list')
def step_impl(context):
    pass #add app restart here


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


@when('send request to get car with car_id {car_id}')
def step_impl(context, car_id):
    context.response = get_car(car_id, context.read_token)


@when('send request to get cars list')
def step_impl(context):
    context.response = get_cars_list(context.read_token)


@when('send request to delete car with car_id')
def step_impl(context):
    context.response = delete_car(context.write_token, str(context.car_id))


@then('receive response with code {code:d}')
def step_impl(context, code):
   assert_that(context.response.status_code, equal_to(code))


@then('add car response is valid')
def step_impl(context):
    validatejson.add_car_response_success(context.response.json())


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


@then('delete car response is valid')
def step_impl(context):
    validatejson.delet_car_response_success(context.response.json())


@then('car with car_id is absent in app')
def step_impl(context):
    car_id_is_absent_in_app(context.car_id, context.read_token)


@then('response contains error message: {error_message}')
def step_impl(context, error_message):
    if 'car_id' in error_message:
        error_message.replace('car_id', context.car_id)
    assert_that(context.response.json().get('errorMessage'), equal_to(error_message))

