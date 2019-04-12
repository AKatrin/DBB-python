@FJ @regresion
Feature: Do a addition of 2 numbers

  Scenario: Addition test case
    Given I have the calculator opened
    When I enter a first number: 60
    And I press the + button
    And I enter a second number: 10
    And I press = button to performance the operation
    Then I should have 70 as a sum

  @AT09 @create_user
  Scenario Outline: Addition test case
    Given I have the calculator opened
    When I enter a first number: <first>
    And I press the <operator> button
    And I enter a second number: <second>
    And I press <equal> button to performance the operation
    Then I should have <result> as a sum
    Examples:
      | first | operator | second | equal | result |
      |   10  |     +    |    2   |   =   |   12   |
      |   10  |     -    |    2   |   =   |    8   |
      |   10  |     *    |    2   |   =   |   20   |
      |   10  |     /    |    2   |   =   |    5   |