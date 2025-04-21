#How to moke order ID from different account and get the unauthorized message displayed
#api call from browser --> api call contact server before that we are mocking the request url
import time

from playwright.sync_api import Page

def interceptRequest(route):
    route.continue_(url = "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=67eb9578fc76541aad1a4b95")


def test_network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client/")
#create listener for the event
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)
   


