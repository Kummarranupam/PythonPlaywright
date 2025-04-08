# conftest file data will have access to all files in the same path

import pytest

# this is used for running browser from terminal
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="session")
def user_credentials(request): # 'request' is a global request parameter. this can access global variable and local pytest variable
    return request.param # this is used to access parameter attached to fixture under test to run

#this is setup for giving browser value from terminal
@pytest.fixture
def browserInstance(playwright, request):
    global browser
    browser_name = request.config.getoption("browser_name")
    #url = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()



