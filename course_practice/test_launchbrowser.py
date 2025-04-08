
from playwright.sync_api import Page


def test_launchbrowser(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context() # seperate private window, like opening browser in incognito mode
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")

# if only want to run test in Chrome or Edge then use directly page fixture(page) - class(Page)

def test_playwrightshortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/")
     

    
