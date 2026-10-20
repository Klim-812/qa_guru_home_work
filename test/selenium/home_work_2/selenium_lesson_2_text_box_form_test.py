import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestTextBoxForm:
    URL = "https://qa-guru.github.io/one-page-form/text-box.html"

    FULL_NAME_FIELD = (By.ID, "userName")
    EMAIL_FIELD = (By.ID, "userEmail")
    CURRENT_ADDRESS_FIELD = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_FIELD = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT_DATA_BLOCK = (By.ID, "output")
    OUTPUT_DATA_NAME = (By.ID, "name")
    OUTPUT_DATA_EMAIL = (By.ID, "email")
    OUTPUT_DATA_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_DATA_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        yield
        self.driver.quit()

    def field_full_name(self, full_name):
        self.driver.find_element(*self.FULL_NAME_FIELD).send_keys(full_name)

    def field_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def field_current_address(self, current_address):
        self.driver.find_element(*self.CURRENT_ADDRESS_FIELD).send_keys(current_address)

    def field_permanent_address(self, permanent_address):
        self.driver.find_element(*self.PERMANENT_ADDRESS_FIELD).send_keys(permanent_address)

    def submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def output_data_block(self):
        self.wait.until(ec.visibility_of_element_located(self.OUTPUT_DATA_BLOCK))

    def output_data_name(self):
        self.wait.until(ec.visibility_of_element_located(self.OUTPUT_DATA_NAME))
        text = self.driver.find_element(*self.OUTPUT_DATA_NAME).text
        return text.replace("Name:", "").strip()

    def output_data_email(self):
        self.wait.until(ec.visibility_of_element_located(self.OUTPUT_DATA_EMAIL))
        text = self.driver.find_element(*self.OUTPUT_DATA_EMAIL).text
        return text.replace("Email:", "").strip()

    def output_data_current_address(self):
        self.wait.until(ec.visibility_of_element_located(self.OUTPUT_DATA_CURRENT_ADDRESS))
        text = self.driver.find_element(*self.OUTPUT_DATA_CURRENT_ADDRESS).text
        return text.replace("Current Address :", "").strip()

    def output_data_permanent_address(self):
        self.wait.until(ec.visibility_of_element_located(self.OUTPUT_DATA_PERMANENT_ADDRESS))
        text = self.driver.find_element(*self.OUTPUT_DATA_PERMANENT_ADDRESS).text
        return text.replace("Permananet Address :", "").strip()

    @pytest.mark.parametrize(
        "full_name, email, output_data_name, output_data_email", [
            ("Климов Артур", "ivan@example.com", "Климов Артур", "ivan@example.com")
        ])
    def test_valid_full_name_and_email(self, setup, full_name, email, output_data_name, output_data_email):
        self.field_full_name(full_name)
        self.field_email(email)
        self.submit_button()
        assert self.output_data_name() == output_data_name
        assert self.output_data_email() == output_data_email

    @pytest.mark.parametrize(
        "full_name, output_data_name", [
            ("12345 6789", "12345 6789")
        ])
    def test_valid_full_name_only_numbers(self, setup, full_name, output_data_name):
        self.field_full_name(full_name)
        self.submit_button()
        assert self.output_data_name() == output_data_name

    @pytest.mark.parametrize(
        "current_address, permanent_address, output_data_current_address, output_data_permanent_address", [
            ("Санкт-Петербург, Маршала Казакова 10 к 1", "Санкт-Петербург, Хасанская 117",
             "Санкт-Петербург, Маршала Казакова 10 к 1", "Санкт-Петербург, Хасанская 117")
        ])
    def test_valid_current_and_permanent_address(self, setup, current_address, permanent_address,
                                                 output_data_current_address, output_data_permanent_address):
        self.field_current_address(current_address)
        self.field_permanent_address(permanent_address)
        self.submit_button()
        assert self.output_data_current_address() == output_data_current_address
        assert self.output_data_permanent_address() == output_data_permanent_address


