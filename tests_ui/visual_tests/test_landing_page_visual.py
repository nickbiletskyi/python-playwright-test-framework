import time

from playwright.sync_api import Playwright, expect

from pom.home_page import HomePage


def test_visual_landing(page, assert_snapshot) -> None:
    page.goto("http://localhost:4200/main")
    home_page = HomePage(page=page)
    # expect(home_page.random_donate_button).to_be_visible()
    assert_snapshot(page.screenshot(full_page=True), threshold=1)
