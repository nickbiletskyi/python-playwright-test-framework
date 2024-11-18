from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.header = page.get_by_role("heading", name="Твій донат до кави")
        self.top_bar_username = page.locator(".dropdown-button .topbar-user-name") # //div[contains(@class, 'dropdown-button')]/*[contains(@class, 'user-icon')]/following-sibling::div[1]]

    def navigate(self):
        self.page.goto("http://localhost:4200/main")




