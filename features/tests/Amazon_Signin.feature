# Created by Admin at 8/8/2023
Feature: Tests for Amazon Sign In, Log out

  Scenario: verify if logged out user sees Sign In when clicking on Orders
    Given open Amazon page in Logged out mode
    When click Orders
    Then Sign In page opens
    And Sign In header is visible, email input field is present

