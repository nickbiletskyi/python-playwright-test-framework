import pytest
from playwright.sync_api import Page, Playwright, expect, sync_playwright

from pom.home_page import HomePage
from pom.login_page import LoginPage


def test_login(set_up_browser_page_scope: Page):
    page = set_up_browser_page_scope
    home_page = HomePage(page=page)
    expect(home_page.top_bar_username).to_be_visible()
    assert page.title() == "Non-Existent Title"


@pytest.mark.parametrize(
    "username, password",
    [
        ("morningdonate@gmail.com", "password1"),
        ("morningdonate@gmail", "password"),
        ("morningdonate@gmail", "sadasklkld"),
    ],
)
def test_login_negative_scenarios(set_up_browser_page_scope: Page, username, password):
    page = set_up_browser_page_scope
    login_page = LoginPage(page=page)
    login_page.navigate()
    login_page.login_with_user(username=username, password=password)
    home_page = HomePage(page=page)
    expect(home_page.top_bar_username).not_to_be_visible(timeout=5000)


# it will be 9 tests
@pytest.mark.parametrize(
    "username",
    ["morningdonate@gmail.com", "morningdonate@gmail", "morningdonate@gmail"],
)
@pytest.mark.parametrize("password", ["password1", "password", "sadasklkld"])
def test_login_negative_scenarios(set_up_browser_page_scope: Page, username, password):
    page = set_up_browser_page_scope
    login_page = LoginPage(page=page)
    login_page.navigate()
    login_page.login_with_user(username=username, password=password)
    home_page = HomePage(page=page)
    expect(home_page.top_bar_username).not_to_be_visible(timeout=5000)
