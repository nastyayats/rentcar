import requests
from hamcrest import assert_that, equal_to

url = 'http://localhost:5000/v1/cars/'

def create_headers(token):
    return {'Content-Type': 'application/json', 'auth_token': token}

def send_car_retrieval_request(car_id, read_token):
    response = requests.get(url + car_id, headers=create_headers(read_token))
    print('Response to car retrieval request for car with id {} is received with code {}'.format(car_id, response.status_code))
    print(response.text)
    return response


def verify_car_data(data, brand, model, power, price):
    assert_that(data.get('brand'), equal_to(brand))
    assert_that(data.get('model'), equal_to(model))
    assert_that(data.get('power_rating'), equal_to(power))
    assert_that(data.get('daily_price'), equal_to(price))

