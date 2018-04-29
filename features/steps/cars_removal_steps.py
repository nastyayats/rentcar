from behave import *
import validatejson
from cars import *


@given('all cars are removed from db')
def step_impl(context):
    response = send_cars_list_retrieval_request(context.read_token)
    ids = get_car_ids(response.json().get('data'))
    for x in ids:
        send_car_removal_request(context.write_token, str(x))


@when('send request to remove car with car_id')
def step_impl(context):
    context.response = send_car_removal_request(context.write_token, str(context.car_id))


@when('send request to remove car with car_id {car_id}')
def step_impl(context, car_id):
    context.response = send_car_removal_request(context.write_token, str(car_id))
    context.car_id = car_id


@then('response for car removal request is valid')
def step_impl(context):
    validatejson.successful_delete_car_response(context.response.json())


@then('car with car_id is absent in db')
def step_impl(context):
    verify_car_removal(context.car_id, context.read_token)
