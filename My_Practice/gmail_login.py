import csv
from playwright.sync_api import sync_playwright
import time

# 🔹 Read test data from CSV
def read_test_data(file_path):  # Take file_path as a parameter
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)  # Returns a list of dicts: [{"username": "admin", "password": "admin123"}, ...]

# 🔹 Perform login & logout on the test site
def login_logout(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch browser (headless=False for visualization)
        page = browser.new_page()

        # Navigate to the login page
        page.goto("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)
        # Fill login form
        page.fill("#username", username)
        page.fill("#password", password)
        page.click("#submit")

        # Wait for login to complete (wait for the URL change after login)
        page.wait_for_url("**/logged-in-successfully/")

        print(f"✅ Logged in as {username}")
        time.sleep(5)
        # Click logout button (logout link on the page)
        page.click("a[href='https://practicetestautomation.com/practice-test-login/']")
        print("🚪 Logged out.")

        time.sleep(2)  # Pause for a bit
        browser.close()  # Close the browser

# 🔹 Main: Run test for each user in CSV
test_data = read_test_data(r"D:\gmail_login1.csv")  # Ensure the path is correct and properly formatted
for user in test_data:
    login_logout(user["username"], user["password"])
print("Execution successful")
