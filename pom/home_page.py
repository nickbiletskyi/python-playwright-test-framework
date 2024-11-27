from playwright.sync_api import Page, expect


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.header = page.get_by_role("heading", name="Твій донат до кави")
        self.top_bar_username = page.locator(
            ".dropdown-button .topbar-user-name"
        )  # //div[contains(@class, 'dropdown-button')]/*[contains(@class, 'user-icon')]/following-sibling::div[1]]
        self.random_donate_button = page.locator(".random-donate > button")
        self.random_donate_modal_header = page.locator("app-modal h2")

    def navigate(self):
        self.page.goto("http://localhost:4200/main")

    def test_random_donate(self):
        expect(self.random_donate_button).to_be_visible()
        self.random_donate_button.click()
        expect(self.random_donate_modal_header).to_have_text(" Рандомний донат ")
