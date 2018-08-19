from behave import *
from selenium.webdriver.common.by import By
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
    time.sleep(1)
    element = context.browser.find_element(By.ID, 'new_enterprise_form')
    assert element is not None
