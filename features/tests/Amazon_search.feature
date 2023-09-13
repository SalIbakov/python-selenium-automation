# Created by Admin at 8/8/2023
Feature: Amazon Search Testing

  Scenario: verify Amazon Cart is empty when clicked
    Given open Amazon page
    When click Cart Icon
    Then verify Amazon Cart page is empty

  Scenario: verify when clicking Orders takes to Sign in
    Given open Amazon page
    When click Orders
    Then Verify Sign In page opened

  Scenario: verify user can search for phone
    Given open Amazon page
    When search for phone
    Then verify search result is "phone"

  Scenario: verify user can search for shorts
    Given open Amazon page
    When search for shorts
    Then verify search result is "shorts"

  Scenario Outline: Verify user can search for product
    Given open Amazon page
    When search for <search_word>
    Then verify search result is <search_result>
    Examples:
    |search_word   |search_result|
    |socks         |"socks"      |
    |pants         |"pants"      |

  Scenario: verify user can add product to cart
    Given open Amazon page
    When search for MCPosters The Expanse TV Show Series Poster GLOSSY FINISH - TVS709 (24" x 36" (61cm x 91.5cm))
    When click on first product
    When Store product name
    When Click add to Cart Icon
    When Open cart page
    Then verify cart has correct product

  Scenario: Verify user can see product and images
    Given open Amazon page
    When search for coffee
    Then Verify every product has name and image


