import time
from playwright.sync_api import Page, Playwright


def test_amazonadd(playwright:Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    time.sleep(2)
    page.locator("#nav-link-accountList").hover()
    time.sleep(2)
    page.get_by_role("button", name="Sign in").click()
    time.sleep(5)


