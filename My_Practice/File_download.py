from playwright.sync_api import sync_playwright
import os

def download_file_to_custom_path():
    download_dir = "D:/Downloads"  # 👈 Set your custom download directory

    # Make sure the folder exists
    os.makedirs(download_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        # Create a browser context with downloads enabled
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        # Go to the page with the download link
        page.goto("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")

        # Wait for the download to be triggered
        with page.expect_download() as download_info:
            page.click("a[href*='file_example_PDF_1MB.pdf']")  # Replace selector as needed

        # Get the download object
        download = download_info.value

        # Save the file to your custom path
        file_path = os.path.join(download_dir, download.suggested_filename)
        download.save_as(file_path)

        print(f"✅ File downloaded to: {file_path}")
        browser.close()

download_file_to_custom_path()
