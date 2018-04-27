from behave import *
import validatejson
from getcarslist import get_cars_list, get_cars_ids, verify_car_ids_unique
from deletecar import delete_car, car_id_is_absent_in_app


@given('all cars are removed from app')
def step_impl(context):
    response = get_cars_list(context.read_token)
    ids = get_cars_ids(response.json().get('data'))
    for x in ids:
        delete_car(context.write_token, str(x))


@when('send request to delete car with car_id')
def step_impl(context):
    context.response = delete_car(context.write_token, str(context.car_id))


@when('send request to delete car with car_id {car_id}')
def step_impl(context, car_id):
    context.response = delete_car(context.write_token, str(car_id))
    context.car_id = car_id


@then('delete car response is valid')
def step_impl(context):
    validatejson.delet_car_response_success(context.response.json())


@then('car with car_id is absent in app')
def step_impl(context):
    car_id_is_absent_in_app(context.car_id, context.read_token)
