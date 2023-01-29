from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from pages.welcome_page import WelcomePage


def before_all(context):
    context.login_page = LoginPage()
    context.secure_page = SecurePage()
    context.welcome_page = WelcomePage()


def after_all(context):
    context.browser.close()

# the context is like a box that contains a type of object like classes from pages
# every time we add a new page on the project we will add an object in context
