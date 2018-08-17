from behave import *
import unittest


@given('there is an enterprise with name "{enterprise_name}" and id "{enterprise_id}"')
def step_impl(context, enterprise_name, enterprise_id):
    pass


@when('I access the details page of the enterprise with id "{enterprise_id}"')
def step_impl(context, enterprise_id):
    context.browser.get(
        'http://localhost:8000/enterprises/' +
        str(enterprise_id)
    )


@then('the details page contains the name "{enterprise_name}"')
def step_impl(context, enterprise_name):
    element = context.browser.find_element_by_id('enterprise_name')
    tc = unittest.TestCase('__init__')
    tc.assertEqual(enterprise_name, element.text)
