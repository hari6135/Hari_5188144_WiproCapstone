Feature: Ixigo Trip Planner End To End Flow

  Background:
    Given user launches ixigo application


  @smoke @regression
  Scenario: Verify complete ixigo trip planner workflow

    When user performs login flow for end to end

    And user completes planner flow for end to end

    And user applies travel filters for end to end

    And user selects tourist location for end to end

    Then tourist location should open successfully for end to end

    And user verifies google map page

    And user clicks book now

    Then flight details page should open successfully