import time

from playwright.sync_api import Page

def test_child_hand(page:Page):
    page.goto("https://omayo.blogspot.com/")
    page.wait_for_load_state('load')
    with page.expect_popup() as C_page:
        page.locator("#selenium143").click()
        page.wait_for_load_state('load')
        child = C_page.value
    child.wait_for_load_state('load')
    links = child.query_selector_all("a")
    for link in links:
        #to get link url
        #href = link.get_attribute("href")
        #to get only link text
        text = link.inner_text().strip()
        #print(f"Link Text :{text}| Href : {href}")
        print(f"Link Text :{text}")

