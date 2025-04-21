from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


# we will bypass login and perform other activity


def test_sessiontokenlogin(playwright : Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    #script to get token and add it in local storage
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()





