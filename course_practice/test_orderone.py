import time

from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils





def test_orderonewebapi(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create Order ---- order ID
# if you want to call any method of class then first create object of class and then using that object call the method
    api_Utils = APIUtils()
    order_Id = api_Utils.createOrder(playwright)

    # Login
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()


#Order history page and verify order id is present

    row = page.locator("tr").filter(has_text=order_Id)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    # to_have_text searches exact text and to_contain searches partial
