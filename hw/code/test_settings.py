import random
import string

from hw.code.base import BaseCase
from selenium.webdriver.support import expected_conditions as EC

from hw.code.fixtures import *
from hw.code.ui.locators.settings import MainTabLocators, AsideMenuSettingsButtonLocators, NotificationTabLocators, \
    AccessListTabLocators


class TestMainTab(BaseCase):

    def test_settings_aside_button(self, settings_page, driver):
        # Можно перейти в настройки из любого места в ЛК, где доступно боковое меню
        driver.get(Config.VK_ADS_OVERVIEW_URL)
        WebDriverWait(driver, 10).until(EC.url_contains(Config.VK_ADS_OVERVIEW_URL))
        settings_page.click(AsideMenuSettingsButtonLocators.SETTINGS_BUTTON)
        assert settings_page.is_opened()

    def test_cancel_button(self, settings_page):
        # Вносим изменения в любые поля, чтобы появились кнопки "Сохранить" и "Отмена"
        settings_page.open_and_wait()
        settings_page.type_valid_data_on_main_tab()  # Вносим валидные изменения
        settings_page.fill_field(MainTabLocators.FULL_NAME_INPUT, 'test')
        current_name = settings_page.get_field_value(MainTabLocators.FULL_NAME_INPUT)  # Запоминаем текущее значение
        settings_page.cancel_settings()  # Нажимаем на кнопку "Отмена"
        assert settings_page.get_field_value(MainTabLocators.FULL_NAME_INPUT) != current_name

    def test_save_button(self, settings_page):
        # Вносим изменения в любые поля, чтобы появились кнопки "Сохранить" и "Отмена"
        # Для сохранения данные должны быть валидными
        settings_page.open_and_wait()
        settings_page.type_valid_data_on_main_tab()
        settings_page.save_settings()
        # Обновляем страницу и проверяем, что сохранения прошли успешно
        settings_page.open()
        assert settings_page.get_field_value(MainTabLocators.TEL_INPUT) == SettingsPage.valid_test_data['tel']

    def test_tel_validation(self, settings_page):
        settings_page.open_and_wait()
        # Сначала заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        # Попробуем перезаписать валидный номер на невалидные варианты
        invalid_cases = [
            '+7(900)5553535',  # Содержит символы помимо цифр и +
            '79005553535',     # Начинается не с +
            '+9999999999',     # Слишком короткий (< 11)
        ]
        for case in invalid_cases:
            settings_page.clear_field(MainTabLocators.TEL_INPUT)
            settings_page.fill_field(MainTabLocators.TEL_INPUT, case)
            settings_page.save_settings()
            assert settings_page.find(MainTabLocators.TEL_ERROR)
            settings_page.cancel_settings()

        # Особый случай: если ввести слишком длинный (> 13) номер, то он сам обрежется
        too_long_case = '+999999999981111'
        settings_page.clear_field(MainTabLocators.TEL_INPUT)
        settings_page.fill_field(MainTabLocators.TEL_INPUT, too_long_case)
        settings_page.save_settings()
        assert settings_page.get_field_value(MainTabLocators.TEL_INPUT) == '+9999999999811'

    def test_email_validation(self, settings_page):
        settings_page.open_and_wait()
        # Сначала заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        # Попробуем перезаписать валидный email на невалидные варианты
        invalid_cases = [
            'testexample.com',    # Ни одного символа @
            'test@@example.com',  # Больше одного символа @
            '@example.com',       # До символа @ ни одного символа из множества [a-zA-Z0-9]
            'test!@example.com',  # До символа @ символы не из множества [a-zA-Z0-9._-]
            'test@.com',          # Между @ и последней точкой нет ни одного символа из множества [a-zA-Zа-яА-Я0-9]
            'test@exa!mple.com',  # Между @ и последней точкой есть символы не из [a-zA-Zа-яА-Я0-9._-]
            'test@example.c',     # После последней точки нет как минимум двух символов из множества [a-zA-Zа-яА-Я]
        ]
        for case in invalid_cases:
            settings_page.clear_field(MainTabLocators.EMAIL_INPUT_0)
            settings_page.fill_field(MainTabLocators.EMAIL_INPUT_0, case)
            settings_page.save_settings()
            assert settings_page.find(MainTabLocators.EMAIL_ERROR)
            settings_page.cancel_settings()

    def test_email_limit(self, settings_page):
        # Можно добавить не более пяти email адресов
        settings_page.open_and_wait()
        assert not settings_page.find(MainTabLocators.ADD_EMAIL_BUTTON).get_attribute('disabled')
        # Сначала заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        # Одна почта уже есть, значит можно добавить ещё 4 (заполнять поля необязательно)
        for i in range(4):
            settings_page.click(MainTabLocators.ADD_EMAIL_BUTTON)
        # После добавления пятой почты кнопка должна заблокироваться
        assert settings_page.find(MainTabLocators.ADD_EMAIL_BUTTON).get_attribute('disabled')

    def test_delete_email(self, settings_page):
        settings_page.open_and_wait()
        # Заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        # Есть email => можно удалить
        assert settings_page.exists(MainTabLocators.DELETE_EMAIL_BUTTON)
        # Удалим все добавленные email
        while settings_page.exists(MainTabLocators.EMAIL_INPUT_0):
            settings_page.click(MainTabLocators.DELETE_EMAIL_BUTTON)
        assert not settings_page.exists(MainTabLocators.DELETE_EMAIL_BUTTON)

    def test_full_name(self, settings_page):
        settings_page.open_and_wait()
        settings_page.type_valid_data_on_main_tab()

        # Введём невалидное ФИО
        settings_page.type_full_name("123")
        settings_page.save_settings()
        assert settings_page.exists(MainTabLocators.FULL_NAME_ERROR)

        # Введём валидное ФИО
        settings_page.type_full_name(SettingsPage.valid_test_data['full_name'])
        settings_page.save_settings()
        assert not settings_page.exists(MainTabLocators.FULL_NAME_ERROR)

    def test_tin(self, settings_page):
        settings_page.open_and_wait()
        settings_page.type_valid_data_on_main_tab()

        # Введём невалидный ИНН из нецифирных символов
        settings_page.clear_field(MainTabLocators.TIN_INPUT)
        settings_page.fill_field(MainTabLocators.TIN_INPUT, 'test')
        settings_page.save_settings()
        assert settings_page.exists(MainTabLocators.TIN_INCORRECT_ERROR)

        # Введём невалидный ИНН из != 12 цифр
        settings_page.clear_field(MainTabLocators.TIN_INPUT)
        settings_page.fill_field(MainTabLocators.TIN_INPUT, '1234567890')
        settings_page.save_settings()
        assert settings_page.exists(MainTabLocators.TIN_INCORRECT_LEN_ERROR)

        # Введём невалидный ИНН из 12 цифр, но не соответствующий алгоритму (неправильная контрольная сумма)
        settings_page.clear_field(MainTabLocators.TIN_INPUT)
        settings_page.fill_field(MainTabLocators.TIN_INPUT, '990000000081')
        settings_page.save_settings()
        assert settings_page.exists(MainTabLocators.TIN_INVALID_ERROR)

        # Введём валидный ИНН
        settings_page.clear_field(MainTabLocators.TIN_INPUT)
        settings_page.fill_field(MainTabLocators.TIN_INPUT, SettingsPage.valid_test_data['tin'])
        # Т.к. это тот же ИНН, что был установлен изначально, кнопка "Сохранить" не появится
        assert not any((settings_page.exists(MainTabLocators.TIN_INVALID_ERROR),
                        settings_page.exists(MainTabLocators.TIN_INCORRECT_ERROR),
                        settings_page.exists(MainTabLocators.TIN_INCORRECT_LEN_ERROR)))

    def test_interface_params(self, settings_page, driver):
        settings_page.open_and_wait()
        settings_page.type_valid_data_on_main_tab()

        # Можно ввести не более 255 символов в название кабинета
        settings_page.clear_field(MainTabLocators.CABINET_NAME_INPUT)
        settings_page.fill_field(MainTabLocators.CABINET_NAME_INPUT, 'a' * 256)
        assert len(settings_page.get_field_value(MainTabLocators.CABINET_NAME_INPUT)) == 255

        # Можно задать название кабинета и оно отобразится в хедере
        cab_name = ''.join(random.choice(string.ascii_letters) for _ in range(25))
        settings_page.clear_field(MainTabLocators.CABINET_NAME_INPUT)
        settings_page.fill_field(MainTabLocators.CABINET_NAME_INPUT, cab_name)
        settings_page.save_settings()
        settings_page.open_and_wait()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainTabLocators.CABINET_NAME_LABEL))
        assert settings_page.find(MainTabLocators.CABINET_NAME_LABEL).text == cab_name

        # Можно сохранить пустым, тогда вместо названия будет имя клиента
        # settings_page.clear_field(SettingsLocators.CABINET_NAME_INPUT)
        # Компонент не реагирует непосредственно на изменение поля, надо эмулировать клавиатуру
        settings_page.find(MainTabLocators.CABINET_NAME_INPUT).send_keys('\b' * 255)
        settings_page.save_settings()
        settings_page.open_and_wait()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainTabLocators.CABINET_NAME_LABEL))
        assert settings_page.find(MainTabLocators.CABINET_NAME_LABEL).text == settings_page.valid_test_data['english_name']

        # При смене языка меняется язык всего интерфейса: в таббаре, боковом меню и главном блоке
        settings_page.set_en_lang()
        assert settings_page.find(MainTabLocators.GENERAL_TAB).text == 'General'
        assert settings_page.find(MainTabLocators.OVERVIEW_BUTTON).text == 'Overview'
        assert settings_page.find(MainTabLocators.ADD_EMAIL_BUTTON).text == 'Add email'
        # Теперь вернёмся на русский
        settings_page.set_ru_lang()
        assert settings_page.find(MainTabLocators.GENERAL_TAB).text == 'Общие'
        assert settings_page.find(MainTabLocators.OVERVIEW_BUTTON).text == 'Обзор'
        assert settings_page.find(MainTabLocators.ADD_EMAIL_BUTTON).text == 'Добавить email'

        # Нажатие кнопки "Список горячих клавиш" приводит к появлению модального окна с таблицей горячих клавиш
        settings_page.click(MainTabLocators.HOTKEYS_BUTTON)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainTabLocators.HOTKEYS_MODAL))
        assert settings_page.exists(MainTabLocators.HOTKEYS_MODAL)


