import time

from playwright.sync_api import Page, expect


def test_handlingframes (page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageframe = page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link", name="All Access plan").click()
    time.sleep(5)
    #To verify any text in the page. give body , its for all page
    expect(pageframe.locator("body")).to_contain_text("Join 13,522 Happy Subscibers!")

