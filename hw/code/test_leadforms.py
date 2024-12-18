from hw.code.base import BaseCase
from hw.code.fixtures import *


class TestLeadForms(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, lead_forms_page):
        lead_forms_page.open_and_wait()
        # Если уже есть какие-то лид-формы, то сначала архивируем их для идемпотентности
        lead_forms_page.archive_all_lead_forms()

    def test_lead_form_creation(self, lead_forms_page):
        # Нажатие на кнопку приводит к появлению модального окна
        lead_forms_page.click_create_leadform_button()
        assert lead_forms_page.is_leadform_creation_modal_opened
        # При нажатии на кнопку "Отмена" модальное окно закрывается
        lead_forms_page.click_cancel_creation_leadform_button()
        assert not lead_forms_page.is_leadform_creation_modal_opened
        lead_forms_page.click_create_leadform_button()
        # По умолчанию название лидформы уже заполнено, очищаем его
        lead_forms_page.clear_leadform_name()
        # Так ни одно обязательное поле (название формы, логотип, название компании, заголовок, описание) не заполнено,
        # появляется соответствующее число ошибок об необходимости заполнить обязательные поля
        lead_forms_page.click_next_step_button()
        assert lead_forms_page.must_fill_field_alerts == 5
        # Заполним название формы и загрузим логотип компании
        lead_forms_page.set_leadform_name('Test')
        lead_forms_page.set_logo(f'{Config.ASSETS_DIR}/img.png')
        # Попробуем нарушить правила валидации по длине полей
        # У поля "Название компании" максимум 30 символов
        # У поля "Заголовок" максимум 50 символов
        # У поля "Описание" максимум 35 символов
        lead_forms_page.set_company_name('a' * 31)
        lead_forms_page.set_header_text('a' * 51)
        lead_forms_page.set_description_text('a' * 36)
        lead_forms_page.click_next_step_button()
        # Должно быть три сообщения о превышении максимальной длины поля
        assert lead_forms_page.too_large_field_alerts == 3
        # Теперь заполним валидными значениями
        lead_forms_page.set_company_name('Company')
        lead_forms_page.set_header_text('Header')
        lead_forms_page.set_description_text('Description')
        # Проверим, что все введенные поля повлияли на окно предпросмотра: там отображаются наши данные
        assert lead_forms_page.is_logo_set
        assert lead_forms_page.is_company_name_set('Company')
        assert lead_forms_page.is_header_text_set('Header')
        assert lead_forms_page.is_description_text_set('Description')
        # Переход на следующий шаг
        # Может потребоваться обрезка картинки, поэтому дважды нажимаем на кнопку
        lead_forms_page.click_next_step_button()
        # Так как все поля валидны, то должен открыться шаг с вопросами
        assert lead_forms_page.is_second_step_opened

        # Второй шаг
        # Удаляем все контактные данные и видим сообщение о необходимости хотя бы одного контакта
        lead_forms_page.delete_all_contact_data()
        lead_forms_page.click_next_step_button()
        assert lead_forms_page.is_contacts_error_shown
        # Нажимаем на кнопку "Добавить контактные данные" и видим модалку с вариантами, выбираем все
        lead_forms_page.click_add_contact_data_button()
        lead_forms_page.click_all_contact_data_option()
        # Сохраняем и видим все варианты в окне предпросмотра
        lead_forms_page.click_save_contact_data()
        assert lead_forms_page.is_preview_contact_name_input_visible
        assert lead_forms_page.is_preview_contact_email_input_visible
        assert lead_forms_page.is_preview_contact_phone_input_visible
        assert lead_forms_page.is_preview_contact_link_input_visible
        assert lead_forms_page.is_preview_contact_birth_date_input_visible
        assert lead_forms_page.is_preview_contact_city_input_visible
        # Добавим вопрос
        lead_forms_page.click_add_question_button()
        # При попытке перехода на следующий шаг без введенного вопроса будет подсвечена ошибка
        lead_forms_page.click_next_step_button()
        assert lead_forms_page.is_question_error_shown
        # Введем текст вопроса и видим его в окне предпросмотра. Максимальная длина 68 символов, дальше он урезается сам
        lead_forms_page.set_question_text('a' * 69)
        assert lead_forms_page.is_question_text_set('a' * 68)
        # Проверяем наличие вопроса в предпросмотре
        assert lead_forms_page.is_question_element_visible('a' * 68)
        # Можно добавить максимум 7 ответов на вопрос, 2 имеются по умолчанию, потом кнопка исчезает
        for _ in range(5):
            lead_forms_page.click_add_variant_button()
        assert not lead_forms_page.is_add_variant_button_visible
        # Удалим первый из вариантов ответа и убедимся, что кнопка добавления снова появилась
        lead_forms_page.delete_variant()
        assert lead_forms_page.is_add_variant_button_visible
        # Переключаем тип выбора ответа и видим изменения в предпросмотре
        # По умолчанию выбран тип "Выбор одного ответа"
        assert lead_forms_page.is_radio_answer_type_shown
        # Переключаем на "Выбор нескольких ответов"
        lead_forms_page.click_question_type_dropdown()
        lead_forms_page.select_many_answers_option()
        assert lead_forms_page.is_checkbox_answer_type_shown
        # Переключаем на "Ответ в произвольной форме"
        lead_forms_page.click_question_type_dropdown()
        lead_forms_page.select_text_answer_option()
        assert lead_forms_page.is_text_answer_type_shown
        # Удалим вопрос, он необязателен для перехода на следующий шаг
        lead_forms_page.delete_question()
        # Вопроса больше нет в предпросмотре
        assert not lead_forms_page.is_question_element_visible('a' * 68)
        # Теперь все заполнено валидно, переходим на следующий шаг
        lead_forms_page.click_next_step_button()
        # Проверяем, что открылся шаг 3
        assert lead_forms_page.is_third_step_opened

        # Третий шаг
        # При пустом заголовке ответа не удастся продолжить
        lead_forms_page.clear_results_header()
        lead_forms_page.click_next_step_button()
        assert lead_forms_page.must_fill_field_alerts == 1
        # Максимальная длина заголовка - 25, а описания - 160
        lead_forms_page.set_results_header('a' * 26)
        lead_forms_page.set_results_description('a' * 161)
        lead_forms_page.click_next_step_button()
        assert lead_forms_page.too_large_field_alerts == 2
        # Заполняем валидными данными и проверяем, что они отобразились в окне предпросмотра
        lead_forms_page.set_results_header('Results header')
        lead_forms_page.set_results_description('Results description')
        assert lead_forms_page.is_results_header_set('Results header')
        assert lead_forms_page.is_results_description_set('Results description')
        # Переходим на следующий шаг
        lead_forms_page.click_next_step_button()
        # Проверяем, что открылся шаг 4
        assert lead_forms_page.is_fourth_step_opened

        # Четвертый шаг
        # Проверяем, что если не ввести ФИО и адрес места жительства, то лид-форма не создастся
        lead_forms_page.click_next_step_button()
        assert lead_forms_page.must_fill_field_alerts == 2
        # Заполняем поля и проверяем, что лид-фома создалась. Данные выше никак не влияют на отображение лид-формы,
        # поэтому проверки предпросмотра нет
        lead_forms_page.set_settings_name('Full name')
        lead_forms_page.set_settings_address('Address')
        lead_forms_page.click_next_step_button()
        # должен появиться элемент в списке с изначальным названием лид-формы
        assert lead_forms_page.is_element_in_list('Test')

    def test_lead_form_edit(self, lead_forms_page):
        # Для начала создадим тестовую форму
        lead_forms_page.create_example_lead_form('test_lead_form_edit')
        # перезагрузим страницу и убедимся, что форма с таким именем есть в списке
        lead_forms_page.open_and_wait()
        assert lead_forms_page.is_element_in_list('test_lead_form_edit')
        # нажмем на кнопку "Редактировать" и убедимся, что открылось точно такое же модальное окно, как и при создании:
        # все поля заполнены теми же данными, проверим это на примере названия лид-формы
        lead_forms_page.click_edit_lead_form()
        assert lead_forms_page.is_leadform_creation_modal_opened
        assert lead_forms_page.is_leadform_name_set('test_lead_form_edit')
        # Изменим название лид-формы и сохраним её (для этого надо 4 раза нажать "Продолжить")
        lead_forms_page.set_leadform_name('edited_test_lead_form')
        lead_forms_page.click_next_step_button(4)
        # перезагружаем страницу ещё раз и видим, что название формы и правда поменялось
        lead_forms_page.open_and_wait()
        assert lead_forms_page.is_element_in_list('edited_test_lead_form')

    def test_archive(self, lead_forms_page):
        # создадим тестовую форму
        lead_forms_page.create_example_lead_form('test_archive')
        # архивируем её
        lead_forms_page.archive_lead_form()
        # перезагружаем страницу и убеждаемся, что форма архивирована
        lead_forms_page.open_and_wait()
        lead_forms_page.select_archive_category()
        assert lead_forms_page.is_element_in_list('test_archive')
        # теперь восстанавливаем форму
        lead_forms_page.restore_lead_form('test_archive')
        # перезагружаем страницу и убеждаемся, что форма восстановлена
        lead_forms_page.open_and_wait()
        assert lead_forms_page.is_element_in_list('test_archive')

    def test_search(self, lead_forms_page):
        # создадим тестовую форму
        lead_forms_page.create_example_lead_form('test_search')
        # в поисковой строке введем название созданной формы
        lead_forms_page.search_lead_form('test_search')
        # убедимся, что форма найдена
        assert lead_forms_page.is_element_in_list('test_search')
        # очистим поисковую строку и введём несуществующую форму
        lead_forms_page.clear_search()
        lead_forms_page.search_lead_form('abc')
        assert not lead_forms_page.is_element_in_list('abc')

    def test_tutorial(self, lead_forms_page):
        # Если нет активных лид-форм, то есть опция с прохождением обучения. По умолчанию активных лид-форм нет
        # Должно открыться модальное окно с выбором вариантов обучения
        lead_forms_page.click_start_tutorial()
        assert lead_forms_page.is_tutorial_modal_opened

        # При варианте обучения по курсу должна открыться страница с курсом
        lead_forms_page.click_watch_course_option()
        assert lead_forms_page.is_vk_expert_page_opened
        lead_forms_page.close_vk_expert_page()

        # При варианте обучения по видео должен открыться плеер
        lead_forms_page.click_start_tutorial()
        lead_forms_page.click_watch_expert_video_option()
        assert lead_forms_page.is_video_player_opened

    def test_hints(self, lead_forms_page):
        lead_forms_page.click_start_tutorial()
        lead_forms_page.click_create_with_hints_option()

        # Должно открыться модальное окно создания с первой подсказкой
        assert lead_forms_page.is_first_hint_opened
        # Кнопка "Далее" открывает следующую подсказку
        lead_forms_page.click_next_hint()
        assert lead_forms_page.is_second_hint_opened
        # Кнопка "Назад" возвращает к предыдущей подсказке
        lead_forms_page.click_previous_hint()
        assert lead_forms_page.is_first_hint_opened
        # Кнопка крестика приводит к появлению модального окна
        lead_forms_page.click_stop_tutorial()
        assert lead_forms_page.is_close_hints_modal_opened
        # Кнопка "Отмена" закрывает модальное окно подтверждения и открывается последняя активная подсказка
        lead_forms_page.click_cancel_hint_modal()
        assert lead_forms_page.is_first_hint_opened
        # Кнопка "Прервать" закрывает модальное окно подтверждения и возвращает к модальному окну обучения
        lead_forms_page.click_stop_tutorial()
        lead_forms_page.click_agree_hint_modal()
        assert not lead_forms_page.is_first_hint_opened
