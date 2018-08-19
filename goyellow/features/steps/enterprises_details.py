from behave import *
from enterprises.models import Enterprise


@given('there is a set of enterprises')
def step_impl(context):
    for enterprise in context.table:
        Enterprise.objects.create(enterprise_name=enterprise['enterprise_name'])


@when('I access the details page of the enterprise with id "{enterprise_id}"')
def step_impl(context, enterprise_id):
    context.response = context.test.client.get('http://localhost:8000/enterprises/' + str(enterprise_id) + '/')


@then('the details page contains the name "{enterprise_name}"')
def step_impl(context, enterprise_name):
    context.test.assertContains(context.response, enterprise_name)


@when('I access the details of a non-existing enterprise')
def step_impl(context):
    context.browser.get(
        'http://localhost:8000/enterprises/666/'
    )


@then('I receive a response of 404')
def step_impl(context):
    assert 'Page not found' in context.browser.title
