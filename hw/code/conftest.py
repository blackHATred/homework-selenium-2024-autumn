import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Config:
    VK_ID_URL = 'https://id.vk.com'
    VK_ADS_URL = 'https://ads.vk.com'
    VK_EXPERT_URL = 'https://expert.vk.com'
    VK_ADS_CABINET_URL = f'{VK_ADS_URL}/hq'
    MAIL_RU_URL = 'https://mail.ru'
    VK_ADS_OVERVIEW_URL = f'{VK_ADS_CABINET_URL}/overview'
    VK_ADS_DASHBOARD_URL = f'{VK_ADS_CABINET_URL}/dashboard'
    VK_ADS_REGISTER_URL = f'{VK_ADS_CABINET_URL}/registration'
    VK_ADS_REGISTER_NEW_URL = f'{VK_ADS_REGISTER_URL}/new'
    VK_ADS_SETTINGS_URL = f'{VK_ADS_CABINET_URL}/settings'
    VK_ADS_SETTINGS_NOTIFICATIONS_URL = f'{VK_ADS_SETTINGS_URL}/notifications'
    VK_ADS_SETTINGS_ACCESS_URL = f'{VK_ADS_SETTINGS_URL}/access'
    VK_ADS_SETTINGS_LOGS_URL = f'{VK_ADS_SETTINGS_URL}/logs'
    VK_ADS_LEADFORMS_URL = f'{VK_ADS_CABINET_URL}/leadads/leadforms'
    VK_ADS_SURVEYS_URL = f'{VK_ADS_CABINET_URL}/leadads/surveys'

    USER_DATA_DIR = os.getenv('USER_PROFILE_DIR', None)
    USER_PROFILE_DIR = os.getenv('PROFILE_NAME', None)
    VK_ID_LOGGED_IN = USER_DATA_DIR is not None
    MAIL_RU_LOGGED_IN = USER_DATA_DIR is not None
    VK_ADS_CAMPAIGN_URL = f'{VK_ADS_CABINET_URL}/dashboard'
    VK_ADS_CAMPAIGN_CREATE_URL = f'{VK_ADS_CABINET_URL}/new_create/ad_plan'
    VK_ADS_COMMERCE_CENTER_URL = f'{VK_ADS_CABINET_URL}/ecomm/catalogs'

    CLICK_RETRIES = 3
    FILL_RETRIES = 3

    ASSETS_DIR = 'B:/Projects/homework-selenium-2024-autumn/assets'


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default=Config.VK_ADS_URL)
    parser.addoption('--headless', action='store_true')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    headless = request.config.getoption('--headless')
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': selenoid,
        'vnc': vnc,
        'headless': headless
    }


@pytest.fixture(scope='session')
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if Config.USER_DATA_DIR is not None:
        # Используем готовый профиль Chrome, где уже выполнена авторизация
        options.add_argument(rf'--user-data-dir={Config.USER_DATA_DIR}')
        options.add_argument(f'--profile-directory={Config.USER_PROFILE_DIR}')
        Config.VK_ID_LOGGED_IN = True
        Config.MAIL_RU_LOGGED_IN = True
    if config['headless']:
        options.add_argument('--headless')
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    # Замедляем скорость интернета, чтобы не ловить ошибки из-за ограничений на кол-во запросов
    driver.set_network_conditions(
        offline=False,
        latency=5,
        download_throughput=500 * 1024,
        upload_throughput=500 * 1024,
    )
    driver.maximize_window()
    yield driver
    driver.quit()
