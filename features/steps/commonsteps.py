from behave import *
from hamcrest import *


@given('app contains default cars list')
def step_impl(context):
    pass #add app restart here


@then('receive response with code {code:d}') #change to response with status ok
def step_impl(context, code):
   assert_that(context.response.status_code, equal_to(code))


@then('response contains error message: {error_message}')
def step_impl(context, error_message):
    if 'car_id' in error_message:
        error_message.replace('car_id', context.car_id)
    assert_that(context.response.json().get('errorMessage'), equal_to(error_message))
