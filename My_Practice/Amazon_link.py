from playwright.sync_api import sync_playwright

def get_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Launching Chromium browser in headless mode
        page = browser.new_page()
        page.goto("https://www.amazon.in")  # Navigate to Amazon India

        # Extract all links and their attributes
        links = page.query_selector_all("a")
        print(len(links))
        for link in links:
            href = link.get_attribute("href")
            text = link.inner_text().strip()
            print(f"Link Text: {text} | Href: {href}")

        browser.close()

# Run the function
get_links()