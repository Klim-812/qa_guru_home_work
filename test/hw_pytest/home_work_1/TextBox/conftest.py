import pytest
from selenium import webdriver
from TextBoxForm import TextBoxForm


@pytest.fixture(scope="function")
def driver():
    drv = webdriver.Chrome()
    yield drv
    drv.quit()


@pytest.fixture(scope="function")
def text_box_page(driver):
    return TextBoxForm(driver).open()