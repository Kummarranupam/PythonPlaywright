from playwright.sync_api import sync_playwright
import openpyxl

# Load Excel data
excel = openpyxl.load_workbook('your_data.xlsx')
sheet = excel.active

data = []
for row in sheet.rows:
    row_data = [cell.value for cell in row]
    data.append(row_data)

# Launch Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Navigate to the testing website
    page.goto('https://example.com')

    # Perform automation tasks with the data
    for item in data:
        username, password = item  # Assuming each item is a list with a username and password
        page.fill('input#username', username)
        page.fill('input#password', password)
        page.click('button#login')
        print(f"Tested with {username} and {password}")

    browser.close()