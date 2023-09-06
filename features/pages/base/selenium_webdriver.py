from selenium.webdriver.common.by import By


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    def get_locator_type(self, tipo_locator):
        """ Retorna por qual método fará a busca: driver.find_element(By.opcao, 'valor que será buscado')
        - Retorna apenas o tipo, não fazendo a busca
        """
        tipo_locator = tipo_locator.lower()

        if tipo_locator == "id":
            return By.ID
        elif tipo_locator == "xpath":
            return By.XPATH
        elif tipo_locator == "name":
            return By.NAME
        elif tipo_locator == "css":
            return By.CSS_SELECTOR
        elif tipo_locator == "class":
            return By.CLASS_NAME
        elif tipo_locator == "link":
            return By.LINK_TEXT
        elif tipo_locator == "tag":
            return By.TAG_NAME
        else:
            print(f"Busca por {tipo_locator} não suportado.")
            return False

    def get_element(self, locator, locator_type="id"):
        """ Realiza a busca do elemento com base no Locator e no tipo de busca
        - Retorna o elemento
        - O tipo de busca default é por 'id'
        """
        try:
            locator_type = locator_type.lower()
            by_type = self.get_locator_type(locator_type)
            return self.driver.find_element(by_type, locator)

        except Exception as e:
            print(f"Elemento '{locator}' não encontrado.")
            print(e)
            return False

    def click_element(self, locator="", locator_type="id", element=None):
        """ Realiza ação de click no elemento (sem retorno)
        - O tipo de busca default é por 'id'
        """
        self.driver.hide_keyboard()
        try:
            if locator != "":
                element = self.get_element(locator, locator_type)
            element.click()
        except Exception as e:
            print(f"Erro ao clicar no elemento {locator}")
            print(e)

    def insert_data_into_element(self, data, locator, locator_type="id"):
        """ Realiza ações de input nos elementos (sem retorno)
       - Recebe como parâmetro os dados que serão inputados, locator e tipo de busca
       - O tipo de busca default é por 'id'
       """
        try:
            by_type = self.get_locator_type(locator_type)
            element = self.get_element(locator, by_type)
            element.click()
            element.send_keys(data)

        except Exception as e:
            print(f"Não foi possível inserir dados no campo {locator}")
            print(e)

    def is_element_displayed(self, locator, locator_type='id'):
        """ Checa se o elemento é mostrado na página
        - Caso o elemento seja enviado, o mesmo é utilizado diretamente
        - Retorna um booleano
        """
        element = None
        self.driver.hide_keyboard()
        try:
            if locator != '':
                element = self.get_element(locator, locator_type)

            if element is not None:
                return element.is_displayed()
            else:
                print(f'Elemento {locator} não encontrado ou nulo')

        except Exception as e:
            print(e)
            return False