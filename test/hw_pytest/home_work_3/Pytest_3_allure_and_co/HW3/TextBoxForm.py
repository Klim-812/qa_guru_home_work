import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TextBoxForm:
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

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        return self

    @allure.step("Ввод имени: {full_name}")
    def fill_full_name(self, full_name):
        self.driver.find_element(*self.FULL_NAME_FIELD).send_keys(full_name)
        return self

    @allure.step("Ввод имейл: {email}")
    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        return self

    @allure.step("Ввод current_address: {current_address}")
    def fill_current_address(self, current_address):
        self.driver.find_element(*self.CURRENT_ADDRESS_FIELD).send_keys(current_address)
        return self

    @allure.step("Ввод permanent_address: {permanent_address}")
    def fill_permanent_address(self, permanent_address):
        self.driver.find_element(*self.PERMANENT_ADDRESS_FIELD).send_keys(permanent_address)
        return self

    @allure.step("Нажатие на кнопку Submit")
    def submit(self):
        button = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.wait.until(ec.element_to_be_clickable(self.SUBMIT_BUTTON))
        button.click()
        return self

    def wait_output_block(self):
        self.wait.until(ec.visibility_of_element_located(self.OUTPUT_DATA_BLOCK))

    def email_field_error(self):
        field = self.driver.find_element(*self.EMAIL_FIELD)
        return self.driver.execute_script("return arguments[0].validationMessage;", field)


    def get_name(self):
        self.wait.until(ec.visibility_of_element_located(self.OUTPUT_DATA_NAME))
        text = self.driver.find_element(*self.OUTPUT_DATA_NAME).text
        return text.replace("Name:", "").strip()

    def get_email(self):
        self.wait.until(ec.visibility_of_element_located(self.OUTPUT_DATA_EMAIL))
        text = self.driver.find_element(*self.OUTPUT_DATA_EMAIL).text
        return text.replace("Email:", "").strip()

    def get_current_address(self):
        self.wait.until(ec.visibility_of_element_located(self.OUTPUT_DATA_CURRENT_ADDRESS))
        text = self.driver.find_element(*self.OUTPUT_DATA_CURRENT_ADDRESS).text
        return text.replace("Current Address :", "").strip()

    def get_permanent_address(self):
        self.wait.until(ec.visibility_of_element_located(self.OUTPUT_DATA_PERMANENT_ADDRESS))
        text = self.driver.find_element(*self.OUTPUT_DATA_PERMANENT_ADDRESS).text
        return text.replace("Permananet Address :", "").strip()