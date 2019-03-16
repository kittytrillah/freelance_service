Feature: Client Jobs

  Scenario: Add new job advertisement
     Given an order parameters
        | name        |
        | description |
        | price       |
        | pay type    |
        | type        |
        | draft       |
    When we create a new job advertisement with name we need indian developer pls
    Then service will add it to list of job offers
