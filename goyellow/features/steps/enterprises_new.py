from behave import *
from selenium.webdriver.common.by import By


@given('I am logged in')
def step_impl(context):
    pass


@when('I access the create new enterprise page')
def step_impl(context):
    context.browser.get(
        'http://localhost:8000/enterprises/new/'
    )


@then('I see a form where I can enter the enterprise info')
def step_impl(context):
    present = context.browser.find_element(By.ID, 'new_enterprise_form')
    assert present is True
