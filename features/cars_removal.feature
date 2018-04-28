  @remove @cars
  Feature: cars removal

    Scenario: remove car
      Given car with car_id exists in db
      When send request to remove car with car_id
      Then receive response with code 200
      Then response for car removal request is valid
      Then car with car_id is absent in db


    @fails @bug#2
    Scenario: try to remove car that does not exist in db
      Given car with car_id is absent in db
      When send request to remove car with car_id
#      next step fails because of bug#2
      Then receive response with code 404
      Then response contains error message: car with id <car_id> not found in database


