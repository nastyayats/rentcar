  @retrieve @cars
  Feature: retrieve cars and cars lists

    Scenario: get car
      Given prepare car with brand TOYOTA, model YARIS, power rating 100 and daily price 150
      When send request to create car and retrieve its car_id
      When send request to retrieve car
      Then receive response with code 200
      Then response for car retrieval request is valid
      Then response contains car TOYOTA, YARIS with power rating 100 and daily price 150


    Scenario: try to get car with not existing car id
      When send request to retrieve car with car_id 999
      Then receive response with code 404
      Then response contains error message: car with id <car_id> not found in database


    @fails @blocked @bug#3
    Scenario: try to get empty cars list
#      next step fails because of bug#3
      Given all cars are removed from db
      When send request to retrieve cars list
      Then receive response with code 200
      And response for cars list retrieval request is valid but contains no cars


    @blocked @bug#3
    Scenario: get cars list
#      next step fails because of bug#3
      Given all cars are removed from db
      And prepare car with brand A, model B, power rating 1 and daily price 2
      When send requests to create 10 cars and verify cars creation
      When send request to retrieve cars list
      Then receive response with code 200
      And response for cars list retrieval request is valid and contains 10 cars with unique ids







