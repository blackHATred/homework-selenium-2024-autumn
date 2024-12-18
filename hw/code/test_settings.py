import random
import string

from hw.code.base import BaseCase

from hw.code.fixtures import *


class TestMainTab(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, settings_page):
        settings_page.open_and_wait()

    def test_settings_aside_button(self, settings_page):
        # Можно перейти в настройки из любого места в ЛК, где доступно боковое меню
        settings_page.open_and_wait(Config.VK_ADS_OVERVIEW_URL)  # Уйдем со страницы настроек на обзорную
        settings_page.click_aside_settings_button()
        assert settings_page.is_opened()

    def test_cancel_button(self, settings_page):
        # Вносим изменения в любые поля, чтобы появились кнопки "Сохранить" и "Отмена"
        settings_page.type_valid_data_on_main_tab()  # Вносим валидные изменения
        settings_page.type_full_name('test')
        current_name = settings_page.full_name  # Запоминаем текущее значение
        settings_page.cancel_settings()  # Нажимаем на кнопку "Отмена"
        assert settings_page.full_name != current_name

    def test_save_button(self, settings_page):
        # Вносим изменения в любые поля, чтобы появились кнопки "Сохранить" и "Отмена"
        # Для сохранения данные должны быть валидными
        settings_page.type_valid_data_on_main_tab()
        settings_page.save_settings()
        # Обновляем страницу и проверяем, что сохранения прошли успешно
        settings_page.open_and_wait()
        assert settings_page.phone_number == SettingsPage.valid_test_data['tel']

    def test_tel_validation(self, settings_page):
        # Сначала заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        # Попробуем перезаписать валидный номер на невалидные варианты
        invalid_cases = [
            '+7(900)5553535',  # Содержит символы помимо цифр и +
            '79005553535',     # Начинается не с +
            '+9999999999',     # Слишком короткий (< 11)
        ]
        for case in invalid_cases:
            settings_page.type_phone_number(case)
            settings_page.save_settings()
            assert settings_page.phone_number_error
            settings_page.cancel_settings()

        # Особый случай: если ввести слишком длинный (> 13) номер, то он сам обрежется
        too_long_case = '+999999999981111'
        settings_page.type_phone_number(too_long_case)
        settings_page.save_settings()
        assert settings_page.phone_number == '+9999999999811'

    def test_email_validation(self, settings_page):
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
            settings_page.type_email(case)
            settings_page.save_settings()
            assert settings_page.email_error
            settings_page.cancel_settings()

    def test_email_limit(self, settings_page):
        # Можно добавить не более пяти email адресов
        assert settings_page.is_add_email_button_available
        # Сначала заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        # Одна почта уже есть, значит можно добавить ещё 4 (заполнять поля необязательно)
        for i in range(4):
            settings_page.add_email()
        # После добавления пятой почты кнопка должна заблокироваться
        assert not settings_page.is_add_email_button_available

    def test_delete_email(self, settings_page):
        # Заполним валидными данными
        settings_page.type_valid_data_on_main_tab()
        # Есть email => можно удалить
        assert settings_page.is_delete_email_button_available
        # Удалим все добавленные email
        settings_page.delete_all_emails()
        assert not settings_page.is_delete_email_button_available

    def test_full_name(self, settings_page):
        settings_page.type_valid_data_on_main_tab()

        # Введём невалидное ФИО
        settings_page.type_full_name("123")
        settings_page.save_settings()
        assert settings_page.full_name_error

        # Введём валидное ФИО
        settings_page.type_full_name(SettingsPage.valid_test_data['full_name'])
        settings_page.save_settings()
        assert not settings_page.full_name_error

    def test_tin(self, settings_page):
        settings_page.type_valid_data_on_main_tab()

        # Введём невалидный ИНН из нецифирных символов
        settings_page.type_tin('test')
        settings_page.save_settings()
        assert settings_page.tin_incorrect_error

        # Введём невалидный ИНН из != 12 цифр
        settings_page.type_tin('1234567890')
        settings_page.save_settings()
        assert settings_page.tin_incorrect_len_error

        # Введём невалидный ИНН из 12 цифр, но не соответствующий алгоритму (неправильная контрольная сумма)
        settings_page.type_tin('990000000081')
        settings_page.save_settings()
        assert settings_page.tin_invalid_error

        # Введём валидный ИНН
        settings_page.type_tin(SettingsPage.valid_test_data['tin'])
        # Т.к. это тот же ИНН, что был установлен изначально, кнопка "Сохранить" не появится
        assert not any((settings_page.tin_incorrect_error,
                        settings_page.tin_invalid_error,
                        settings_page.tin_incorrect_len_error,))

    def test_interface_params(self, settings_page):
        settings_page.type_valid_data_on_main_tab()

        # Можно ввести не более 255 символов в название кабинета
        settings_page.type_cabinet_name('a' * 256)
        assert len(settings_page.cabinet_name) == 255

        # Можно задать название кабинета и оно отобразится в хедере
        cab_name = ''.join(random.choice(string.ascii_letters) for _ in range(25))
        settings_page.type_cabinet_name(cab_name)
        settings_page.save_settings()
        settings_page.open_and_wait()
        assert settings_page.cabinet_name_label == cab_name

        # Можно сохранить пустым, тогда вместо названия будет имя клиента
        # Компонент не реагирует непосредственно на изменение поля, надо эмулировать клавиатуру
        settings_page.cabinet_name_input.send_keys('\b' * 255)
        settings_page.save_settings()
        settings_page.open_and_wait()
        assert settings_page.cabinet_name_label == settings_page.valid_test_data['english_name']

        # При смене языка меняется язык всего интерфейса: в таббаре, боковом меню и главном блоке
        # В идеале, конечно, нужно проверять все компоненты на перевод, но ограничимся проверкой на то, что перевод
        # происходит во всех блоках
        settings_page.set_en_lang()
        settings_page.open_and_wait()
        assert settings_page.general_tab_text == settings_page.translation['Общие']
        assert settings_page.overview_button_text == settings_page.translation['Обзор']
        assert settings_page.add_email_button.text == settings_page.translation['Добавить email']
        # Теперь вернёмся на русский
        settings_page.set_ru_lang()
        settings_page.open_and_wait()
        assert settings_page.general_tab_text == 'Общие'
        assert settings_page.overview_button_text == 'Обзор'
        assert settings_page.add_email_button.text == 'Добавить email'

        # Нажатие кнопки "Список горячих клавиш" приводит к появлению модального окна с таблицей горячих клавиш
        settings_page.click_hotkeys_button()
        assert settings_page.hotkeys_modal


