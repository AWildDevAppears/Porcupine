Feature: Dataset Creator
  In order to create entries in the database
  As a user
  I need to be able to utilise the form presented to me

  Scenario: Text input - enter text
    Given I have an input of type
      | field | modifier  | optional | reference | multiple |
      | text  |           | False    |           | False    |
    When I enter "Hello"
    Then the form should save

  Scenario: Text input - enter number string
    Given I have an input of type
      | field | modifier  | optional | reference | multiple |
      | text  |           | False    |           | False    |
    When I enter "1234"
    Then the form should save

  Scenario: Integer input - enter Int
    Given I have an input of type
      | field       | modifier  | optional | reference | multiple |
      | numerical   |           | False    |           | False    |
    When I enter "12"
    Then the form should save

  Scenario: Integer input - enter Float
    Given I have an input of type
      | field       | modifier  | optional | reference | multiple |
      | numerical   |           | False    |           | False    |
    When I enter "12.5"
    Then the form should not save
