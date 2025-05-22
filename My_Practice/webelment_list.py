from playwright.sync_api import sync_playwright


def launch_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://omayo.blogspot.com/")
        page.wait_for_load_state('load')
        print(page.title())
        # links = page.query_selector_all('a')
        # for link in links:
        #     href = link.get_attribute("href")
        #     text = link.inner_text().strip()
        #     print(f"Link text: {text} | Href : {href}")
        page.locator("#home").click()
        #page.hover("text =Blogs")
        page.hover("text=Blogs")
        page.wait_for_timeout(5)
        # Extract and print list items
        #blog_list = page.query_selector_all("//li[@class = 'has-sub']//li//span")
        blog_list = page.query_selector_all(".has-sub li a")
        for blog in blog_list:
            print(blog.inner_text())

        #option1= page.select_option("#multiselect1, Swift")
        #option1 = page.locator("#multiselect1").select_option("Swift")
        # selected_values = page.locator("#multiselect1").evaluate(
        #     "element => Array.from(element.selectedOptions).map(opt => opt.value)")

        # print("Selected values:", selected_values)
        # Wait for the multi-select box to be visible
        page.wait_for_selector("select#multiselect1")

        # Select the 'Swift' option
        pik=page.select_option("select#multiselect1", label="Swift")
        #selected_values = page.locator("#multiselect1").evaluate("element => Array.from"
                                                                 #"(element.selectedOptions).map(opt => opt.value)")

        print(pik)
        page.wait_for_load_state('load')
        #page.get_by_role("combobox").select_option("ghi")
        page.locator("#drop1").select_option("doc 2")  # Using 'doc2' as the value

        # Print selected value for verification
        selected_value = page.locator("#drop1").input_value()
        print("Selected Option:", selected_value)
        page.wait_for_load_state('load')



launch_browser()








