from behave import *
from selenium.webdriver.common.keys import Keys
import unittest
import time


@given('there is a set of enterprises')
def step_impl(context):
    for enterprise in context.table:
        context.browser.get('http://localhost:8000/enterprises/new')
        inputbox = context.browser.find_element_by_id('id_enterprise_name')
        inputbox.send_keys(enterprise['enterprise_name'])
        inputbox.send_keys(Keys.RETURN)
        time.sleep(4)
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


@when('I access the details of a non-existing enterprise')
def step_impl(context):
    context.browser.get(
        'http://localhost:8000/enterprises/666'
    )


@then('I receive a response of 404')
def step_impl(context):
    assert 'Page not found' in context.browser.title
