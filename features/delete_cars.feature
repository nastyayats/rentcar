
  Feature: delete car

    Scenario: delete car
      Given car with car_id exists in app
      When send request to delete car with car_id
      Then receive response with code 200
      Then delete car response is valid
      Then car with car_id is absent in app


    @fails @bug#2
#    Scenario: try to delete car that does not exist
#      Given car with car_id is absent in app
#      When send request to delete car with car_id
#      Then receive response with code 404
#      Then response contains error message: car with id car_id not found in database


