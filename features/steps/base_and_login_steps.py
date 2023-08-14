from behave import given, when, then
from behave.api.async_step import async_run_until_complete

from models.base_page import BasePage
from models.login_page import LoginPage


@given('the login page is open')
@async_run_until_complete
async def open_login_url(context):
    login_page = LoginPage(context.page)
    await login_page.navigate()


@when('i fill "{field}" on Login page with value "{value}"')
@async_run_until_complete
async def fill_login_page_field(context, field: str, value: str):
    """
    :param value:
    :param field:
    :type context: behave.runner.Context
    """
    login_page = LoginPage(context.page)
    await login_page.fill_form_field(field, value)


@when('i click "{action}" button on the login page')
@async_run_until_complete
async def click_login_page_button(context, action: str):
    """
    :param action:
    :type context: behave.runner.Context
    """
    login_page = LoginPage(context.page)
    await login_page.click_button(action)


@then('the next page is "{title}" page')
@async_run_until_complete
async def is_next_page(context, title: str):
    """
    :param title:
    :type context: behave.runner.Context
    """
    base_page = BasePage(context.page)
    await base_page.is_title_contains(title)


@then("the error message on login page is visible")
@async_run_until_complete
async def is_login_error_message(context):
    """
    :type context: behave.runner.Context
    """
    login_page = LoginPage(context.page)
    assert await login_page.is_error_message_displayed()
