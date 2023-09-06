from features.pages.base.selenium_webdriver import SeleniumDriver


class RegisterPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    name_field = 'com.example.vamsi.login:id/etRegName'
    phone_field = 'com.example.vamsi.login:id/etRegPhone'
    email_field = 'com.example.vamsi.login:id/etRegGmail'
    password_field = 'com.example.vamsi.login:id/etRegPassword'
    register_btn = 'com.example.vamsi.login:id/btnRegLogin'
    login_btn = 'com.example.vamsi.login:id/btnGotoLogin'
    logged_message_txt = "//android.widget.TextView[@text='You are now logged in']"
    register_title = "//android.widget.TextView[@text='Registration']"

    def fill_name_field(self, name):
        self.insert_data_into_element(name, self.name_field, locator_type="id")

    def fill_phone_field(self, phone):
        self.insert_data_into_element(phone, self.phone_field, locator_type="id")

    def fill_email_field(self, email):
        self.insert_data_into_element(email, self.email_field, locator_type="id")

    def fill_password_field(self, password):
        self.insert_data_into_element(password, self.password_field, locator_type="id")

    def click_login_button(self):
        self.click_element(self.login_btn, locator_type="id")

    def click_register_button(self):
        self.click_element(self.register_btn, locator_type='id')

    def fill_register_fields(self, name, phone, email, password):
        self.fill_name_field(name)
        self.fill_phone_field(phone)
        self.fill_email_field(email)
        self.fill_password_field(password)

    def is_registration_page(self):
        element = self.get_element(self.register_title, 'xpath')
        if element is not None and element.text == 'Registration':
            return True
        else:
            return False

    def is_all_registration_data_filled(self, nome='Tester', telefone='00000', email='tester@qa.com', senha='1234'):
        fields = [self.name_field, self.phone_field, self.email_field, self.password_field]
        values = [nome, telefone, email, senha]
        correct_data = False
        for field in fields:
            for value in values:
                if value in self.get_element(field, locator_type='id').text:
                    correct_data = True

        return correct_data

    def is_register_button_displayed(self):
        return self.is_element_displayed(self.register_btn, locator_type='id')