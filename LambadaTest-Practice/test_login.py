import time

from playwright.sync_api import Page, Playwright
from playwright.sync_api import sync_playwright

def test_launchbrowser(playwright:Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context() # seperate private window, like opening browser in incognito mode
    page = context.new_page()
    page.goto("https://ecommerce-playground.lambdatest.io/")
    page.locator("a.icon-left both nav-link dropdown-toggle").hover()
    time.sleep(5)



with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ecommerce-playground.lambdatest.io/")
    

    #page.waitForTimeout(5000)