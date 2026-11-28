# cd test/hw_pytest/home_work_3/Pytest_3_allure_and_co/HW3
# pytest TestTextBoxForm.py -v
# pytest -m smoke -s
# pytest -m regression -s
# allure serve allure-results сделать отчет в аллюр
# rm -rf allure-results очистить папку с результатми аллюр, потому что там все сохраняется

# параметр -k поддерживает логические выражения and, or и not
# параметр -m запускает только те тесты, которые помечены определёнными маркерами - декораторами
# параметр -s отключает перехват вывода и позволяет видеть в терминале всё, что тесты печатают через print()

import pytest
import allure

#from test.hw_pytest.home_work_1.TextBox.conftest import text_box_page
#from test.hw_pytest.home_work_3.Pytest_3_allure_and_co.HW3.conftest import text_box_page


@allure.epic('Веб форма')
@allure.feature("Форма ввода")
class TestTextBox:

    @allure.story("Успешное заполнение")
    @allure.title('Успешное заполнение имени и имейла')
    @allure.description("В этом кейсе поля имя и имейл заполнены валидными данными")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "full_name, email, expected_name, expected_email",
        [("Климов Артур", "ivan@example.com", "Климов Артур", "ivan@example.com")],
    )
    def test_valid_full_name_and_email(
            self, text_box_page, full_name, email, expected_name, expected_email
    ):
        text_box_page.fill_full_name(full_name).fill_email(email).submit()

        assert text_box_page.get_name() == expected_name
        assert text_box_page.get_email() == expected_email

    @allure.story("Успешное заполнение")
    @allure.title('Успешное заполнение имени только числами')
    @allure.description("В этом кейсе проверка что имя принимает числа")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "full_name, expected_name",
        [("12345 6789", "12345 6789")],
    )
    def test_valid_full_name_only_numbers(self, text_box_page, full_name, expected_name):
        text_box_page.fill_full_name(full_name).submit()
        assert text_box_page.get_name() == expected_name

    @allure.story("Успешное заполнение")
    @allure.title('Успешное заполнение адресов current и permanent ')
    @allure.description("В этом кейсе поля только с адресами заполнены валидными данными")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "current_address, permanent_address, expected_current, expected_permanent",
        [(
                "Санкт-Петербург, Маршала Казакова 10 к 1",
                "Санкт-Петербург, Хасанская 117",
                "Санкт-Петербург, Маршала Казакова 10 к 1",
                "Санкт-Петербург, Хасанская 117",
        )],
    )
    def test_valid_current_and_permanent_address(
            self, text_box_page, current_address, permanent_address,
            expected_current, expected_permanent,
    ):
        text_box_page.fill_current_address(current_address) \
            .fill_permanent_address(permanent_address) \
            .submit()

        assert text_box_page.get_current_address() == expected_current
        assert text_box_page.get_permanent_address() == expected_permanent

    @allure.story("Успешное заполнение")
    @allure.title('Успешное заполнение всех полей')
    @allure.description("В этом кейсе все поля заполнены валидными данными")
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "full_name, email, expected_name, expected_email, current_address, permanent_address, expected_current, expected_permanent",
        [("Климов Артур", "ivan@example.com", "Климов Артур", "ivan@example.com",
          "Санкт-Петербург, Маршала Казакова 10 к 1",
          "Санкт-Петербург, Хасанская 117",
          "Санкт-Петербург, Маршала Казакова 10 к 1",
          "Санкт-Петербург, Хасанская 117",)],
    )
    def test_all_filled_fields(self, text_box_page, full_name, email, current_address, permanent_address, expected_name,
                               expected_email, expected_permanent, expected_current):
        text_box_page.fill_full_name(full_name).fill_email(email).fill_current_address(
            current_address).fill_permanent_address(permanent_address).submit()

        assert text_box_page.get_name() == expected_name
        assert text_box_page.get_email() == expected_email
        assert text_box_page.get_current_address() == expected_current
        assert text_box_page.get_permanent_address() == expected_permanent

    @allure.story("Негативный тест")
    @allure.title('Невалидный формат имейл')
    @allure.description("В этом кейсе имейл заполнен невалдиным знаечнием")
    @pytest.mark.smoke
    @pytest.mark.parametrize("email", ["example.com"])
    def test_wrong_email_format(self, text_box_page, email):
        text_box_page.fill_email(email).submit()
        error_text = text_box_page.email_field_error()

        assert "должен содержать символ" in error_text or "@" in error_text, \
            f"Ожидали ошибку о неверном формате email, но получили: '{error_text}'"

    @allure.story("Негативный тест")
    @allure.title('Неверное имя')
    @allure.description("В этом кейсе специально неверные параметры что бы был упавший")
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "full_name, expected_name",
        [("12345 6789", "555")],
    )
    def test_special_broken(self, text_box_page, full_name, expected_name):
        text_box_page.fill_full_name(full_name).submit()
        assert text_box_page.get_name() == expected_name

