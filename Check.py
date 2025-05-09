import time

from playwright.sync_api import Page

# def test_website(page:Page):
#
#     page.goto("https://www.geeksforgeeks.org/")
#     time.sleep(3)
#     page.locator(".headerMainListItem").filter(has_text="Tutorials").hover()
#     page.hover("text=Tutorials")
#
#
#     time.sleep(3)


from playwright.sync_api import sync_playwright


def scrape_tutorials():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True for headless mode
        page = browser.new_page()
        page.goto("https://www.geeksforgeeks.org/")

        # Hover over the Tutorials module
        page.hover("text=Tutorials")

        # Wait for the dropdown to appear
        page.wait_for_selector(".mega-dropdown")  # Ensuring the dropdown becomes visible

        # Extract all items from the dropdown
        tutorials = page.query_selector_all(".mega-dropdown a")  # Selecting all links

        # Print extracted items
        for item in tutorials:
            print(item.inner_text())

        browser.close()


scrape_tutorials()
