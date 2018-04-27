
  Feature: manage cars list

    Scenario Outline: add a lot of cars
      When create car with brand <brand>, model B, power rating 1 and daily price 2
      And send request to add car
      Then receive response with code 200
      Then add car response is valid
      When send request to get cars list
      Then get cars list response is valid and contains N cars with unique ids

      Examples: brand names
      | brand |
      | A     |
      | B     |
      | C     |
      | D     |
      | E     |
      | F     |
      | G     |
      | H     |
      | I     |
      | J     |
      | K     |
      | L     |
      | M     |
      | N     |


    Scenario: get cars list
      Given app contains default cars list
      When send request to get cars list
      Then receive response with code 200
      And get cars list response is valid and contains N cars with unique ids


    Scenario: get car
      When send request to get car with car_id 1
      Then receive response with code 200
      Then get car response is valid
      Then response contains car Ford, Focus with power rating 100 and daily price 100


    Scenario: try to get car with unexisting car id
      When send request to get car with car_id 100
      Then receive response with code 404
      Then response contains error message: car with id <car_id> not found in database


    Scenario Outline: add cars
      When create car with brand <brand>, model <model>, power rating <power> and daily price <price>
      And send request to add car
      Then receive response with code 200
      Then add car response is valid
      When send request to get cars list
      Then get cars list response is valid and contains N cars with unique ids

      Examples: valid car parameters
      | brand  | model |power|price|
      | TOYOTA | YARIS | 1   | 1   |
      | TOYOTA | YARIS | 1   | 1   |
      | TOYOTA | YARIS | 500 | 500 |
      | TOYOTA | CAMRY | 500 | 500 |


    Scenario Outline: try to add car with invalid daily price
      When create car with brand TOYOTA, model YARIS, power rating 100 and daily price <price>
      And send request to add car
      Then receive response with code 400
      Then response contains error message: <error_message>

      Examples: invalid price values
      |price| error_message                                                      |
# bug#4     | 0   | Key 'daily_price' must have a value >= 0 and <= 500, got value 0   |
      | -1  | Key 'daily_price' must have a value >= 0 and <= 500, got value -1  |
      | 501 | Key 'daily_price' must have a value >= 0 and <= 500, got value 501 |


    Scenario Outline: try to add car with invalid power rating
      When create car with brand TOYOTA, model YARIS, power rating <power> and daily price 100
      And send request to add car
      Then receive response with code 400
      Then response contains error message: <error_message>

      Examples: invalid power rating values
      |power| error_message                                                      |
      | 0   | Key 'power_rating' must have a value > 0 and <= 500, got value 0   |
      | -1  | Key 'power_rating' must have a value > 0 and <= 500, got value -1  |
      | 501 | Key 'power_rating' must have a value > 0 and <= 500, got value 501 |


    Scenario Outline: try to add car with invalid payload
      When create car with payload <payload>
      And send request to add car
      Then receive response with code 400
      Then response contains error message: <error_message>

      Examples: invalid payload
      | payload                                                                    | error_message                                                                                                                                                 |
      | {"brand":"A", "model":"B", "power_rating":1, "daily_price":1, "car_id":1}  | Expected keys in JSON data: ["brand", "model", "power_rating", "daily_price"] got: [u'daily_price', u'brand', u'car_id', u'model', u'power_rating'] |
      | {"brand":"A", "model":"B", "power_rating":1, "daily_price":1, "smth":"str"}| Expected keys in JSON data: ["brand", "model", "power_rating", "daily_price"] got: [u'daily_price', u'brand', u'smth', u'model', u'power_rating']   |
      | {"brand":"A", "model":"B", "power_rating":1}                               | Expected keys in JSON data: ["brand", "model", "power_rating", "daily_price"] got: [u'brand', u'model', u'power_rating'] |
      | {"brand":"A", "model":"B", "daily_price":1}                                | Expected keys in JSON data: ["brand", "model", "power_rating", "daily_price"] got: [u'daily_price', u'brand', u'model']  |
      | {"brand":"A", "power_rating":1, "daily_price":1}                           | Expected keys in JSON data: ["brand", "model", "power_rating", "daily_price"] got: [u'daily_price', u'brand', u'power_rating'] |
      | {"model":"B", "power_rating":1, "daily_price":1}                           | Expected keys in JSON data: ["brand", "model", "power_rating", "daily_price"] got: [u'daily_price', u'model', u'power_rating'] |
# bug#5     | {"brand":"", "model":"B", "power_rating":1, "daily_price":1}               | Expected key 'model' having non-empty string/unicode value, got type <type 'unicode'> with value  |
# bug#5     | {"brand":"A", "model":"", "power_rating":1, "daily_price":1}               | Expected key 'model' having non-empty string/unicode value, got type <type 'unicode'> with value  |
      | {"brand":"A", "model":"B", "power_rating":1, "daily_price":1               | Please use JSON as input data |
      | {"brand":"A", "model":"B", "power_rating":"str", "daily_price":1}          | Expected key 'power_rating' having non-empty integer value, got type <type 'unicode'> with value str |
      | {"brand":"A", "model":"B", "power_rating":1, "daily_price":"str"}          | Expected key 'daily_price' having non-empty integer value, got type <type 'unicode'> with value str  |
# bug#6     | {"brand":"A", "model":"B", "power_rating":1.5, "daily_price":1}            | Expected key 'daily_price' having non-empty integer value, got type <type 'unicode'> with value 1.5  |
# bug#6     | {"brand":"A", "model":"B", "power_rating":1, "daily_price":1.5}            | Expected key 'daily_price' having non-empty integer value, got type <type 'unicode'> with value 1.5  |


    Scenario: delete car
      Given car with car_id exists in app
      When send request to delete car with car_id
      Then receive response with code 200
      Then delete car response is valid
      Then car with car_id is absent in app


#    Blocked by bug#3
#    Scenario: try to get empty cars list
#      Given tokens retrieved
#      Given all cars are removed from app
#      When send request to get cars list
#      Then receive response with code 200
#      And get cars list response is valid and contains 0 cars with unique ids


#    bug#2
#    Scenario: try to delete car that does not exist
#      Given tokens retrieved
#      And car with car_id is absent in app
#      When send request to delete car with car_id
#      Then receive response with code 404
#      Then response contains error message: car with id car_id not found in database


#
#    Scenario: try to perform read operation with write token
#    Scenario: try to perform write operation with read token
#    Scenario: wrong urls




