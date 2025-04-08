from playwright.sync_api import Page


def test_childpage(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newpage:
        page.locator(".blinkingText").click()
        childpager = newpage.value
        text=childpager.locator(".red").text_content()
        #print(text)
        text1 = text.split("at")
        email = text1[1].strip().split(" ")[0]
        print(email)
        assert  email=="mentor@rahulshettyacademy.com"





