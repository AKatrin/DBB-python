Feature: Login Feature
  As a AT09 student
  I want to test login
  In oder to verify all Login Functionality

  Scenario: Successful login with a valid account
    Given I open the browser at: wwwlogin jhj

  Scenario Outline: Successful login with a valid account
    Given I open the browser at: "<url>"
    Given I fill <account> in Account field
    And I fill <password> in Password field
    Examples:
      | url | account | password |
      | wwwlogin | my |   aaa   |
      | wwwlogin | you | |
      | wwwlocal | you |  aaa     |


  Scenario: Verify that using a existent account the login is successful