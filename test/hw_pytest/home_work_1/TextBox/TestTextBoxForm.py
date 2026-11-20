# cd test/hw_pytest/home_work_1/TextBox
#pytest TestTextBoxForm.py -v
# pytest -m smoke -s
# pytest -m regression -s

# параметр -k поддерживает логические выражения and, or и not
# параметр -m запускает только те тесты, которые помечены определёнными маркерами - декораторами
# параметр -s отключает перехват вывода и позволяет видеть в терминале всё, что тесты печатают через print()

import pytest


class TestTextBox:

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

    @pytest.mark.regression
    @pytest.mark.parametrize(
        "full_name, expected_name",
        [("12345 6789", "12345 6789")],
    )
    def test_valid_full_name_only_numbers(self, text_box_page, full_name, expected_name):
        text_box_page.fill_full_name(full_name).submit()
        assert text_box_page.get_name() == expected_name

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