class TestNotificationTab(BaseCase):
    def test_checkboxes(self, notification_settings_page):
        notification_settings_page.open_and_wait()
        # По умолчанию уведомления по почте включены, поэтому отключаем их
        notification_settings_page.set_email_notifications()
        # При выключении уведомлений появляется сообщение о том, что уведомления отключены
        assert notification_settings_page.exists(NotificationTabLocators.WARNING_MESSAGE)
        # При включении уведомлений сообщение пропадает
        notification_settings_page.set_email_notifications()
        assert not notification_settings_page.exists(NotificationTabLocators.WARNING_MESSAGE)

    def test_options_availability(self, notification_settings_page):
        notification_settings_page.open_and_wait()
        # Если уведомления отключены, то опции недоступны
        notification_settings_page.set_email_notifications()
        assert notification_settings_page.find(NotificationTabLocators.FINANCE_OPTION_LABEL).get_attribute('disabled') is not None
        # Если включены уведомления хотя бы одним из методов, то опции доступны к выбору
        notification_settings_page.set_email_notifications()
        assert notification_settings_page.find(NotificationTabLocators.FINANCE_OPTION_LABEL).get_attribute('disabled') is None


class TestAccessListTab(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, access_settings_page):
        access_settings_page.open_and_wait()
        access_settings_page.delete_all_invites()  # Для идемпотентности тестов

    def test_empty_list(self, access_settings_page):
        # У пользователя по умолчанию не отправлено никаких приглашений
        assert access_settings_page.exists(AccessListTabLocators.EMPTY_ACCESS_LIST_MESSAGE)

    def test_modal(self, access_settings_page):
        # Нажатие на кнопку "Добавить кабинет" открывает модальное окно
        access_settings_page.click(AccessListTabLocators.SEND_INVITE_BUTTON)
        assert access_settings_page.exists(AccessListTabLocators.MODAL)
        # Модальное окно содержит поле ввода ID пользователя, кнопки "Отправить" и "Отмена" появляются после ввода ID
        assert access_settings_page.exists(AccessListTabLocators.USER_ID_INPUT)
        assert access_settings_page.exists(AccessListTabLocators.SUBMIT_BUTTON)
        assert access_settings_page.exists(AccessListTabLocators.CANCEL_BUTTON)
        access_settings_page.click(AccessListTabLocators.CANCEL_BUTTON)

    def test_modal_send_invite(self, access_settings_page):
        access_settings_page.click(AccessListTabLocators.SEND_INVITE_BUTTON)

        # В ID пользователя можно ввести только цифры в количестве не более 10 штук
        access_settings_page.fill_field(AccessListTabLocators.USER_ID_INPUT, 'abc012345678901234')
        assert access_settings_page.get_field_value(AccessListTabLocators.USER_ID_INPUT) == '0123456789'

        # При отправке приглашения несуществующему пользователю появляется сообщение об ошибке
        access_settings_page.send_invite_to_invalid_user()
        assert access_settings_page.exists(AccessListTabLocators.SOMETHING_WENT_WRONG_MESSAGE)

        # При отправке приглашения существующему пользователю модальное окно закроется и приглашение отправится
        access_settings_page.send_invite_to_valid_user()
        assert access_settings_page.exists(AccessListTabLocators.THESE_USERS_HAVE_ACCESS_LABEL)

        # При попытке отправить приглашение уже добавленному пользователю появляется сообщение об ошибке
        access_settings_page.click(AccessListTabLocators.SEND_INVITE_BUTTON_TOP)
        access_settings_page.send_invite_to_valid_user_again()
        assert access_settings_page.exists(AccessListTabLocators.USER_ALREADY_ADDED_MESSAGE)
        access_settings_page.click(AccessListTabLocators.CANCEL_BUTTON)

    def test_non_empty_access_list(self, access_settings_page):
        # После отправки приглашения список пользователей не пуст
        access_settings_page.click(AccessListTabLocators.SEND_INVITE_BUTTON)
        access_settings_page.send_invite_to_valid_user()
        assert access_settings_page.exists(AccessListTabLocators.THESE_USERS_HAVE_ACCESS_LABEL)

    def test_delete_invite(self, access_settings_page):
        access_settings_page.click(AccessListTabLocators.SEND_INVITE_BUTTON)
        access_settings_page.send_invite_to_valid_user()
        # После отправки приглашения кнопка удаления появляется
        assert access_settings_page.exists(AccessListTabLocators.DELETE_INVITE_BUTTON)
        # При удалении приглашения пользователь исчезает (список станет пустым)
        # Открываем модальное окно с подтверждением удаления
        access_settings_page.focus(AccessListTabLocators.DELETE_INVITE_BUTTON)
        access_settings_page.click(AccessListTabLocators.DELETE_INVITE_BUTTON)
        assert access_settings_page.is_visible(AccessListTabLocators.MODAL)
        # Кнопка отмены отменяет действие и пользователь остаётся
        access_settings_page.click(AccessListTabLocators.DELETE_INVITE_CANCEL_BUTTON)
        assert access_settings_page.exists(AccessListTabLocators.THESE_USERS_HAVE_ACCESS_LABEL)
        # Кнопка подтверждения удаления удаляет пользователя
        access_settings_page.focus(AccessListTabLocators.DELETE_INVITE_BUTTON)
        access_settings_page.click(AccessListTabLocators.DELETE_INVITE_BUTTON)
        access_settings_page.click(AccessListTabLocators.DELETE_INVITE_CONFIRM_BUTTON)
        assert access_settings_page.exists(AccessListTabLocators.EMPTY_ACCESS_LIST_MESSAGE)

    def test_search(self, access_settings_page):
        access_settings_page.click(AccessListTabLocators.SEND_INVITE_BUTTON)
        access_settings_page.send_invite_to_valid_user()
        # Поиск по ID пользователя
        access_settings_page.click(AccessListTabLocators.SEARCH_INPUT)
        # Из-за специфики компонента нужно эмулировать нажатие клавиши Backspace вместо использования clear_field
        access_settings_page.find(AccessListTabLocators.SEARCH_INPUT).send_keys('\b' * 100)
        access_settings_page.fill_field(AccessListTabLocators.SEARCH_INPUT, access_settings_page.valid_vk_ads_cabinet_id)
        # Пользователь найден
        assert not access_settings_page.exists(AccessListTabLocators.EMPTY_SEARCH_MESSAGE)
        # Поиск по несуществующему ID пользователя
        access_settings_page.click(AccessListTabLocators.SEARCH_INPUT)
        access_settings_page.find(AccessListTabLocators.SEARCH_INPUT).send_keys('\b' * 100)
        access_settings_page.fill_field(AccessListTabLocators.SEARCH_INPUT, access_settings_page.invalid_vk_ads_cabinet_id)
        # Пользователь не найден
        assert access_settings_page.exists(AccessListTabLocators.EMPTY_SEARCH_MESSAGE)


class TestChangesHistoryTab(BaseCase):
    pass

