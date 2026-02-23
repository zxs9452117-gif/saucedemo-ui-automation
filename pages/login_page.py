from pages.base_page import BasePage
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._username = "id=user-name"
        self._password = "id=password"
        self._login_btn = "id=login-button"

    def login(self, user, pwd):
        self.fill_input(self._username, user)
        self.fill_input(self._password, pwd)
        self.click_element(self._login_btn)