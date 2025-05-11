import time

from playwright.sync_api import Playwright
from playwright.sync_api import Page
def test_website(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://money.rediff.com/gainers")
    column_count = len(page.query_selector_all("table.dataTable thead tr th"))
    #print("Total column Size : ", column_count)
    print(f"Total Column Count: {column_count}")

    #row_count = len(page.query_selector_all("table.dataTable tbody tr"))
    rows = page.query_selector_all("table.dataTable tbody tr")
    row_count=len(rows)
    #print("Total Row Size:",row_count)

    print(f"Total Row Count: {row_count}")

    print("\n--- Table Data ---\n")
    for row in rows:
        cells = row.query_selector_all("td")
        row_data = [cell.inner_text().strip() for cell in cells]
        print(" | ".join(row_data))