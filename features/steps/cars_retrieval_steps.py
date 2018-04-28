from behave import *
import validatejson
from cars import *


@given('car with car_id exists in db')
def step_impl(context):
    response = send_cars_list_retrieval_request(context.read_token)
    context.car_id= get_last_car_id(response.json().get('data'))


@given('car with car_id is absent in db')
def step_impl(context):
    response = send_cars_list_retrieval_request(context.read_token)
    context.car_id = get_last_car_id(response.json().get('data')) + 1


@when('send request to retrieve car with car_id {car_id}')
def step_impl(context, car_id):
    context.response = send_car_retrieval_request(car_id, context.read_token)
    context.car_id = car_id


@when('send request to retrieve car')
def step_impl(context):
    context.response = send_car_retrieval_request(context.car_id, context.read_token)


@when('send request to retrieve cars list')
def step_impl(context):
    context.response = send_cars_list_retrieval_request(context.read_token)


@then('response for car retrieval request is valid')
def step_impl(context):
    validatejson.validate_json_in_response_to_successful_get_car_request(context.response.json())


@then('response contains car {brand}, {model} with power rating {power:d} and daily price {price:d}')
def step_impl(context, brand, model, power, price):
    data = context.response.json().get('data')
    verify_car_data(data, brand, model, power, price)


@then('response for cars list retrieval request is valid and contains {number} cars with unique ids')
def step_impl(context, number):
    validatejson.validate_json_in_response_to_successful_get_cars_list_request(context.response.json())
    data = context.response.json().get('data')
    assert_that(len(data), equal_to(int(number)))
    verify_car_ids_uniqueness(data)


@then('response for cars list retrieval request is valid but contains no cars')
def step_impl(context):
    validatejson.validate_json_in_response_to_successful_get_cars_list_request(context.response.json())
    assert_that(len(context.response.json().get('data')) == 0)


