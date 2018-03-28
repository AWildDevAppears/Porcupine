Feature: Side Navigation
  In order to see the structure of my database
  As a user
  I need to be able to see a list of datasets

  Scenario: Load definitions file
    Given we have loaded the definitions from "defGood.yml"
    Then I should see the following fields
      | name  | description |
      | A     | Item A      |
      | B     | Item B      |
      | C     | Item C      |

  Scenario: Corrupt definitions - no model
    Given we have loaded the definitions from "defBad.yml"
    Then we should receive the error "Cannot load definitions, model not found for C"

  Scenario: Corrupt definitions - no description
    Given we have loaded the definitions from "defBad2.yml"
    Then we should receive the error "Cannot load definitions, description not found for C"

  Scenario: Corrupt definitions - no file
    Given we have loaded the definitions from "defDoesNotExist.yml"
    Then we should receive the error "Cannot load file ./features/mock/defDoesNotExist.yml, not found"

  Scenario: Corrupt definitions - blank file
    Given we have loaded the definitions from "defEmpty.yml"
    Then we should receive the error "Cannot load file ./features/mock/defEmpty.yml, no content"

  Scenario: Corrupt definitions - missing Model
    Given we have loaded the definitions from "defBadNoModel.yml"
    Then we should receive the error "Cannot load definitions, missing model file for D"
