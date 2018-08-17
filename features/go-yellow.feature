Feature: opening the site

  Scenario: open the go-yellow website
    Given no preconditions
    when we open the homepage
    then the title contains "go-yellow"
