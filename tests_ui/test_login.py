from pom.login_page import LoginPage
from pom.home_page import HomePage
from playwright.sync_api import Playwright, sync_playwright, expect

def test_login(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    login_page = LoginPage(page=page)
    login_page.navigate()
    login_page.login_with_user()

    home_page = HomePage(page=page)
    expect(home_page.top_bar_username).to_be_visible()





with sync_playwright() as playwright:
    test_login(playwright)


