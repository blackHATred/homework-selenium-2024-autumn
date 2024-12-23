import os

import pytest
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait

from hw.code.conftest import Config
from hw.code.ui.pages.index_page import IndexPage
from hw.code.ui.pages.leadform_page import LeadFormsPage
from hw.code.ui.pages.register_page import RegisterPage
from hw.code.ui.pages.settings_page import SettingsPage, NotificationSettingsPage, AccessSettingsPage, LogsSettingsPage
from hw.code.ui.pages.surveys_page import SurveysPage
from hw.code.ui.pages.campaign_page import CampaignPage
from hw.code.ui.pages.commerce_center_page import CommerceCenterPage


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
def authorized_user(driver, index_page, credentials):
    # Фикстура для авторизованного через VK ID пользователя (необязательно зарегистрированного)
    driver.get(IndexPage.url)
    WebDriverWait(driver, 10).until(lambda d: d.current_url.rstrip('/') in (
        Config.VK_ADS_OVERVIEW_URL,
        Config.VK_ADS_REGISTER_URL,
        Config.VK_ADS_URL,
    ))
    if Config.VK_ADS_OVERVIEW_URL in driver.current_url or Config.VK_ADS_REGISTER_URL in driver.current_url:
        # Пользователь авторизован
        return IndexPage(driver)
    # Пользователь авторизован, но не зарегистрирован
    page = IndexPage(driver)
    page.login(credentials)
    page.wait(10).until(lambda d: d.current_url in (Config.VK_ADS_OVERVIEW_URL, Config.VK_ADS_REGISTER_URL))
    return page


@pytest.fixture
def registered_user(driver, authorized_user, credentials):
    # Фикстура для зарегистрированного пользователя
    driver.get(IndexPage.url)
    # Откроется либо страница регистрации, либо главная страница ЛК
    WebDriverWait(driver, 5).until(lambda d: d.current_url.rstrip('/') in (
        Config.VK_ADS_OVERVIEW_URL,
        Config.VK_ADS_REGISTER_URL,
        Config.VK_ADS_URL,
    ))
    reg_page = RegisterPage(driver)
    if Config.VK_ADS_OVERVIEW_URL not in driver.current_url:
        # Пользователь не зарегистрирован, регистрируем его
        reg_page.register(credentials)
    return reg_page


@pytest.fixture
def settings_page(driver, registered_user):
    return SettingsPage(driver)


@pytest.fixture
def notification_settings_page(driver, registered_user):
    return NotificationSettingsPage(driver)


@pytest.fixture
def access_settings_page(driver, registered_user):
    return AccessSettingsPage(driver)


@pytest.fixture
def logs_settings_page(driver, registered_user):
    return LogsSettingsPage(driver)


@pytest.fixture
def lead_forms_page(driver, registered_user):
    return LeadFormsPage(driver)


@pytest.fixture
def surveys_page(driver, registered_user):
    return SurveysPage(driver)


@pytest.fixture
def register_page(driver, authorized_user, credentials):
    # Фикстура authorized_user гарантирует, что пользователь авторизован, но нужно проверить, зарегистрирован ли он

    driver.get(Config.VK_ADS_CABINET_URL)
    # Может открыться одна из страниц
    WebDriverWait(driver, 15).until(
        lambda d: any((
            Config.VK_ADS_OVERVIEW_URL in d.current_url,
            Config.VK_ADS_REGISTER_URL in d.current_url,
        ))
    )
    # Если открылась страница регистрации, то возвращаем ее
    if Config.VK_ADS_REGISTER_URL in driver.current_url:
        return RegisterPage(driver)
    # Если пользователь не удален, то удаляем его
    SettingsPage(driver).delete_account()
    # Заново входим через mail ru
    IndexPage(driver).login(credentials)
    driver.get(RegisterPage.url)
    return RegisterPage(driver)

@pytest.fixture
def campaign_page_with_deleted_campaign(driver, campaign_page):
    driver.get(Config.VK_ADS_CAMPAIGN_URL)
    # удалим кампанию, если она есть
    campaign_page.delete_campaign_if_exists()
    return CampaignPage(driver)

@pytest.fixture
def campaign_page(driver, authorized_user):
    driver.get(CampaignPage.url)
    return CampaignPage(driver)

@pytest.fixture
def commerce_center(driver, commerce_center_page):
    driver.get(Config.VK_ADS_COMMERCE_CENTER_URL)
    # удалим кампанию, если она есть
    commerce_center_page.delete_catalog_if_exists()
    return CommerceCenterPage(driver)

@pytest.fixture
def commerce_center_page(driver, authorized_user):
    driver.get(CommerceCenterPage.url)
    return CommerceCenterPage(driver)