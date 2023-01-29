Feature: Herokuapp login page

  # before every test
  Background:
    Given welcome: I am a user on herokuapp welcome page

    @heroku
    Scenario: Email validation message
      When welcome: I click Form Authentication
      When login: I set my username
      When login: I set my password
      When login: I click login button
      Then login: I verify that email validation message is correct