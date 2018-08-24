Feature: Show the list of enterprises in the system.

  Scenario: A message is displayed if there are no enterprises
    Given there are no enterprises
    when I access the enterprise list page
    then I see the message "No enterprises available"

  Scenario: A list of enterprises is displayed if there are enterprises
    Given there is a set of enterprises
        |   enterprise_name             | enterprise_id     | enterprise_address            |
        |   test_enterprise             | 1                 | enterprise road               |
        |   another_test_enterprise     | 4                 | enterprise avenue             |
    when I access the enterprise list page
    then I see the list of enterprises contains "test_enterprise"
    and I see the list of enterprises contains "another_test_enterprise"
