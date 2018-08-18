Feature: Add a new enterprise.

  Scenario: A user accesses the create new enterprise page
    Given I am logged in
    when I access the create new enterprise page
    then I see a form where I can enter the enterprise info
