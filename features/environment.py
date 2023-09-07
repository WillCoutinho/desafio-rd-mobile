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


def after_all(context):
    context.driver.close_app()