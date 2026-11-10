import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Локаторы элементов формы на странице
LOGIN_INPUT     = (By.ID, "login-input")
PASSWORD_INPUT  = (By.ID, "password-input")
SUBMIT_BUTTON   = (By.ID, "submit-button")
STATUS_MESSAGE  = (By.ID, "error-message")
WELCOME_MESSAGE = (By.ID, "welcome-message")


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    #options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # Фоновый режим для CI/CD
    #options.add_argument("--window-size=1920,1080")    
    #driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


# Реализация DDT подхода через параметризацию pytest
@pytest.mark.parametrize(
    "email, password, expected_text",
    [
        # --- ПОЗИТИВНЫЕ СЦЕНАРИИ ---
        ("user1", "password1", "Welcome, user1!"),
        
        # --- НЕГАТИВНЫЕ СЦЕНАРИИ ---
        ("user2", "password1", "Wrong login or password"), # добавил негативный
        ("qaguru@qa.guru", "wrong_pass", "Wrong login or password"),
        ("unknown@qa.guru", "qaguru", "Wrong login or password"),
        ("", "qaguru", "Login is required (minimum 3 characters)"),
        ("qaguru@qa.guru", "", "Password is required (minimum 6 characters)"),
        ("", "", "Login and password are required (minimum 3 and 6 characters)"),
        ("qaguruqa.guru", "qaguru", "Wrong login or password"),
        ("qaguru@", "qaguru", "Wrong login or password"),
        ("@qa.guru", "qaguru", "Wrong login or password"),
        ("qaguru' OR '1'='1", "' OR '1'='1", "Wrong login or password"),
    ]
)
def test_login_form(driver, email, password, expected_text):
    """Тест кейс, принимающий наборы данных (DDT)."""
    
    # 1. Открытие тестируемой страницы
    driver.get("https://qa-guru.github.io/one-page-form/login.html")
    
    # 2. Поиск элементов формы
    email_field = driver.find_element(*LOGIN_INPUT)    
    password_field = driver.find_element(*PASSWORD_INPUT)    
    submit_button = driver.find_element(*SUBMIT_BUTTON)
    
    # 3. Очистка полей и ввод тестовых данных
    email_field.clear()
    email_field.send_keys(email)
    
    password_field.clear()
    password_field.send_keys(password)
    
    # 4. Клик по кнопке отправки формы
    submit_button.click()

    # 5. Ожидание появления ответа
    actual_result = ""

    time.sleep(5)

    try:
        # Проверяем, появился ли браузерный alert
        welcom_message = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(WELCOME_MESSAGE))
        actual_result = welcom_message.text
    except TimeoutException:
        # Если алерта нет, ищем текст на странице
        status_message = WebDriverWait(driver, 2).until(EC.visibility_of_element_located(STATUS_MESSAGE))
        actual_result = status_message.text

    # 6. Проверка результата (Assertion)
        assert expected_text in actual_result, f"Ожидаемый текст '{expected_text}', а полученный '{actual_result}'"