class TestNotificationTab(BaseCase):
    def test_checkboxes(self, notification_settings_page):
        notification_settings_page.open_and_wait()
        # По умолчанию уведомления по почте включены, поэтому отключаем их
        notification_settings_page.set_email_notifications()
        # При выключении уведомлений появляется сообщение о том, что уведомления отключены
        assert notification_settings_page.warning_message
        # При включении уведомлений сообщение пропадает
        notification_settings_page.set_email_notifications()
        assert not notification_settings_page.warning_message

    def test_options_availability(self, notification_settings_page):
        notification_settings_page.open_and_wait()
        # Если уведомления отключены, то опции недоступны
        notification_settings_page.set_email_notifications()
        assert not notification_settings_page.is_finances_option_available
        # Если включены уведомления хотя бы одним из методов, то опции доступны к выбору
        notification_settings_page.set_email_notifications()
        assert notification_settings_page.is_finances_option_available


class TestAccessListTab(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, access_settings_page):
        access_settings_page.open_and_wait()
        access_settings_page.delete_all_invites()  # Для идемпотентности тестов

    def test_empty_list(self, access_settings_page):
        # У пользователя по умолчанию не отправлено никаких приглашений
        assert access_settings_page.empty_list_message

    def test_modal(self, access_settings_page):
        # Нажатие на кнопку "Добавить кабинет" открывает модальное окно
        access_settings_page.click_invite_button()
        assert access_settings_page.is_close_hints_modal_opened
        # Модальное окно содержит поле ввода ID пользователя, кнопки "Отправить" и "Отмена" появляются после ввода ID
        assert access_settings_page.is_user_id_input_visible
        assert access_settings_page.is_submit_button_visible
        assert access_settings_page.is_cancel_button_visible
        access_settings_page.click_cancel_button()

    def test_modal_send_invite(self, access_settings_page):
        access_settings_page.click_invite_button()

        # В ID пользователя можно ввести только цифры в количестве не более 10 штук
        access_settings_page.type_user_id('abc012345678901234')
        assert access_settings_page.user_id_field_value == '0123456789'

        # При отправке приглашения несуществующему пользователю появляется сообщение об ошибке
        access_settings_page.send_invite_to_invalid_user()
        assert access_settings_page.something_went_wrong_message

        # При отправке приглашения существующему пользователю модальное окно закроется и приглашение отправится
        access_settings_page.send_invite_to_valid_user()
        assert access_settings_page.these_users_have_access_label

        # При попытке отправить приглашение уже добавленному пользователю появляется сообщение об ошибке
        access_settings_page.click_top_invite_button()
        access_settings_page.send_invite_to_valid_user_again()
        assert access_settings_page.user_already_added_message
        access_settings_page.click_cancel_button()

    def test_non_empty_access_list(self, access_settings_page):
        # После отправки приглашения список пользователей не пуст
        access_settings_page.click_invite_button()
        access_settings_page.send_invite_to_valid_user()
        access_settings_page.open_and_wait()  # Обновляем страницу, чтобы убедиться, что данные сохранились
        assert access_settings_page.these_users_have_access_label

    def test_delete_invite(self, access_settings_page):
        access_settings_page.click_invite_button()
        access_settings_page.send_invite_to_valid_user()
        # После отправки приглашения кнопка удаления появляется
        assert access_settings_page.is_delete_invite_button_visible
        # При удалении приглашения пользователь исчезает (список станет пустым)
        # Открываем модальное окно с подтверждением удаления
        access_settings_page.click_delete_invite_button()
        assert access_settings_page.is_close_hints_modal_opened
        # Кнопка отмены отменяет действие и пользователь остаётся
        access_settings_page.click_cancel_delete_invite_button()
        assert access_settings_page.these_users_have_access_label
        # Кнопка подтверждения удаления удаляет пользователя
        access_settings_page.click_delete_invite_button()
        access_settings_page.click_confirm_delete_invite_button()
        assert access_settings_page.empty_list_message

    def test_search(self, access_settings_page):
        access_settings_page.click_invite_button()
        access_settings_page.send_invite_to_valid_user()
        # Поиск по ID пользователя
        access_settings_page.type_search_input(access_settings_page.valid_vk_ads_cabinet_id)
        # Пользователь найден
        assert not access_settings_page.empty_search_message
        # Поиск по несуществующему ID пользователя
        access_settings_page.type_search_input(access_settings_page.invalid_vk_ads_cabinet_id)
        # Пользователь не найден
        assert access_settings_page.empty_search_message


