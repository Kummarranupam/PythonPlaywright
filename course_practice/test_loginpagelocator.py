import time

from playwright.sync_api import Page, expect


def test_loginpage(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("rahulshettyacademy")
    page.locator("#password").fill("learning")
# give wrong credentials to validate the error message
    #page.locator("#password").fill("earning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#signInBtn").click()
# To validate the error message
    #expect(page.get_by_text("Incorrect username/password.")).to_be_visible()



