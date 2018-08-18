from selenium import webdriver
from django.core import management


def before_all(context):
    context.browser = webdriver.Firefox()


def after_all(context):
    context.browser.quit()
