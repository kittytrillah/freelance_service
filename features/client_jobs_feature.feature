Feature: Client Jobs
#    Scenario: Post a new job to the website
#      Given: I have a set of jobs
#          | job_title      | job_description            | job_price | job_pay_type | job_category     | req_skills | job_deadline |
#          | JS Developer   | We need to ...             | 350       | fixed        | web_development  | javascript | 3 days       |
#          | UI Designer    | Our website main page ...  | 15        | hourly       | graphic_design   | sketch     | 5 hours      |
#          | Web Copywriter | We start a business on ... | 10        | hourly       | copywriting      | wordpress  | 24 hours     |
#      When: I create job advertisement
#      Then: The set of active jobs for my account includes
#          | JS Developer   |
#          | UI Designer    |
#          | Web Copywriter |


#    /////////////////////Undone////////////////////

  Scenario: Сортировка заявок на основе требуемых навыков
    Given У меня опубликован проект Ищу фрилансера для разработки веб-приложения
    And Указаны необходимые навыки web, 3d, gamedev
    When Я открываю список заявок от фрилансеров
    Then Заявки отсортированы таким образом, что сначала показываются работники с навыками, а затем все остальные


  Scenario: Создание заказа
    Given Категория работы Веб-разработка
    And Краткое описание заказа с ключевыми словами django, html5, concurrent
    When Приступаю к выбору навыков
    Then  Я получаю подсказки, основанные на категории работы и ключевых словах из краткого описания заказа


  Scenario: Создание заказа
    Given  Категория работы Аналитика
    And Краткое описание заказа без распознаваемых ключевых слов
    When  Приступаю к выбору навыков
    Then Я получаю подсказки, основанные только на категории работы





