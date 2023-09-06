from features.pages.login.login_page import LoginPage
from features.pages.register.register_page import RegisterPage


class Aplicacao:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.register_page = RegisterPage(driver)