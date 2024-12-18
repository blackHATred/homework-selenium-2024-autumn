from hw.code.base import BaseCase
from hw.code.fixtures import *


class TestSurveys(BaseCase):
    @pytest.fixture(autouse=True)
    def setup(self, surveys_page):
        surveys_page.open_and_wait()
        # Если уже есть какие-то опросы, то сначала архивируем их для идемпотентности
        surveys_page.archive_all_surveys()

    def test_survey_creation(self, surveys_page):
        # Нажатие на кнопку приводит к появлению модального окна
        surveys_page.click_create_survey_button()
        assert surveys_page.is_survey_creation_modal_opened
        # По умолчанию название опроса уже заполнено, очищаем его
        surveys_page.clear_survey_name()
        # Если обязательные поле (название опроса, логотип, название компании, заголовок, описание) не заполнены,
        # появляется соответствующее число ошибок об необходимости заполнить обязательные поля
        surveys_page.click_next_step_button()
        assert surveys_page.must_fill_field_alerts == 5
        # Заполним название опроса и загрузим логотип компании
        surveys_page.set_survey_name('Test')
        surveys_page.set_logo(f'{Config.ASSETS_DIR}/img.png')
        # Попробуем нарушить правила валидации по длине полей
        # У поля "Название компании" максимум 30 символов
        # У поля "Заголовок" максимум 50 символов
        # У поля "Описание" максимум 350 символов
        surveys_page.set_company_name('a' * 31)
        surveys_page.set_header_text('a' * 51)
        surveys_page.set_description_text('a' * 351)
        surveys_page.click_next_step_button()
        # Должно быть три сообщения о превышении максимальной длины поля
        assert surveys_page.too_large_field_alerts == 3
        # Теперь заполним валидными значениями
        surveys_page.set_company_name('Company')
        surveys_page.set_header_text('Header')
        surveys_page.set_description_text('Description')
        # Проверим, что все введенные поля повлияли на окно предпросмотра: там отображаются наши данные
        assert surveys_page.is_logo_set
        assert surveys_page.is_company_name_set('Company')
        assert surveys_page.is_header_text_set('Header')
        assert surveys_page.is_description_text_set('Description')
        # Переход на следующий шаг
        surveys_page.click_next_step_button()
        # Так как все поля валидны, то должен открыться шаг с вопросами
        assert surveys_page.is_second_step_opened

        # Второй шаг
        # По умолчанию уже есть один вопрос, добавим ещё один
        surveys_page.click_add_question_button()
        assert surveys_page.question_count == 2
        # Теперь удалим первый вопрос
        surveys_page.delete_question()
        assert surveys_page.question_count == 1
        # При попытке перехода на следующий шаг без введенного вопроса будет подсвечена ошибка
        surveys_page.click_next_step_button()
        assert surveys_page.is_question_error_shown
        # Введем текст вопроса и видим его в окне предпросмотра
        surveys_page.set_question_text('a' * 5)
        assert surveys_page.is_question_element_visible('a' * 5)
        # Можно добавить максимум 7 ответов на вопрос, 2 имеются по умолчанию, потом кнопка исчезает
        for _ in range(5):
            surveys_page.click_add_variant_button()
        assert not surveys_page.is_add_variant_button_visible
        # Удалим первый из вариантов ответа и убедимся, что кнопка добавления снова появилась
        surveys_page.delete_variant()
        assert surveys_page.is_add_variant_button_visible
        # Переключаем тип выбора ответа и видим изменения в предпросмотре
        # По умолчанию выбран тип "Выбор одного ответа"
        assert surveys_page.is_radio_answer_type_shown
        # Переключаем на "Выбор нескольких ответов"
        surveys_page.click_question_type_dropdown()
        surveys_page.select_many_answers_option()
        assert surveys_page.is_checkbox_answer_type_shown
        # Переключаем на "Ответ в произвольной форме"
        surveys_page.click_question_type_dropdown()
        surveys_page.select_text_answer_option()
        assert surveys_page.is_text_answer_type_shown
        # Переключаем на "Шкала"
        surveys_page.click_question_type_dropdown()
        surveys_page.select_scale_answer_option()
        assert surveys_page.is_scale_answer_type_shown
        # Теперь все заполнено валидно, переходим на следующий шаг
        surveys_page.click_next_step_button()
        # Проверяем, что открылся шаг 3
        assert surveys_page.is_third_step_opened

        # Третий шаг
        # При пустом заголовке ответа не удастся продолжить
        surveys_page.clear_results_header()
        surveys_page.click_next_step_button()
        assert surveys_page.must_fill_field_alerts == 1
        # Максимальная длина заголовка - 25, а описания - 160
        surveys_page.set_results_header('a' * 26)
        surveys_page.set_results_description('a' * 161)
        surveys_page.click_next_step_button()
        assert surveys_page.too_large_field_alerts == 2
        # Заполняем валидными данными и проверяем, что они отобразились в окне предпросмотра
        surveys_page.set_results_header('Results header')
        surveys_page.set_results_description('Results description')
        assert surveys_page.is_results_header_set('Results header')
        assert surveys_page.is_results_description_set('Results description')
        # Переходим на следующий шаг
        surveys_page.click_next_step_button()
        # должен появиться элемент в списке с изначальным названием опроса
        assert surveys_page.is_element_in_list('Test')

    def test_survey_edit(self, surveys_page):
        # Для начала создадим тестовый опрос
        surveys_page.create_example_survey('test_survey_edit')
        # перезагрузим страницу и убедимся, что форма с таким именем есть в списке
        surveys_page.open_and_wait()
        assert surveys_page.is_element_in_list('test_survey_edit')
        # нажмем на кнопку "Редактировать" и убедимся, что открылось точно такое же модальное окно, как и при создании:
        # все поля заполнены теми же данными, проверим это на примере названия опроса
        surveys_page.click_edit_survey()
        assert surveys_page.is_survey_creation_modal_opened
        assert surveys_page.is_survey_name_set('test_survey_edit')
        # Изменим название опроса и сохраним его (для этого надо 3 раза нажать "Продолжить")
        surveys_page.set_survey_name('edited_test_survey')
        surveys_page.click_next_step_button(3)
        # перезагружаем страницу ещё раз и видим, что название формы и правда поменялось
        surveys_page.open_and_wait()
        assert surveys_page.is_element_in_list('edited_test_survey')

    def test_archive(self, surveys_page):
        # создадим тестовый опрос
        surveys_page.create_example_survey('test_archive')
        # архивируем его
        surveys_page.archive_survey()
        # перезагружаем страницу и убеждаемся, что форма архивирована
        surveys_page.open_and_wait()
        surveys_page.select_archive_category()
        assert surveys_page.is_element_in_list('test_archive')
        # теперь восстанавливаем форму
        surveys_page.restore_survey('test_archive')
        # перезагружаем страницу и убеждаемся, что форма восстановлена
        surveys_page.open_and_wait()
        assert surveys_page.is_element_in_list('test_archive')

    def test_search(self, surveys_page):
        # создадим тестовый опрос
        surveys_page.create_example_survey('test_search')
        # в поисковой строке введем название созданного опроса
        surveys_page.search_survey('test_search')
        # убедимся, что опрос найден
        assert surveys_page.is_element_in_list('test_search')
        # очистим поисковую строку и введём несуществующий опрос
        surveys_page.clear_search()
        surveys_page.search_survey('abc')
        assert not surveys_page.is_element_in_list('abc')
