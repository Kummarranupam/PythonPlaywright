import time

from playwright.sync_api import Page, expect


def test_loginpage(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("rahulshettyacademy")
    page.locator("#password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#signInBtn").click()
    iphone= page.locator("app-card").filter(has_text="iphone X")
    iphone.get_by_role("button").click()
    nokia = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)

