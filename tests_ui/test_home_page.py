from pom.login_page import LoginPage
from pom.home_page import HomePage
from playwright.sync_api import Playwright, sync_playwright, expect

def test_home_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    home_page = HomePage(page=page)
    home_page.navigate()
    page.reload()
    home_page.test_random_donate()
    browser.close()


# with sync_playwright() as playwright:
#     test_login(playwright)


