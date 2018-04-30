**Current project is designed to test "rent_a_car" application.**

Project uses "behave" for tests structuring and execution.

Project contains tests for creation, retrieval and removal of cars and cars lists,
which are splited on 3 features - cars_creation, cars_removal, cars_retrieval.

There is one more feature - tokens, which is meant to contain tests for
tokens generation and usage. Its implementation is planned for future.

If application was running before test execution, it should be restarted.
It would be possible to avoid application restart after fix of bug#1 from bugs!!!.txt file,
or after implementation of improvement#1 from bugs!!!.txt and changes in tests.

To execute tests from command line enter project directory and run command:
```
behave
```
Use tags to execute particular groups of tests.
To run test for car creation, removal, retrieval:
```
behave --tags=cars
```
or
```
behave --tags=create,remove,delete
```
To exclude tests, that fails because of known issues in application:
```
behave --tags=-fails
```
To execute tests that verify fix of particular issue:
```
behave --tags=bug3
```


