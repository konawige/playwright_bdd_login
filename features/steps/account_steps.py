from behave import then
from behave.api.async_step import async_run_until_complete

from models.account_page import AccountPage


@then('the welcome text on Account page contains the value "{user}"')
@async_run_until_complete
async def step_impl(context, user: str):
    """
    :param user:
    :type context: behave.runner.Context
    """
    account_page = AccountPage(context.page)
    assert await account_page.is_welcome_text_contains(user)