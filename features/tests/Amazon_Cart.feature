# Created by Admin at 8/8/2023
Feature: Amazon Cart Testing

  Scenario: verify Amazon Cart is empty when clicked
    Given open Amazon page in Logged out mode
    When click Cart Icon
    Then Amazon Cart page is empty