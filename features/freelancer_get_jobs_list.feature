Feature: Client Jobs

  Scenario: Get jobs list
     Given filter parameters
        | name        |
        | description |
        | price       |
        | pay type    |
        | type        |
        | draft       |
    When we open jobs list
    Then service will show every job on it