class TestChangesHistoryTab(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, logs_settings_page):
        logs_settings_page.open_and_wait()
        logs_settings_page.delete_all_filters()  # Для идемпотентности тестов

    def test_filter_modal(self, logs_settings_page, driver):
        # Нажатие на кнопку "Фильтр" открывает модальное окно с фильтрами
        logs_settings_page.open_filter_modal()
        assert logs_settings_page.is_filter_category_object_type_visible

        # Выбор категории приводит к отображению соответствующих категории опций
        # Тип объекта
        options = logs_settings_page.get_current_available_filter_options()
        for option in logs_settings_page.filter_categories['Тип объекта']:
            assert option in options
        # Что изменилось
        logs_settings_page.click_filter_category_what_changed_button()
        options = logs_settings_page.get_current_available_filter_options()
        for option in logs_settings_page.filter_categories['Что изменилось']:
            assert option in options
        # Автор изменения
        logs_settings_page.click_filter_category_author_button()
        options = logs_settings_page.get_current_available_filter_options()
        for option in logs_settings_page.filter_categories['Автор изменения']:
            assert option in options

        logs_settings_page.click_filter_category_object_type_button()
        # Кнопка "Выбрать все" выбирает все опции, кнопка "Сбросить" отсутствует, т.к. ничего не выбрано
        assert logs_settings_page.is_check_all_button_visible
        assert not logs_settings_page.is_uncheck_all_button_visible
        logs_settings_page.click_check_all_button()
        options = logs_settings_page.get_options_check_status()
        assert all((opt for opt in options))

        # Когда выбрана хоть одна опция, то появляется кнопка "Сбросить", а "Выбрать все" исчезает
        assert not logs_settings_page.is_check_all_button_visible
        assert logs_settings_page.is_uncheck_all_button_visible
        logs_settings_page.click_uncheck_all_button()
        options = logs_settings_page.get_options_check_status()
        assert not any((opt for opt in options))

        # Нажатие на кнопку "Отмена" закрывает модальное окно
        logs_settings_page.click_cancel_filter()
        assert not logs_settings_page.is_filter_category_object_type_visible

        # Нажатие на кнопку "Применить" применяет выбранные фильтры
        logs_settings_page.open_filter_modal()
        logs_settings_page.click_filter_category_object_type_button()
        logs_settings_page.click_check_all_button()
        logs_settings_page.click_apply_filter()
        assert logs_settings_page.is_applied_filter_element_visible

    def test_applied_filters_list(self, logs_settings_page):
        # При применении одного фильтра кнопка "Сбросить все" отсутствует
        logs_settings_page.apply_one_filter()
        assert not logs_settings_page.is_delete_all_button_visible
        logs_settings_page.click_delete_filter()
        # При применении двух фильтров кнопка "Сбросить все" появляется
        logs_settings_page.apply_two_filters()
        assert logs_settings_page.is_delete_all_button_visible
        # При нажатии на кнопку "Сбросить все" все фильтры сбрасываются
        logs_settings_page.click_delete_all_filters()
        assert not logs_settings_page.is_applied_filter_element_visible
