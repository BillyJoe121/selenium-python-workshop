Feature: Login Feature
  Scenario: Successful login with valid credentials
    Given the user is on the moodle page
    When the user logs in with valid data
    Then the user should be redirected to the dashboard

  
