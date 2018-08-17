Feature: Display an enterprise's details page.

  Scenario: Open the enterprise's details page.
    Given there is an enterprise with name "test_enterprise" and id "1"
    when I access the details page of the enterprise with id "1"
    then the details page contains the name "test_enterprise"
