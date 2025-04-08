from .dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page # attaching the page to the local class reference- self.page


    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self, userEmail, userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.get_by_role("button", name="Login").click()
#when we clearly know that we will land on this page then we can use the next page method in same page
        dashboardPage = DashboardPage(self.page)
        return dashboardPage

