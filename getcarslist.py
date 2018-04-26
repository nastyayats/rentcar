import requests
from hamcrest import assert_that

def get_cars_list(read_token):
    headers = {'Content-Type': 'application/json', 'auth_token': read_token}
    response = requests.get('http://localhost:5000/v1/cars', headers=headers)
    print(response.text)
    return response


def verify_car_ids_unique(data):
    ids = list()
    for x in data:
        ids.append(x.get('car_id'))
    assert_that(len(ids) == len(set(ids)))


