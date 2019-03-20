#Feature: Client Jobs
#
#  Scenario: Add new job advertisement
#     Given an order parameters
#        | name        |
#        | description |
#        | price       |
#        | pay type    |
#        | type        |
#        | draft       |
#    When we create a new job advertisement with name we need indian developer pls
#    Then service will add it to list of job offers

Feature: Client Jobs
    Scenario: Post a new job to the website
      Given: I have a set of jobs
          | job_title      | job_description            | job_price | job_pay_type | job_category     | req_skills | job_deadline |
          | JS Developer   | We need to ...             | 350       | fixed        | web_development  | javascript | 3 days       |
          | UI Designer    | Our website main page ...  | 15        | hourly       | graphic_design   | sketch     | 5 hours      |
          | Web Copywriter | We start a business on ... | 10        | hourly       | copywriting      | wordpress  | 24 hours     |
      When: I create job advertisement
      Then: The set of active jobs for my account includes
          | JS Developer   |
          | UI Designer    |
          | Web Copywriter |