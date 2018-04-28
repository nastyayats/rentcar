from jsonschema import validate
import os


def validate_json_in_response_to_successful_get_token_request(response):
    schema = {
        "$ref": "file:///" + os.getcwd() + "\\definitions.json#/definitions/get_token_response_success"
    }
    validate(response, schema)


def validate_json_in_response_to_successful_add_car_request(response):
    schema ={
        "$ref": "file:///" + os.getcwd() + "\\definitions.json#/definitions/add_car_response_success"
    }
    validate(response, schema)


def validate_json_in_response_to_successful_get_car_request(response):
    schema = {
        "$ref": "file:///" + os.getcwd() + "\\definitions.json#/definitions/get_car_response_success"
    }
    validate(response, schema)


def validate_json_in_response_to_successful_get_cars_list_request(response):
    schema = {
        "$ref": "file:///" + os.getcwd() + "\\definitions.json#/definitions/get_cars_list_response_success"
    }
    validate(response, schema)


def validate_json_in_response_to_successful_delete_car_request(response):
    schema = {
        "$ref": "file:///" + os.getcwd() + "\\definitions.json#/definitions/delete_car"
    }
    validate(response, schema)


def validate_json_in_response_to_failed_request(response):
    schema = {
        "$ref": "file:///" + os.getcwd() + "\\definitions.json#/definitions/response_fail"
    }
    validate(response, schema)
