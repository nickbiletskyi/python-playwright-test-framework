import os

from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input[type=email]")
        self.password_input = page.locator("input[type=password]")
        self.login_button = page.locator("button[type=submit]")
        self.heading_login = page.get_by_role("heading", name="Увійти")

    def navigate(self):
        self.page.goto("http://localhost:4200/auth/login")

    def navigate_from_main_page(self):
        self.page.get_by_role("button", name="Увійти").click()
        expect(self.heading_login).to_be_visible()

    def login_with_user(
        self,
        username: str = os.getenv("USER_ADMIN_USERNAME"),
        password: str = os.getenv("USER_ADMIN_PASSWORD"),
    ):
        self.email_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
