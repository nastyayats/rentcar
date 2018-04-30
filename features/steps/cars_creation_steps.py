from behave import *
from cars import *
import validatejson
from hamcrest import assert_that


@given('prepare car with brand {brand}, model {model}, power rating {power:d} and daily price {price:d}')
def step_impl(context, brand, model, power, price):
    context.payload = prepare_car_data(brand, model, power, price)


@given('prepare car with payload {payload}')
def step_impl(context, payload):
    context.payload = payload
    print('Payload: {}'.format(payload))


@when('send request to create car')
def step_impl(context):
    context.response = send_car_creation_request(context.w_token, context.payload)


@when('send requests to create {number:d} cars and verify cars creation')
def step_impl(context, number):
    old_list = send_cars_list_retrieval_request(context.r_token).json().get('data')
    for x in range(0, number):
        send_car_creation_request(context.w_token, context.payload)
    new_list = send_cars_list_retrieval_request(context.r_token).json().get('data')
    assert_that(len(new_list) == len(old_list) + number)
    # current verification is time consuming, but it can be changed
    # after car id will be added to response to car creation request


@when('send request to create car and retrieve its car_id')
def step_impl(context):
    old_list = send_cars_list_retrieval_request(context.r_token).json().get('data')
    context.response = send_car_creation_request(context.w_token, context.payload)
    new_list = send_cars_list_retrieval_request(context.r_token).json().get('data')
    assert_that(len(new_list) == len(old_list) + 1)
    context.car_id = str(get_id_of_created_car(old_list, new_list).pop())
    # retrieval of cars lists before and after car creation request could be removed
    # when car id will be added to response


@then('response for car creation request is valid')
def step_impl(context):
    validatejson.successful_car_creation_response(context.response.json())
