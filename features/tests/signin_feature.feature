Feature: Signin tests

  Scenario: Amazon users see sign in button
    Given open Amazon page
    Then Verify Sign In is clickable
    When Wait for 3 sec
    Then Verify Sign In is clickable
    Then Verify Sign In disappears
