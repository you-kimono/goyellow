from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from enterprises.models import Enterprise
from features.behave_utilities import *


@given('I am logged in')
def step_impl(context):
    pass


@when('I access the create new enterprise page')
def step_impl(context):
    context.browser.get(
        context.test.live_server_url + '/enterprises/new/'
    )


@then('I see a form where I can enter the enterprise info')
def step_impl(context):
    wait_for(lambda: context.test.assertNotEqual(
        None,
        context.browser.find_element(By.ID, 'new_enterprise_form')
    ))


@when('I compile the form with name "{enterprise_name}"')
def step_impl(context, enterprise_name):
    wait_for(lambda: context.browser.find_element(By.ID, 'id_enterprise_name'))

    element = context.browser.find_element(By.ID, 'id_enterprise_name')
    element.send_keys(enterprise_name)
    #element.send_keys(Keys.RETURN)


@when('I compile the form with address "{enterprise_address}"')
def step_impl(context, enterprise_address):
    wait_for(lambda: context.browser.find_element(By.ID, 'id_enterprise_address'))

    element = context.browser.find_element(By.ID, 'id_enterprise_address')
    element.send_keys(enterprise_address)
    #element.send_keys(Keys.RETURN)


@when('I press submit')
def step_impl(context):
    wait_for(lambda: context.browser.find_element(By.ID, 'id_submit_button'))

    element = context.browser.find_element(By.ID, 'id_submit_button')
    element.send_keys(Keys.RETURN)


@then('a new enterprise is created')
def step_impl(context):
    time.sleep(1)
    wait_for_database_update(
        lambda: context.test.assertEqual(
            Enterprise.objects.all().count(),
            1
        ))


@then('the enterprise has name "{enterprise_name}"')
def step_impl(context, enterprise_name):
    wait_for_database_update(
        lambda: context.test.assertEqual(
            Enterprise.objects.first().enterprise_name,
            enterprise_name
        ))


@then('the enterprise has address "{enterprise_address}"')
def step_impl(context, enterprise_address):
    wait_for_database_update(
        lambda: context.test.assertEqual(
            Enterprise.objects.first().enterprise_address,
            enterprise_address
        ))


@then('I see that the inputbox is centered')
def step_impl(context):
    context.browser.set_window_size(1024, 768)

    wait_for(lambda: context.browser.find_element(By.ID, 'id_enterprise_name'))
    element = context.browser.find_element(By.ID, 'id_enterprise_name')
    context.test.assertAlmostEqual(
        element.location['x'] + element.size['width'] / 2,
        512,
        delta = 10
    )
