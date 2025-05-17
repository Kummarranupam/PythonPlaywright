from playwright.sync_api import sync_playwright

# User credentials (replace with actual login details)
USERNAME = "your_username"
PASSWORD = "your_password"

URL = "https://www.geeksforgeeks.org/"
TUTORIALS_TAB_SELECTOR = "a[title='Tutorials']"  # CSS Selector for Tutorials tab
DROPDOWN_LINKS_SELECTOR = ".mega-dropdown li a"  # Dropdown links selector

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)  # Set headless=True to hide browser
    page = browser.new_page()

    # Navigate to GeeksforGeeks
    page.goto(URL)

    # Click on Login button (modify selector if needed)
    #page.click("a[href*='login']")  # Navigate to login page

    # Enter credentials
    # page.fill("input[name='username']", USERNAME)
    # page.fill("input[name='password']", PASSWORD)
    # page.click("button[type='submit']")  # Click login button

    # Wait for login to complete (modify wait if needed)
    page.wait_for_selector(TUTORIALS_TAB_SELECTOR)

    # Hover over the Tutorials tab
    page.hover(TUTORIALS_TAB_SELECTOR)

    # Get all links in the dropdown
    links = page.query_selector_all(DROPDOWN_LINKS_SELECTOR)

    print("\nTutorials Dropdown Links:")
    for link in links:
        print(link.get_attribute("href"))  # Print link URLs

    browser.close()
