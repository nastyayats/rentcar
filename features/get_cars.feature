
  Feature: manage cars list

    Scenario: get car
      Given create car with brand TOYOTA, model YARIS, power rating 100 and daily price 150
      When send request to add car and retrieve its car_id
      When send request to get car
      Then receive response with code 200
      Then get car response is valid
      Then response contains car TOYOTA, YARIS with power rating 100 and daily price 150


    Scenario: try to get car with unexisting car id
      When send request to get car with car_id 999
      Then receive response with code 404
      Then response contains error message: car with id <car_id> not found in database


    @blocked @bug#3
    Scenario: try to get empty cars list
      Given all cars are removed from app
      When send request to get cars list
      Then receive response with code 200
      And get cars list response is valid but contains no cars


    @blocked @bug#3
    Scenario: get cars list
      Given all cars are removed from app
      And create car with brand A, model B, power rating 1 and daily price 2
      When send requests to add 10 cars and verify cars added
      When send request to get cars list
      Then receive response with code 200
      And get cars list response is valid and contains 10 cars with unique ids







