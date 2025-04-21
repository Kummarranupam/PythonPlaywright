from playwright.sync_api import Playwright



orderPayload = {"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}
loginPayload = {"userEmail":"rahulshetty@gmail.com","userPassword":"Iamking@000"}


class APIUtils:

    def getToken(self,playwright:Playwright):

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data=loginPayload)
        assert  response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]



    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)  # when we are calling any method then we should also pass parameter if there
        api_request_context = playwright.request.new_context(base_url ="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=orderPayload,
                                            headers={"Content-Type": "application/json",
                                                     "Authorization" : token })
        print(response.json())
        response_body = response.json()
        order_Id = response_body["orders"][0]
        return order_Id
