import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page=context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com")
    page.wait_for_load_state()
    window_ID = id(page)
    print(window_ID)
    with page.expect_popup() as newpage:
        page.get_by_role("link",name="OrangeHRM, Inc").click()
        childpage = newpage.value
        ChildID = id(page)
        print(ChildID)
    childpage.wait_for_load_state()
    childpage.get_by_placeholder("Enter your email address here").fill("anupamk842@gmail.com")


    childpage.close()

    #Parent_page = context.pages[0]
    #Parent_page.bring_to_front()
    #print(Parent_page.title())
    #page=window_ID
    #Parent_page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Username").fill("Admin")
    #Parent_page.get_by_placeholder("Password").fill("admin123")
    page.get_by_placeholder("Password").fill("admin123")

    time.sleep(3)
    page.get_by_role("button", name="Login").click()
    time.sleep(3)
    browser.close()



