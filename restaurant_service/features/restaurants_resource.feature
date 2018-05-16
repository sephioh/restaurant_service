Feature: Restaurants API resource

  Scenario: Retrieves all restaurants
    Given there is a restaurant called The Incredible Restaurant
    When we make a HTTP GET request to /api/restaurants/
    Then this restaurant should be listed on the response

  Scenario: Retrieves single restaurant
    Given there is a restaurant with a 10000 id
    When we make a HTTP GET request to /api/restaurant/10000
    Then this restaurant should be on the response

  Scenario: Creates a restaurant
    When we make a HTTP POST request to /api/restaurants/
    Then this restaurant should be created

  Scenario: Deletes a restaurant
    Given there is a restaurant with a 10000 id
    When we make a HTTP DELETE request to /api/restaurant/10000
    Then the restaurant with a id 10000 should be deleted

  Scenario: Updates a restaurant using PUT
    Given there is a The Awesome Restaurant restaurant with a 10000 id
    When we make a HTTP PUT request to /api/restaurant/10000 changing the name to The Nice Restaurant
    Then the restaurant with a id 10000 should have the name The Nice Restaurant

  Scenario: Updates a restaurant using PATCH
    Given there is a The Awesome Restaurant restaurant with a 10000 id
    When we make a HTTP PATCH request to /api/restaurant/10000 changing the name to The Nice Restaurant
    Then the restaurant with a id 10000 should have the name The Nice Restaurant
