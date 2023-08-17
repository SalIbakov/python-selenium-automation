Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown

  Scenario: Sign In page can be opened from Signin popup
    Given open Amazon page
    When Click on button from Signin popup
    Then Verify Sign In page opened