import pytest
from selenium import webdriver
from TextBoxForm import TextBoxForm


@pytest.fixture(scope="function")
def driver():
    # Создаем объект опций
    options = webdriver.ChromeOptions()
    # Добавляем аргумент для скрытого запуска (без окна)
    options.add_argument("--headless")
    # Окно в fhd, потому что падает на маленьком экране из-за того что кнопку не видит
    options.add_argument("--window-size=1920,1080")

    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.fixture(scope="function")
def text_box_page(driver):
    return TextBoxForm(driver).open()