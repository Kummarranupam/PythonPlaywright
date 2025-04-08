import time

from playwright.sync_api import Page

def test_handlechild(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    time.sleep(3)
#this is called as closure. its used for when there is chance for popup to trigger
    with page.expect_popup() as newpage_info: # this a listioner and keep eye on all steps. whenever a new page opens
        # it takes the info and store in object(newpage_info)
        #childpage all activity should be written below this block
        page.locator(".blinkingText").click()
        childpage = newpage_info.value
        text=childpage.locator(".red").text_content()
        print(text)
#to extract the email
        word = text.split("at")
        email = word[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"
