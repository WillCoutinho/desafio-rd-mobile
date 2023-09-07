from features.pages.base.selenium_webdriver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    email_field = 'com.example.vamsi.login:id/etLogGmail'
    password_field = 'com.example.vamsi.login:id/etLoginPassword'
    login_button = 'com.example.vamsi.login:id/btnLogin'
    login_register_button = 'com.example.vamsi.login:id/btnGotoLogin'
    register_link = 'com.example.vamsi.login:id/tvRegister'
    logged_message_txt = "//android.widget.TextView[@text='You are now logged in']"
    login_title = "//android.widget.TextView[@text='Login']"

    def fill_email_field(self, email):
        self.insert_data_into_element(email, self.email_field, locator_type="id")

    def fill_password_field(self, senha):
        self.insert_data_into_element(senha, self.password_field, locator_type="id")

    def click_login_button(self):
        self.click_element(self.login_button, locator_type='id')

    def login(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)

    def login_message(self):
        return self.get_element(self.logged_message_txt, locator_type='xpath').text

    def is_login_page(self):
        if self.is_element_displayed(self.login_title, locator_type='xpath'):
            # element = self.get_element(self.login_title, locator_type='xpath')
            return True

        if self.is_element_displayed(self.login_register_button, locator_type='id'):
            self.click_element(self.login_register_button, locator_type='id')
            element = self.get_element(self.login_title, locator_type='xpath')

            if element is not None and element.text == 'Login':
                return True

        return False

    def new_user_page(self):
        self.click_element(self.register_link, locator_type='id')

    def is_all_login_data_filled(self, email, password):
        fields = [self.email_field, self.password_field]
        values = [email, password]
        correct_data = False
        for field in fields:
            for value in values:
                if value in self.get_element(field, locator_type='id').text:
                    correct_data = True

        return correct_data

    def login_button_is_displayed(self):
        return self.is_element_displayed(self.login_button, locator_type='id')
