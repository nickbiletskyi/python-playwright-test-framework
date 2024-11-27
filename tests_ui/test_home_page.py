import pytest
from playwright.sync_api import Page

from pom.home_page import HomePage


@pytest.mark.regression
@pytest.mark.smoke
def test_home_page(set_up_browser: Page):
    page = set_up_browser
    home_page = HomePage(page=page)
    home_page.navigate()
    page.reload()
    home_page.test_random_donate()


@pytest.mark.skip(reason="not ready")
def test_home_page_to_skip(set_up_browser: Page):
    page = set_up_browser
    home_page = HomePage(page=page)
    home_page.navigate()
    page.reload()
    home_page.test_random_donate()


@pytest.mark.xfail(reason="not ready")
def test_home_page_to_fail(set_up_browser: Page):
    page = set_up_browser
    assert 1 == 2
    home_page = HomePage(page=page)
    home_page.navigate()
    page.reload()
    home_page.test_random_donate()
    browser.close()
