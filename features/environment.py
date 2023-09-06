from app.aplicacao import Aplicacao
from appium import webdriver


def before_all(context):
    context.driver = webdriver.Remote("http://127.0.0.1:4723",
                                      desired_capabilities={
                                          "project": "Desafio RD",
                                          'platformName': 'Android',
                                          'automationName': 'uiautomator2',
                                          "deviceName": "emulator-5554",
                                          "app": ".apk/app-debug.apk",
                                          "appPacakge": "com.example.vamsi.login",
                                          "appActivity": "com.example.vamsi.login.MainActivity",
                                          "noReset": "true",
                                          "newCommandTimeout": 3600,
                                      })

    context.driver.implicitly_wait(10)
    context.app = Aplicacao(context.driver)


# def before_scenario(context, scenario):
#     context.driver.launch_app()
#

# def before_tag(context, tag):
#     if tag == 'pre_condicao_cadastro_realizado':
#         from features.support.credentials import login_scenario
#
#         context.driver.close_app()
#         context.driver.launch_app()
#         context.app.login_page.new_user_page()
#         context.app.register_page.fill_register_fields(login_scenario['name'],
#                                                        login_scenario['phone'],
#                                                        login_scenario['email'],
#                                                        login_scenario['password'])
#         context.app.register_page.click_register_button()
#         context.app.register_page.click_login_button()


def after_all(context):
    context.driver.close_app()