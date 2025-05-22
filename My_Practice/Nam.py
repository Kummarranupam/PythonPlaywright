from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://omayo.blogspot.com/")

    # Print all available elements
    print(page.content())

    browser.close()
