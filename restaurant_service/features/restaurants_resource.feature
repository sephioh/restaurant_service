Feature: Restaurants API resource

  Scenario: GET /restaurants
    Given there is a restaurant
    When we make a HTTP GET request to /api/restaurants/
    Then this restaurant should be listed on the response

  Scenario: POST /restaurants
    When we make a HTTP POST request to /api/restaurants/
    Then this restaurant should be created
