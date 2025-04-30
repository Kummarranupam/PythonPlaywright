import csv
import time
import logging
from playwright.sync_api import sync_playwright

# 🔹 Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


# 🔹 Read test data from CSV
def read_test_data(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            logger.info("CSV file loaded successfully.")
            return list(reader)  # List of dicts: [{"username": ..., "password": ...}]
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        raise  # Reraise the exception after logging


# 🔹 Login & Logout using credentials
def login_logout(username, password):
    try:
        logger.info(f"Starting login process for user: {username}")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)  # Set headless=True to hide the browser window
            page = browser.new_page()

            # Visit login page
            logger.info("Visiting login page...")
            page.goto("https://practicetestautomation.com/practice-test-login/")

            # Fill credentials and submit
            logger.info(f"Entering credentials for {username}...")
            page.fill("#username", username)
            page.fill("#password", password)
            page.click("#submit")

            logger.info(f"Clicking submit button for {username}...")

            try:
                # Wait for login success page
                logger.info("Waiting for successful login URL...")
                page.wait_for_url("**/logged-in-successfully/", timeout=10000)  # Increased timeout to 10 seconds
                logger.info(f"✅ Logged in successfully as {username}")

                # Click logout link
                logger.info("Clicking the logout button...")
                page.click("a[href='https://practicetestautomation.com/practice-test-login/']")
                logger.info("🚪 Logged out successfully.")

            except Exception as e:
                logger.error(f"❌ Login failed for {username}. Error: {e}")
                raise  # Reraise the exception after logging

            time.sleep(2)  # Wait before closing browser
            browser.close()

    except Exception as e:
        logger.error(f"An error occurred during login/logout for {username}: {e}")
        # You can add additional error handling here if needed, like retrying the operation


# 🔹 Main runner
if __name__ == "__main__":
    try:
        test_data = read_test_data(r"D:\gmail_login1.csv")
        logger.info(f"Found {len(test_data)} users to test.")
        for user in test_data:
            login_logout(user["username"], user["password"])
    except Exception as e:
        logger.critical(f"Critical error: {e}")
