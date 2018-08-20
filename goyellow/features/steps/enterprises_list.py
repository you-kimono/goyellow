from behave import *
import time


@given('there are no enterprises')
def step_impl(context):
    pass


@when('I access the enterprise list page')
def step_impl(context):
    context.browser.get(
        context.test.live_server_url + '/enterprises/'
    )
    time.sleep(3)


@then('I see the message "{message}"')
def step_impl(context, message):
    context.test.assertIn(message, context.browser.page_source)


@then('I see the list of enterprises contains "{enterprise_name}"')
def step_impl(context, enterprise_name):
    context.test.assertIn(
        enterprise_name,
        context.browser.page_source
    )