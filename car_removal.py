import requests
from hamcrest import assert_that, equal_to
from car_retrieval import send_car_retrieval_request
from cars_list_retrieval import send_cars_list_retrieval_request

url = 'http://localhost:5000/v1/cars/'

def send_car_removal_request(write_token, car_id):
    headers = {'Content-Type': 'application/json', 'auth_token': write_token}
    response = requests.delete(url + car_id, headers=headers)
    print('Response to car removal request for car with id {} is received with code {}'.format(car_id, response.status_code))
    print(response.text)
    return response


def verify_car_removal(car_id, read_token):
    response = send_car_retrieval_request(str(car_id), read_token)
    assert_that(response.status_code, equal_to(404))
    response = send_cars_list_retrieval_request(read_token)
    ids_list = [x.get('car_id') for x in response.json().get('data')]
    print('Ids list: {}'.format(ids_list))
    assert_that(car_id not in ids_list)
