import json

import pytest
from playwright.sync_api import Page, Playwright, expect

from pageObjects.dashboard import DashboardPage
from pageObjects.login import LoginPage

#from .pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

#create Json file with credentials --> utils --> this will convert my json file to python
# object(convert data into list or dictionaries) then access into test

with open("data/credentials.json") as f:
    test_data = json.load(f)  # load will convert json file to python object
    print(test_data)
    user_credentials_list = test_data["user_credentials"]  # there are 2 credentials set...
    # we have to make it run how many credentials are there that many times

@pytest.mark.parametrize('user_credentials',user_credentials_list)# Parameterize does the iteration of all elements present under
# 'user_credentials_list' from the external json data
# every pytest function takes fixture as argument and fixtures are executed first before test

def test_orderonewebapi(playwright:Playwright, user_credentials, browserInstance):
    userName = user_credentials["userEmail"]
    Password = user_credentials["userPassword"]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create Order ---- order ID
# if you want to call any method of class then first create object of class and then using that object call the method
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    # Login
    loginPage = LoginPage(browserInstance)# whenever we create object of class its constructor will be called automatically
    loginPage.navigate()
    dashboardPage = loginPage.login(userName,Password)
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    ordersDetailsPage = orderHistoryPage.selectOrder(orderId)
    ordersDetailsPage.verifyOrderMessage()

    context.close()


#Order history page and verify order id is present
# to_have_text searches exact text and to_contain searches partial
