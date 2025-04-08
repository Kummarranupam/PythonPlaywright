import time

from playwright.sync_api import Page, expect


def test_radiobutton(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("//input[@value='radio1']").click()

#test_textplaceholder
    page.get_by_placeholder("Type to Select Countries").fill("India")# how to select from suggestion?
#dropdown...after clicking option display
    page.get_by_role("combobox").select_option("option2")
#Checkbox
    page.locator("#checkBoxOption2").check()
    time.sleep(5)
#OPen Window
    #page.locator("#openwindow").click()
    #page.get_by_role("button", name="Open Window").click()
#OPen Tab
    #page.locator("#opentab").click()

#Alertbox......need to check again  a function without name is called anonmous function =
    page.on("dialog", lambda dialog: dialog.accept())  #to cancel what we need to do?
    page.get_by_role("button", name="Confirm").click()
    time.sleep(4)

#Hide and Show
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)

#Mousehover

    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()



    

    