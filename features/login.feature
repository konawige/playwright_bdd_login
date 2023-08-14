Feature: As a user,  wat to be able to log in and access the account page

  Scenario: Given login page, i can login with valid credentials
    Given the login page is open
    When i fill "username" on Login page with value "Willy"
    And i fill "password" on Login page with value "password"
    And i click "submit" button on the login page
    Then the next page is "Account" page
    And the welcome text on Account page contains the value "Willy"


  Scenario: Given a user, when i fill login form with invalid credentials,
  i stay on login page and a error message is displayed
    Given the login page is open
    When i fill "username" on Login page with value "Willy"
    And i fill "password" on Login page with value "pass"
    And i click "submit" button on the login page
    Then the next page is "Login" page
    And the error message on login page is visible