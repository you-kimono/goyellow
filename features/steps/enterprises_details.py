from behave import *
import unittest


@given('there is a set of enterprises')
def step_impl(context):
    for enterprise in context.table:
        #make it add the enterprise to the database
        pass
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
