import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Config:
    VK_ID_URL = 'https://id.vk.com'
    VK_ADS_URL = 'https://ads.vk.com'
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

    CLICK_RETRIES = 3


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
    driver.get(url)
    yield driver
    driver.quit()
