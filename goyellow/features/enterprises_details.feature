Feature: Display an enterprise's details page.

  Scenario Outline: The details page of an existing enterprise displays its name.
    Given there is a set of enterprises
        |   enterprise_name             | enterprise_id     |
        |   test_enterprise             | 1                 |
        |   another_test_enterprise     | 2                 |

    when I access the details page of the enterprise with id "<enterprise_id>"
    then the details page contains the name "<enterprise_name>"

    Examples: Enterprises
        |   enterprise_name             | enterprise_id     |
        |   test_enterprise             | 1                 |
        |   another_test_enterprise     | 2                 |

  Scenario: The details page of a non-existing enterprise cannot be accessed
    Given no preconditions
    when I access the details of a non-existing enterprise
    then I receive a response of 404
