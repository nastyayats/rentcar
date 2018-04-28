import requests
from hamcrest import assert_that

url = 'http://localhost:5000/v1/cars'

def send_cars_list_retrieval_request(read_token):
    headers = {'Content-Type': 'application/json', 'auth_token': read_token}
    response = requests.get(url, headers=headers)
    print('Response to cars list retrieval requestis received with code {}'.format(response.status_code))
    print(response.text)
    return response


def get_car_ids(data):
    return [x.get('car_id') for x in data]


def verify_car_ids_uniqueness(data):
    ids = get_car_ids(data)
    assert_that(len(ids) == len(set(ids)))


def get_cars_list_size(data):
    return len(data)


