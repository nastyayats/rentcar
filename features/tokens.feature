
  @tokens
  Feature: verify tokens

    Scenario Outline: generate tokens and validate token generation responses
      Given prepare payload for token generation with client id <client_id>, client secret <client_secret>, scope <scope>
      When send request to generate token
      Then receive response with code 200
      Then response for token generation request is valid

      Examples: invalid payload
      |client_id                        | client_secret                                   |scope|
      |f2a1ed52710d4533bde25be6da03b6e3 | ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q | R   |
      |f2a1ed52710d4533bde25be6da03b6e3 | ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q | W   |


    @fails @bug8
    Scenario Outline: try to create token with invalid input data
      Given prepare payload <payload> for token generation
      When send request to generate token
      Then receive response with code 400
      Then response contains error message: <error_message>

      Examples: invalid payload
      |payload                                                     |error_message|
      |{"client_id":"123f", "scope":"W"}                           | Bad Request: Missing/Wrong Input data |
      |{"client_secret":"ABCDEFG", "scope":"R"}                    | Bad Request: Missing/Wrong Input data |
      |{"client_id":"123f", "client_secret":"ABCDEFG"}             | Bad Request: Missing/Wrong Input data |
      |{"client_id":"123f" "client_secret":"ABCDEFG", "scope":"R"} | Please use JSON as input data         |
#      next example fails because of bug#9
      |{"client_id":"123f", "client_secret":"ABCDEFG", "scope":"A"}| Bad Request: Missing/Wrong Input data |
      |{"client_id":"123f", "client_secret":"ABCDEFG", "scope":""} | Bad Request: Missing/Wrong Input data |


    @fails @bug9
    Scenario Outline: try to use token with lack of permissions for write operations
      Given prepare payload for token generation with client id <client_id>, client secret <client_secret>, scope <scope>
      When send request to generate token
      Then receive response with code 200
      When store token into w_token context

      Given prepare car with brand TOYOTA, model YARIS, power rating 100 and daily price 200
      When send request to create car
      Then receive response with code 401
      Then response contains error message: <error_message>

      Examples: unauthorized client
      |client_id                        | client_secret                                   |scope| error_message                                         |
      |f2a1ed52710d4533bde25be6da03b6e3 | ABCDEFG                                         | W   | 'auth_token' in header does not have write permissions|
      |123f                             | ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q | W   | 'auth_token' in header does not have write permissions|
#      next example fails because of bug#9
      |f2a1ed52710d4533bde25be6da03b6e3 | ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q | R   | 'auth_token' in header does not have write permissions|
      |F2A1ED52710D4533BDE25BE6DA03B6E3 | zydpllbwsk3mvqjsiyhb1or2jxcy0x2c5uj2qar2maait5q | W   | 'auth_token' in header does not have write permissions|


    Scenario Outline: try to use token with lack of permissions for read operations
      Given prepare payload for token generation with client id <client_id>, client secret <client_secret>, scope R
      When send request to generate token
      Then receive response with code 200
      When store token into r_token context

      When send request to retrieve cars list
      Then receive response with code 401
      Then response contains error message: <error_message>

      Examples: unauthorized client
      |client_id                        | client_secret                                   | error_message                                                 |
      |f2a1ed52710d4533bde25be6da03b6e3 | ABCDEFG                                         | 'auth_token' in header does not have read or write permissions|
      |123f                             | ZYDPLLBWSK3MVQJSIYHB1OR2JXCY0X2C5UJ2QAR2MAAIT5Q | 'auth_token' in header does not have read or write permissions|
      |F2A1ED52710D4533BDE25BE6DA03B6E3 | zydpllbwsk3mvqjsiyhb1or2jxcy0x2c5uj2qar2maait5q | 'auth_token' in header does not have read or write permissions|


