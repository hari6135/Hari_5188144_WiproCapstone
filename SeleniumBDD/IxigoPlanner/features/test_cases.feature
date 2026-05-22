Feature: Ixigo Trip Planner Test Cases

  Background:
    Given user launches the ixigo planner page


  @smoke
  Scenario: Verify Plan Page Navigation

    When user clicks on plan page for test cases

    Then planner page should open successfully for test cases


  @regression
  Scenario: Verify Travel Month Selection

    When user selects travel month for test cases

    Then selected travel month should be displayed for test cases


  @regression
  Scenario: Verify Filter Selection

    When user completes planner flow for test cases

    And user selects category filter for test cases

    Then filter should be applied successfully for test cases


  @regression
  Scenario: Verify Tourist Location Selection

    When user completes planner flow for test cases

    And user selects category filter for test cases

    And user selects destination country for test cases

    And user selects tourist location card for test cases

    Then tourist location card should open successfully for test cases


  @negative
  Scenario: Verify Invalid Location Search

    When user enters invalid location for test cases

    Then invalid location error message should appear for test cases


  @negative
  Scenario: Verify Book Now Button Absence

    When user completes planner flow for test cases

    And user selects category filter for test cases

    And user selects destination country for test cases

    And user selects invalid from location for test cases

    Then book now button should not be displayed for test cases