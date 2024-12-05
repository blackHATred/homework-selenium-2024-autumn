import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait

from hw.code.conftest import Config
from hw.code.ui.pages.index_page import IndexPage
from hw.code.ui.pages.register_page import RegisterPage
from hw.code.ui.pages.settings_page import SettingsPage, NotificationSettingsPage, AccessSettingsPage


@pytest.fixture(scope='session')
def credentials() -> dict:
    load_dotenv()
    return {
        'login': os.getenv('LOGIN'),
        'password': os.getenv('PASSWORD')
    }


@pytest.fixture
def index_page(driver):
    return IndexPage(driver)


@pytest.fixture
def auth_page(driver):
    return IndexPage(driver)


@pytest.fixture
def authorized_user(driver, auth_page, credentials):
    # Фикстура для авторизованного через VK ID пользователя (необязательно зарегистрированного)
    driver.get(IndexPage.url)
    auth_page.login(credentials)
    return IndexPage(driver)


@pytest.fixture
def registered_user(driver, authorized_user, credentials):
    # Фикстура для зарегистрированного пользователя
    driver.get(RegisterPage.url)
    reg = RegisterPage(driver)
    reg.open()
    # Откроется либо страница регистрации, либо главная страница ЛК
    WebDriverWait(driver, 5).until(lambda d: d.current_url.rstrip('/') in (Config.VK_ADS_OVERVIEW_URL, Config.VK_ADS_REGISTER_URL))
    if driver.current_url.rstrip('/') == Config.VK_ADS_OVERVIEW_URL:
        return reg
    reg.register(credentials)
    return reg


@pytest.fixture
def settings_page(driver, registered_user):
    driver.get(SettingsPage.url)
    return SettingsPage(driver)


@pytest.fixture
def notification_settings_page(driver, registered_user):
    driver.get(NotificationSettingsPage.url)
    return NotificationSettingsPage(driver)


@pytest.fixture
def access_settings_page(driver, registered_user):
    driver.get(AccessSettingsPage.url)
    return AccessSettingsPage(driver)


@pytest.fixture
def register_page(driver, settings_page, auth_page, credentials):
    driver.get(Config.VK_ADS_CABINET_URL)
    # Может открыться одна из страниц
    WebDriverWait(driver, 5).until(
        lambda d: any((
            Config.VK_ADS_OVERVIEW_URL in d.current_url,
            Config.VK_ADS_DASHBOARD_URL in d.current_url,  # тот же OVERVIEW, но предлагает пройти обучение по ЛК
            Config.VK_ADS_REGISTER_URL in d.current_url,
        ))
    )
    if driver.current_url.rstrip('/') == Config.VK_ADS_REGISTER_URL:
        return RegisterPage(driver)
    # Если пользователь не удален, то удаляем его
    settings_page.delete_account()
    # Заново входим через mail ru
    auth_page.login(credentials)
    return RegisterPage(driver)
