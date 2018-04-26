
  Feature: manage cars list

    Scenario: retrieve cars list
      Given tokens retrieved
      And app contains default cars list
      When send request to get cars list
      Then receive response with code 200
      And get cars list response is valid and contains N cars with unique ids


    Scenario: retrieve car
      Given tokens retrieved
      When send request to get car with car_id 1
      Then receive response with code 200
      Then get car response is valid
      Then response contains car Ford, Focus with power rating 100 and daily price 100


    Scenario Outline: add cars
      Given tokens retrieved
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
      Given tokens retrieved
      When create car with brand TOYOTA, model YARIS, power rating 100 and daily price <price>
      And send request to add car
      Then receive response with code 400
      Then response contains error message: <error_message>

      Examples: invalid price values
      |price| error_message                                                      |
#      | 0   | Key 'daily_price' must have a value >= 0 and <= 500, got value 0   | fails! Bug!
      | -1  | Key 'daily_price' must have a value >= 0 and <= 500, got value -1  |
      | 501 | Key 'daily_price' must have a value >= 0 and <= 500, got value 501 |


    Scenario Outline: try to add car with invalid power rating
      Given tokens retrieved
      When create car with brand TOYOTA, model YARIS, power rating <power> and daily price 100
      And send request to add car
      Then receive response with code 400
      Then response contains error message: <error_message>

      Examples: invalid power rating values
      |power| error_message                                                      |
      | 0   | Key 'power_rating' must have a value > 0 and <= 500, got value 0   |
      | -1  | Key 'power_rating' must have a value > 0 and <= 500, got value -1  |
      | 501 | Key 'power_rating' must have a value > 0 and <= 500, got value 501 |


    Scenario: delete car
      Given tokens retrieved
      And car with car_id exists in app
      When send request to delete car with car_id
      Then receive response with code 200
      Then delete car response is valid
      Then car with car_id is absent in app


#    Fails! bug!!!
#    Scenario: try to delete car that does not exist
#      Given tokens retrieved
#      And car with car_id is absent in app
#      When send request to delete car with car_id
#      Then receive response with code 404
#      Then response contains error message: car with id car_id not found in database


#
#    Scenario: try to perform read operation with write token
#    Scenario: try to perform write operation with read token
#    Scenario: try to get empty cars list
#    Scenario: try to add car without some fields
#    Scenario: try to add car with string instead integer
#    Scenario: make sure that car with error is not added to app



