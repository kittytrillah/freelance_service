Feature: Submit proposals

  Scenario: Submit new proposal
    Given a job advertisement random
    When we offer our candidature
    Then service register a proposal



    #    ////////////////////UNDONE//////////////////////
  Scenario: Подача заявки на проект, в котором я соответствую требованиям
    Given У меня есть навык web, 3d, gamedev в профиле
    And В проекте web, 3d, gamedev указан в обязательных навыках
    When Я отправляю заявку на выполнение проекта
    Then Моя заявка отправлена


  Scenario: Подача заявки на проект, для которого у меня нет необходимых навыков, у проекта стоит Soft block
    Given У меня нет навыка web в профиле, но есть 3d, gamedev
    And В проекте web, 3d, gamedev указан в обязательных навыках
    When Я пытаюсь отправить заявку на выполнение проекта
    Then Моя отправляется (но не попадет в приоритетные)


  Scenario: Подача заявки на проект, для которого у меня нет необходимых навыков, у проекта стоит Hard block
    Given У меня нет навыка web в профиле, но есть 3d, gamedev
    And В проекте web, 3d, gamedev указан в обязательных навыках
    When Я пытаюсь отправить заявку на выполнение этого проекта
    Then Моя заявка не отправляется



