import time

from hw.code.conftest import Config
from hw.code.ui.locators.auth import AuthLocators
from hw.code.ui.locators.index import IndexLocators
from hw.code.ui.pages.base_page import BasePage, PageNotOpenedException
from selenium.webdriver.support import expected_conditions as EC


class IndexPage(BasePage):
    url = Config.VK_ADS_URL
    vkid_logged_in = Config.VK_ID_LOGGED_IN
    mailru_logged_in = Config.MAIL_RU_LOGGED_IN

    def click_go_to_cabinet_button(self):
        self.click(IndexLocators.GO_TO_CABINET_BUTTON)
        self.wait(10).until(EC.url_contains(Config.VK_ID_URL))

    def login(self, credentials):
        if IndexPage.vkid_logged_in:
            # Если уже авторизованы, то повторно входить не нужно
            return
        # Входим в VK ADS через Mail ru oauth
        self.click(IndexLocators.GO_TO_CABINET_BUTTON)
        self.click(AuthLocators.MAIL_RU_OAUTH_OPTION_BUTTON)
        if IndexPage.mailru_logged_in:
            # Если уже авторизованы, то повторно входить не нужно
            return
        self.fill_field(AuthLocators.EMAIL_INPUT, credentials['login'])
        self.click(AuthLocators.NEXT_BUTTON)
        self.click(AuthLocators.AUTH_PROBLEMS_BUTTON)
        self.click(AuthLocators.USE_PASSWORD_BUTTON)
        self.fill_field(AuthLocators.PASSWORD_INPUT, credentials['password'])
        self.click(AuthLocators.SUBMIT_BUTTON)
        IndexPage.mailru_logged_in = True

        # Может открыться одна из двух страниц, поэтому обрабатываем открытие следующей страницы не через is_opened()
        timeout = 60  # c поправкой на возможную капчу
        started = time.time()
        while time.time() - started < timeout:
            # Может открыться страница регистрации или сразу ЛК
            if self.driver.current_url.rstrip('/') in (Config.VK_ADS_REGISTER_URL, Config.VK_ADS_OVERVIEW_URL):
                IndexPage.vkid_logged_in = True
                return
        raise PageNotOpenedException(f'auth did not completed in {timeout} sec, current url {self.driver.current_url}')
