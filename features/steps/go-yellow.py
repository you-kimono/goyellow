from behave import *
from selenium import webdriver
    
@given('no preconditions')
def step_impl(context):
    pass

@when('we open the homepage')
def step_impl(context):
    context.browser.get('http://localhost:8000')

@then('the title contains "{text}"')
def step_impl(context, text):
    assert 'go-yellow' in context.browser.title
