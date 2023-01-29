
from behave import *

# given - sets initial situation
# when - steps from test
# then - verify from test


@given('welcome: I am a user on herokuapp welcome page')
def step_impl(context):
    context.welcome_page.navigate_welcome_page()


@when('welcome: I click Form Authentication')
def step_impl(context):
    context.welcome_page.click_form_auth_link()


@when('login: I set my username')
def step_impl(context):
    context.login_page.set_username()


@when('login: I set my password')
def step_impl(context):
    context.login_page.set_password()


@when('login: I click login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('login: I verify that email validation message is correct')
def step_impl(context):
    context.login_page.verify_correct_login()

