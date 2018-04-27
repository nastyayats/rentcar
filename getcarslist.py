import requests
from hamcrest import assert_that

def get_cars_list(read_token):
    headers = {'Content-Type': 'application/json', 'auth_token': read_token}
    response = requests.get('http://localhost:5000/v1/cars', headers=headers)
    print('Get cars list')
    print(response)
    print(response.text)
    return response


def get_cars_ids(data):
    ids = list()
    for x in data:
        ids.append(x.get('car_id'))
    return ids


def verify_car_ids_unique(data):
    ids = get_cars_ids(data)
    assert_that(len(ids) == len(set(ids)))


def get_cars_list_size(data):
    return len(data)


