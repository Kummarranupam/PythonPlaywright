from playwright.sync_api import sync_playwright

def automate_hrm():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch browser
        page = browser.new_page()

        # Navigate to OrangeHRM login page
        page.goto("https://opensource-demo.orangehrmlive.com")

        # Click on "Orange HRM INC" link at bottom
        page.locator("text=OrangeHRM INC").click()

        # Wait for new page to open
        new_page = browser.contexts[0].pages[-1]  # Get the newly opened page
        new_page.wait_for_load_state()

        # Type email address in the 30-day trial textbox
        new_page.fill("input[name='Email']", "your_email@example.com")

        # Close the new page and switch back to main window
        new_page.close()

        # Enter login credentials in main page
        page.fill("input[name='username']", "Admin")
        page.fill("input[name='password']", "admin123")

        # Close the browser
        browser.close()

# Run the function
automate_hrm()
