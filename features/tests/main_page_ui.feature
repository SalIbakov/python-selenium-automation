# Created by Admin at 8/13/2023
Feature: Test Main page UI

  Scenario: Verify BestSellers page has 5 header links
    Given open Amazon page
    When Click BestSellers button
    Then Verify BestSellers page has 5 header links