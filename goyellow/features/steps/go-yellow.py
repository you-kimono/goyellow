from behave import *


@given('no preconditions')
def step_impl(context):
    pass


@when('we open the homepage')
def step_impl(context):
    context.browser.get(context.test.live_server_url)


@then('the title contains "{text}"')
def step_impl(context, text):
    assert 'go-yellow' in context.browser.title
