import time

from hw.code.conftest import Config
from hw.code.ui.locators.auth import AuthLocators
from hw.code.ui.locators.index import IndexLocators
from hw.code.ui.pages.base_page import BasePage, PageNotOpenedException


class IndexPage(BasePage):
    url = Config.VK_ADS_URL
    logged_in = False

    def login(self, credentials):
        # Входим в VK ADS через Mail ru oauth
        self.click(IndexLocators.GO_TO_CABINET_BUTTON)
        self.click(AuthLocators.MAIL_RU_OAUTH_OPTION_BUTTON)
        if IndexPage.logged_in:
            # Если в рамках сессии уже авторизовались в Mail ru, то не нужно вводить логин и пароль повторно
            return
        self.fill_field(AuthLocators.EMAIL_INPUT, credentials['login'])
        self.click(AuthLocators.NEXT_BUTTON)
        self.click(AuthLocators.AUTH_PROBLEMS_BUTTON)
        self.click(AuthLocators.USE_PASSWORD_BUTTON)
        self.fill_field(AuthLocators.PASSWORD_INPUT, credentials['password'])
        self.click(AuthLocators.SUBMIT_BUTTON)

        # Может открыться одна из двух страниц, поэтому обрабатываем открытие следующей страницы не через is_opened()
        timeout = 30
        started = time.time()
        while time.time() - started < timeout:
            # Может открыться страница регистрации или сразу ЛК
            if self.driver.current_url.rstrip('/') in (Config.VK_ADS_REGISTER_URL, Config.VK_ADS_OVERVIEW_URL):
                IndexPage.logged_in = True
                return
        raise PageNotOpenedException(f'auth did not completed in {timeout} sec, current url {self.driver.current_url}')