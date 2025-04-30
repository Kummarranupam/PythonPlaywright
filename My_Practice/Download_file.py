from playwright.sync_api import sync_playwright


def download_file():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the page with the download link
        page.goto("https://example.com/download")

        # Start the download process
        with page.expect_download() as download_info:
            page.click("a#download-link")  # Update the selector based on your page
            download = download_info.value

        # Save the downloaded file
        file_path = f"downloads/{download.suggested_filename}"
        download.save_as(file_path)

        print(f"File downloaded to {file_path}")

        browser.close()


download_file()
