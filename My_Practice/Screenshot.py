from playwright.sync_api import sync_playwright

def take_screenshot():
    # Initialize Playwright
    with sync_playwright() as p:
        # Launch a browser (Chromium in this case)
        browser = p.chromium.launch(headless=True)
        # Open a new browser context and page
        context = browser.new_context()
        page = context.new_page()
        # Navigate to the desired URL
        page.goto("https://google.co.in")
        # Take a screenshot and save it
        page.screenshot(path="screenshot.png")
        print("Screenshot saved as new screenshot.png")
        # Close the browser
        browser.close()

# Call the function
take_screenshot()