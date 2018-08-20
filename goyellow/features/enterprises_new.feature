Feature: Add a new enterprise.

  Scenario: the enterprise lists page is styled
    Given no preconditions
    when I access the create new enterprise page
    then I see that the inputbox is centered

  Scenario: A user accesses the create new enterprise page
    Given I am logged in
    when I access the create new enterprise page
    then I see a form where I can enter the enterprise info

  Scenario: A user creates a new enterprise page
    Given I am logged in
    when I access the create new enterprise page
    and I compile the form with name "new_enterprise" and press submit
    then the a new enterprise with name "new_enterprise" is created