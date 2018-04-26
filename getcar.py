import requests
from hamcrest import assert_that, equal_to


def get_car(car_id, read_token):
    headers = {'Content-Type': 'application/json', 'auth_token': read_token}
    response = requests.get('http://localhost:5000/v1/cars/' + car_id, headers=headers)
    print('Get car with id {}'.format(car_id))
    print(response)
    print(response.text)
    return response


def verify_car_parameters(data, brand, model, power, price):
    assert_that(data.get('brand'), equal_to(brand))
    assert_that(data.get('model'), equal_to(model))
    assert_that(data.get('power_rating'), equal_to(power))
    assert_that(data.get('daily_price'), equal_to(price))

