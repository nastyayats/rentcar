from jsonschema import validate
import os

definitions_path = "file:///" + os.getcwd() + "\\definitions.json#/definitions"

def successful_get_token_response(response):
    schema = {
        "$ref": definitions_path + "/get_token_response_success"
    }
    validate(response, schema)


def successful_add_car_response(response):
    schema ={
        "$ref":  definitions_path + "/add_car_response_success"
    }
    validate(response, schema)


def successful_get_car_response(response):
    schema = {
        "$ref":  definitions_path + "/get_car_response_success"
    }
    validate(response, schema)


def successful_get_cars_list_response(response):
    schema = {
        "$ref":  definitions_path + "/get_cars_list_response_success"
    }
    validate(response, schema)


def successful_delete_car_response(response):
    schema = {
        "$ref":  definitions_path + "/delete_car"
    }
    validate(response, schema)


def failed_response(response):
    schema = {
        "$ref":  definitions_path + "/response_fail"
    }
    validate(response, schema)
