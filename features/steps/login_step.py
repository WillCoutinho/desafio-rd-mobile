from behave import step
from hamcrest import assert_that, is_, equal_to
from features.support.credentials import user_data


@step(u'que estou na tela de login')
def login_page(context):
    is_login_page = context.app.login_page.is_login_page()
    assert_that(is_login_page, is_(True),
                "A tela de Login deve ser exibida.")


@step(u'clico no link "New User? Register"')
def click_register_link(context):
    context.app.login_page.new_user_page()
    assert_that(context.app.register_page.is_registration_page(), is_(True),
                "Link 'New User? Register' deve ser exibido em tela.")


@step(u'preencho todos os campos em branco')
def fill_register_fields(context):
    context.app.register_page.fill_register_fields(user_data['name'],
                                                   user_data['phone'],
                                                   user_data['email'],
                                                   user_data['password'])

    assert_that(context.app.register_page.is_all_registration_data_filled(user_data['name'],
                                                                          user_data['phone'],
                                                                          user_data['email'],
                                                                          user_data['password']), is_(True),
                "Dados devem ser preenchidos em todos os campos.")


@step(u'clico no botão "Register"')
def click_register_button(context):
    assert_that(context.app.register_page.is_register_button_displayed(), is_(True),
                "Botão 'Register' deve ser exibido.")

    context.app.register_page.click_register_button()


@step(u'o usuário é criado e permanecemos na tela de cadastro')
def success_register_message(context):
    assert_that(context.app.register_page.is_registration_page(), is_(True),
                "Tela de cadastro deve ser exibida.")


@step(u'preencho os campos com dados já cadastrados')
def valid_login(context):
    context.app.login_page.login(user_data['email'],
                                 user_data['password'])

    assert_that(context.app.login_page.is_all_login_data_filled(user_data['email'],
                                                                user_data['password']), is_(True),
                "Todos os campos devem ser preenchidos corretamente.")


@step(u'clico no botão "Login"')
def click_login_button(context):
    assert_that(context.app.login_page.login_button_is_displayed(), is_(True),
                "Botão 'Login' deve ser exibido.")
    context.app.login_page.click_login_button()


@step(u'a mensagem "{success_message}" é exibida na tela')
def login_success_message(context, success_message):
    assert_that(context.app.login_page.login_message(), equal_to(success_message),
                f"Mensagem '{success_message}' não encontrada.")

    context.driver.back()


@step(u'preencho os campos com dados não cadastrados')
def invalid_login(context):
    context.app.login_page.login(email='teste', password='01020304')
    assert_that(context.app.login_page.is_all_login_data_filled(email='teste', password='01020304'), is_(True),
                "Dados preenchidos não batem com dados enviados.")


@step(u'o login não é realizado e permanecemos na tela de login')
def login_error(context):
    assert_that(context.app.login_page.is_login_page(), is_(True),
                "Tela de Login deve ser exibida.")
