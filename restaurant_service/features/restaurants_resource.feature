Feature: Restaurants API resource

  Scenario: GET /restaurants
    Given we have a restaurant
     When we make a HTTP GET request to /restaurants
     Then we should receive this restaurant on the response
