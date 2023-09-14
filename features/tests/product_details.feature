# Created by Admin at 8/17/2023
Feature: Test for Product Page

  Scenario: User can select colors
    Given Open Amazon product B07BJKRR25 page
    Then Verify user can click through colors

  Scenario: User can select certain colors
    Given Open Amazon product B07BJKRR25 page
    Then Verify user can click through selected colors

  Scenario: Verify user can hovers over New Arrivals to see the deals
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify user can see Women deals

