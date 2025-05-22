
from playwright.sync_api import sync_playwright



# def get_links_tittle():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless = False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://omayo.blogspot.com/")
#         page.wait_for_load_state()
#         print(page.title())
#         links = page.query_selector_all("a")
#         for link in links:
#             href = link.get_attribute("href")
#             if href:
#                 print(href)
#
#         browser.close()
# get_links_tittle()