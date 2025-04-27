from playwright.sync_api import sync_playwright
import os

# Create a sample file to upload

with open("Sample_text1", "w") as f:
    f.write("This is a sample file for Playwright upload test2.")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=True to run without UI
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the file upload demo site
    page.goto("https://the-internet.herokuapp.com/upload")

    # Upload the file
    page.set_input_files("input#file-upload", "Sample_text1")

    # Click the upload button
    page.click("input#file-submit")

    # Wait for the upload confirmation
    page.wait_for_selector("h3")  # "File Uploaded!" header

    print("Upload successful!")

    browser.close()

# Clean up (optional)
os.remove("Sample_text")
