from behave import *
from features.behave_utilities import *


@given('there are no enterprises')
def step_impl(context):
    pass


@when('I access the enterprise list page')
def step_impl(context):
    context.browser.get(
        context.test.live_server_url + '/enterprises/'
    )


@then('I see the message "{message}"')
def step_impl(context, message):
    wait_for(lambda: context.test.assertEqual(
        context.browser.find_element_by_id('id_enterprise_list').text,
        message
    ))


@then('I see the list of enterprises contains "{enterprise_name}"')
def step_impl(context, enterprise_name):
    wait_for(lambda: context.test.assertIn(
        enterprise_name,
        context.browser.find_element_by_id('id_enterprise_list').text
    ))
