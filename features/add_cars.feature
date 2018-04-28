  @add
  Feature: add car

    Scenario Outline: add cars
      Given prepare car with brand <brand>, model <model>, power rating <power> and daily price <price>
      When send request to add car and retrieve its car_id
      Then receive response with code 200
      Then add car response is valid

      Examples: valid car parameters
      | brand  | model |power|price|
      | TOYOTA | YARIS | 1   | 1   |
      | TOYOTA | YARIS | 1   | 1   |
      | TOYOTA | YARIS | 500 | 500 |
      | TOYOTA | CAMRY | 500 | 500 |


    @fails @bug#4
    Scenario Outline: try to add car with invalid daily price
      Given prepare car with brand TOYOTA, model YARIS, power rating 100 and daily price <price>
      When send request to add car
      Then receive response with code 400
      Then response contains error message: <error_message>

      Examples: invalid price values
      |price| error_message                                                      |
      | 0   | Key 'daily_price' must have a value >= 0 and <= 500, got value 0   |
      | -1  | Key 'daily_price' must have a value >= 0 and <= 500, got value -1  |
      | 501 | Key 'daily_price' must have a value >= 0 and <= 500, got value 501 |


    Scenario Outline: try to add car with invalid power rating
      Given prepare car with brand TOYOTA, model YARIS, power rating <power> and daily price 100
      When send request to add car
      Then receive response with code 400
      Then response contains error message: <error_message>

      Examples: invalid power rating values
      |power| error_message                                                      |
      | 0   | Key 'power_rating' must have a value > 0 and <= 500, got value 0   |
      | -1  | Key 'power_rating' must have a value > 0 and <= 500, got value -1  |
      | 501 | Key 'power_rating' must have a value > 0 and <= 500, got value 501 |


    @fails @bug#5 @bug#6
    Scenario Outline: try to add car with invalid payload
      Given prepare car with payload <payload>
      When send request to add car
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
      | {"brand":"A", "model":"B", "power_rating":1, "daily_price":1               | Please use JSON as input data |
      | {"brand":"A", "model":"B", "power_rating":"str", "daily_price":1}          | Expected key 'power_rating' having non-empty integer value, got type <type 'unicode'> with value str |
      | {"brand":"A", "model":"B", "power_rating":1, "daily_price":"str"}          | Expected key 'daily_price' having non-empty integer value, got type <type 'unicode'> with value str  |
      | {"brand":"", "model":"B", "power_rating":1, "daily_price":1}               | Expected key 'model' having non-empty string/unicode value, got type <type 'unicode'> with value  |
      | {"brand":"A", "model":"", "power_rating":1, "daily_price":1}               | Expected key 'model' having non-empty string/unicode value, got type <type 'unicode'> with value  |
      | {"brand":"A", "model":"B", "power_rating":1.5, "daily_price":1}            | Expected key 'daily_price' having non-empty integer value, got type <type 'unicode'> with value 1.5  |
      | {"brand":"A", "model":"B", "power_rating":1, "daily_price":1.5}            | Expected key 'daily_price' having non-empty integer value, got type <type 'unicode'> with value 1.5  |

