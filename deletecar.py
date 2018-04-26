import requests
from hamcrest import assert_that, equal_to
from getcar import get_car
from getcarslist import get_cars_list


def delete_car(write_token, car_id):
    headers = {'Content-Type': 'application/json', 'auth_token': write_token}
    response = requests.delete('http://localhost:5000/v1/cars/' + car_id, headers=headers)
    print(response.text)
    return response


def car_id_is_absent_in_app(car_id, read_token):
    response = get_car(str(car_id), read_token)
    assert_that(response.status_code, equal_to(404))
    response = get_cars_list(read_token)
    ids_list = list()
    for x in response.json().get('data'):
        ids_list.append(x.get('car_id'))
    assert_that(car_id not in ids_list)
