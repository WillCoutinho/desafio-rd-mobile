# language: pt

Funcionalidade: Login
  Como usuário
  Quero poder me registrar e logar
  Assim posso usufruir do app

  @criar_cadastro
  Cenário: Criar cadastro de usuário
    Dado que estou na tela de login
    E clico no link "New User? Register"
    Quando preencho todos os campos em branco
    E clico no botão "Register"
    Então o usuário é criado e permanecemos na tela de cadastro

  @login_valido
  @pre_condicao_cadastro_realizado
  Cenário: Login válido
    Dado que estou na tela de login
    E preencho os campos com dados já cadastrados
    Quando clico no botão "Login"
    Então a mensagem "You are now logged in" é exibida na tela

  @login_invalido
  Cenário: Login inválido
    Dado que estou na tela de login
    E preencho os campos com dados não cadastrados
    Quando clico no botão "Login"
    Então o login não é realizado e permanecemos na tela de login