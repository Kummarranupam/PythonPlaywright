import re
from time import sleep

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.naukri.com/")
    page.get_by_role("link", name="Login", exact=True).click()
    page.get_by_placeholder("Enter your active Email ID /").click()
    page.get_by_placeholder("Enter your active Email ID /").fill("kummarranupam@gmail.com")
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill("Kummarr@1990")
    page.get_by_placeholder("Enter your password").press("Enter")
    page.get_by_role("button", name="Login", exact=True).click()
    page.get_by_role("link", name="View profile").click()
    sleep(10)
    for i in range(10):
        page.locator("em").filter(has_text="editOneTheme").click()
        page.get_by_role("button", name="Save").click()
        sleep(60)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)