from behave import *
import validatejson
from tokens import *


@given('prepare payload for token generation with client id {client_id}, client secret {client_secret}, scope {scope}')
def step_impl(context, client_id, client_secret, scope):
    context.payload = prepare_token_payload(client_id, client_secret, scope)


@given('prepare payload {payload} for token generation')
def step_impl(context, payload):
    context.payload = payload
    print('Payload: {}'.format(payload))


@when('send request to generate token')
def step_impl(context):
    context.response = send_token_generation_request(context.payload)


@when('store token into {context_type} context')
def step_impl(context, context_type):
    if context_type == 'r_token':
        context.r_token = context.response.json().get('auth_token')
    if context_type == 'w_token':
        context.w_token = context.response.json().get('auth_token')


@then('response for token generation request is valid')
def step_impl(context):
    validatejson.successful_token_generation_response(context.response.json())

