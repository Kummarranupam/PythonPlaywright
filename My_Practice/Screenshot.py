from playwright.sync_api import sync_playwright


def test_take_screenshot():

    # Initialize Playwright
    with sync_playwright() as p:
        # Launch a browser (Chromium in this case)
        browser = p.chromium.launch(headless=True)
        # Open a new browser context and page
        context = browser.new_context()
        page = context.new_page()
        # Navigate to the desired URL
        page.goto("https://playwright.dev")
        print(page.title())
        # Take a screenshot and save it
        page.locator(".gh-text").screenshot(path="test_shot2.png")
        page.screenshot(path="test_screenfull2.png")
        page.screenshot(path="test_screens2.png", full_page=True)

        print("Screenshot saved as new screenshot.png")
        # Close the browser
        browser.close()

# Call the function


take_screenshot()

