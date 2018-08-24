from behave import *
from enterprises.models import Enterprise


@given('there is a set of enterprises')
def step_impl(context):
    for enterprise in context.table:
        Enterprise.objects.create(
            enterprise_name=enterprise['enterprise_name'],
            enterprise_address=enterprise['enterprise_address']
        )


@when('I access the details page of the enterprise with id "{enterprise_id}"')
def step_impl(context, enterprise_id):
    context.response = context.test.client.get(context.test.live_server_url + '/enterprises/' + str(enterprise_id) + '/')


@then('the details page contains the name "{enterprise_name}"')
def step_impl(context, enterprise_name):
    context.test.assertContains(context.response, enterprise_name)


@then('the details page contains the address "{enterprise_address}"')
def step_impl(context, enterprise_address):
    context.test.assertContains(context.response, enterprise_address)


@when('I access the details of a non-existing enterprise')
def step_impl(context):
    context.browser.get(
        context.test.live_server_url + '/enterprises/666/'
    )


@then('I receive a response of 404')
def step_impl(context):
    context.test.assertIn('Not Found', context.browser.page_source)
