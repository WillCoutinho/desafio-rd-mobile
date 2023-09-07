# Desafio RD - Automação Mobile

Cenários de teste para automação do app que está na pasta .apk deste projeto.
A documentação deste projeto foi feita considerando que quem for rodá-lo está ciente de como preparar o 
ambiente, bastando informar os pré-requisitos.


### Pré-requisitos:

- GIT: https://git-scm.com/download/win
- Python: https://www.python.org/downloads/
- Android Studio (emulador): https://developer.android.com/studio
- NodeJS (Appium): https://nodejs.org/pt-br/download
- Appium: https://appium.io/
- Allure para o report: https://github.com/allure-framework/allure2/releases
- Configuração do Allure: https://docs.qameta.io/allure/#_get_started
- Lib Pipenv: https://pipenv.pypa.io/en/latest/installation/#installing-pipenv


### Instalação - Passo a Passo:

Preparado o ambiente com os pré-requisitos, clone o repositório deste projeto.  
Inicie um ambiente virtual com ``pipenv shell``  
Faça as instalações das libs pelo pipenv: ``pipenv install``  
Inicie um emulador no Android Studio e instale o _.apk_        

### Iniciando os Cenários
Abra um terminal e inicie o Appium Server: ``appium``  
Em um segundo terminal inicie o emulador do Android Studio: ``emulator -avd nome_do_emulador``
>*Nota*: Caso não tenha configurado corretamente o Android Studio e suas variáveis de ambiente, 
> basta abri-lo e iniciar o emulador através dele.  
 
Em um terceiro terminal onde o ambiente virtual do _Pipenv_ foi iniciado com as libs instaladas, 
rode o comando abaixo para executar os testes

Os parâmetros deste comando são:\
``--lang=pt``: língua utilizada nos arquivos ``.feature``\
``-f allure_behave.formatter:AllureFormatter``: formato que vamos utilizar na saída (_Allure Framework_)\
``-o allure_result_folder``: pasta onde será salvo a saída do teste\
``./features``: features que serão executadas
       
````bash
behave --lang=pt -f allure_behave.formatter:AllureFormatter -o allure_result_folder ./features
````

Após os testes serem executados, usamos o comando abaixo para gerar o relatório.
O comando criará um servidor local que vai ler os arquivos em ``allure_result_folder`` e lançará os resultados no browser:
````bash
allure serve allure_result_folder
````

##
#### Libs utilizadas

* [Behave](https://pypi.org/project/behave/#description) - BDD com suporte ao Python
* [Allure-Behave](https://pypi.org/project/allure-behave/#description) - Framework para gerar reports
* [Pipenv](https://pypi.org/project/pipenv/#description) - Package/VirtualEnv manager 
* [Selenium](https://pypi.org/project/selenium/#description) - API WebDriver
* [Appium Python Client](https://pypi.org/project/Appium-Python-Client/#description) - Extensão para teste mobile
* [HamCrest](https://pyhamcrest.readthedocs.io/en/latest/) - Lib para asserções
