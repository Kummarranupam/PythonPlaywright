import time

from playwright.sync_api import Playwright
from playwright.sync_api import Page
def test_website(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://money.rediff.com/gainers")
    time.sleep(5)