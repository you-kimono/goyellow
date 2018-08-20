from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from enterprises.models import Enterprise
import time


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
    time.sleep(3)
    element = context.browser.find_element(By.ID, 'new_enterprise_form')
    assert element is not None


@when('I compile the form with name "{enterprise_name}" and press submit')
def step_impl(context, enterprise_name):
    time.sleep(3)
    element = context.browser.find_element(By.ID, 'id_enterprise_name')
    element.send_keys(enterprise_name)
    element.send_keys(Keys.RETURN)


@then('the a new enterprise with name "{enterprise_name}" is created')
def step_impl(context, enterprise_name):
    time.sleep(3)
    enterprise = Enterprise.objects.first()
    context.test.assertEqual(enterprise.enterprise_name, enterprise_name)


@then('I see that the inputbox is centered')
def step_impl(context):
    context.browser.set_window_size(1024, 768)
    time.sleep(3)
    element = context.browser.find_element(By.ID, 'id_enterprise_name')
    context.test.assertAlmostEqual(
        element.location['x'] + element.size['width'] / 2,
        512,
        delta = 10
    )
