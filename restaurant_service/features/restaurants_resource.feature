Feature: Restaurants API resource

  Scenario: Retrieve all restaurants
    Given there is a restaurant called The Incredible Restaurant
    When we make a HTTP GET request to /api/restaurants/
    Then this restaurant should be listed on the response

  Scenario: Retrieve single restaurant
    Given there is a restaurant with a 10000 id
    When we make a HTTP GET request to /api/restaurant/10000
    Then this restaurant should be on the response

  Scenario: Create a restaurant
    When we make a HTTP POST request to /api/restaurants/
    Then this restaurant should be created

  Scenario: Delete a restaurant
    Given there is a restaurant with a 10000 id
    When we make a HTTP DELETE request to /api/restaurant/10000
    Then the restaurant with a id 10000 should be deleted
