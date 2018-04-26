from jsonschema import validate


def validate_get_token_response_success_json(response):
    schema = {
        "definitions": {
            "get_token_response_success": {
                "type": "object",
                "properties": {
                    "success": {
                        "type": "boolean",
                        "enum": [True]
                    },
                    "auth_token": {"type": "string"}
                },
                "required": ["success", "auth_token"],
                "additionalProperties": False
            }
        },
        "$ref": "#/definitions/get_token_response_success"
    }
    validate(response, schema)


def add_car_response_success(response):
    schema ={
        "type": "object",
        "properties": {
            "success": {
                "type": "boolean",
                "enum": [True]
            },
        },
        "required": ["success"],
        "additionalProperties": False
    }
    validate(response, schema)


def validate_car_data_json(car_data):
    schema = {
        "definitions": {
            "car_details": {
                "type": "object",
                "properties": {
                    "car_id": {"type": "number"},
                    "brand": {"type": "string"},
                    "model": {"type": "string"},
                    "power_rating": {"type": "number"},
                    "daily_price": {"type": "number"},
                },
                "required": ["car_id", "brand", "model", "power_rating", "daily_price"],
                "additionalProperties": False
            }
        },
        "type": "object",
        "data": {"$ref": "#/definitions/car_details"}
    }
    validate(car_data, schema)


def get_car_response_success(response):
    schema = {
        "definitions": {
            "car_details": {
                "type": "object",
                "properties": {
                    "car_id": {"type": "number"},
                    "brand": {"type": "string"},
                    "model": {"type": "string"},
                    "power_rating": {"type": "number"},
                    "daily_price": {"type": "number"},
                },
                "required": ["car_id", "brand", "model", "power_rating", "daily_price"],
                "additionalProperties": False
            },
            "get_car_response_success": {
                "type": "object",
                "properties": {
                    "success": {
                        "type": "boolean",
                        "enum": [True]
                    },
                    "data": {"$ref": "#/definitions/car_details"}
                },
                "required": ["success", "data"],
                "additionalProperties": False
            }
        },
        "$ref": "#/definitions/get_car_response_success"
    }
    validate(response, schema)


def get_cars_list_response_success(response):
    schema = {
        "definitions": {
            "car_details": {
                "type": "object",
                "properties": {
                    "car_id": {"type": "number"},
                    "brand": {"type": "string"},
                    "model": {"type": "string"},
                    "power_rating": {"type": "number"},
                    "daily_price": {"type": "number"},
                },
                "required": ["car_id", "brand", "model", "power_rating", "daily_price"],
                "additionalProperties": False
            },
            "get_cars_list_response_success": {
                "type": "object",
                "properties": {
                    "success": {
                        "type": "boolean",
                        "enum": [True]
                    },
                    "data": {"type": "array",
                             "items": {"$ref": "#/definitions/car_details"}
                             }
                },
                "required": ["success", "data"],
                "additionalProperties": False
            }
        },
        "$ref": "#/definitions/get_cars_list_response_success"
    }
    validate(response, schema)


def validate_response_fail_json(response):
    schema = {
        "definitions": {
            "response_fail": {
                "type": "object",
                "properties": {
                    "success": {
                        "type": "boolean",
                        "enum": [False]
                    },
                    "errorMessage": {"type": "string"}
                },
                "required": ["success", "errorMessage"],
                "additionalProperties": False
            }
        },
        "$ref": "#/definitions/response_fail"
    }
    validate(response, schema)


def delet_car_response_success(response):
    schema = {
        "definitions": {
            "delete_car": {
                "type": "object",
                "properties": {
                    "success": {
                        "type": "boolean",
                        "enum": [True]
                    },
                },
                "required": ["success"],
                "additionalProperties": False
            }
        },
        "$ref": "#/definitions/delete_car"
    }
    validate(response, schema)
