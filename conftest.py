import os

import pytest
from playwright.sync_api import sync_playwright

from pom.login_page import LoginPage


@pytest.fixture(scope="session")
def playwright():
    """
    Playwright session scope fixture.
    """
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser_context(playwright):
    """
    Creates a browser context for the entire session.
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()


@pytest.fixture(scope="session")
def login_set_up_browser(browser_context):
    """
    Logs into the application and prepares the browser context.
    """
    page = browser_context.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_user()
    page.wait_for_load_state("networkidle")
    browser_context.storage_state(path="state.json")
    yield browser_context
    page.close()


@pytest.fixture
def open_new_tab(login_set_up_browser):
    """
    Opens a new tab in the logged-in browser context.
    """
    page = login_set_up_browser.new_page()
    yield page
    page.close()


@pytest.fixture
def set_up_browser_page_scope(playwright):
    """
    Opens a fresh browser page for each test with saved state
    """
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    yield page
    context.close()
    browser.close()


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Hook to determine the result of the test and handle failures.
#     """
#     # Execute all other hooks to get the report
#     outcome = yield
#     report = outcome.get_result()
#
#     # Only proceed if the call phase is the test (not setup/teardown)     # Let's ensure we are dealing with a test report
#     if report.when == "call" and report.failed:
#         # Check if the test function uses the "page" fixture
#         if "set_up_browser" in item.funcargs:
#             # breakpoint()
#             page = item.funcargs["set_up_browser"]
#
#             # Create a directory for screenshots if it doesn't exist
#             project_dir = os.getcwd()  # This gets the current working directory (usually the project root)
#             screenshot_dir = os.path.join(project_dir, "screenshots")
#
#             # Ensure the screenshots directory exists
#             os.makedirs(screenshot_dir, exist_ok=True)
#
#             # Take a screenshot and save it with the test name
#             screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
#
#             # Save the screenshot with the test name
#             page.screenshot(path=screenshot_path)
#             print(f"Screenshot saved to: {screenshot_path}")
