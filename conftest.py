import pytest

from pom.login_page import LoginPage


@pytest.fixture(scope="session")
def set_up_browser(browser) -> None:
    """

    :param page:
    :return: None
    pytest --headed: to run in headless mode
    """
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture()
def set_up_browser_page_scope(page) -> None:
    """

    :param page:
    :return: None
    pytest --headed: to run in headless mode
    """
    yield page
    page.close()


@pytest.fixture(scope="session")
def login_set_up_browser(set_up_browser) -> None:
    """

    :param page:
    :return: None
    pytest --headed: to run in headless mode
    """
    page = set_up_browser
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_user()
    yield page
    page.context.close()


@pytest.fixture()
def login_set_up_browser_page_scope(set_up_browser_page_scope) -> None:
    """

    :param page:
    :return: None
    pytest --headed: to run in headless mode
    """
    page = set_up_browser_page_scope
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_user()
    yield page
    page.context.close()


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
