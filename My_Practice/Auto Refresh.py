import time

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.naukri.com/")
    page.click("text = Login")
    time.sleep(3)
    page.get_by_placeholder("Enter your active Email ID / Username").fill("kummarranupam@gmail.com")
    page.get_by_placeholder("Enter your password").fill("Kummarr@1990")
    page.click("//button[@type='submit']")
    page.get_by_role()
    time.sleep(3)