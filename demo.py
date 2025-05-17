from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.wait_for_timeout(2)
    print(page.title())
    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")
    page.get_by_role("button", name = "submit").click()
    #page.wait_for_selector('load')
    browser.close()

