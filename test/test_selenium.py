import pytest
from selenium import webdriver

driver = webdriver.Chrome()
url_selenium = 'https://www.selenium.dev/'
url_gitHub = 'https://github.com/'
url_dzen = "https://dzen.ru/"


@pytest.mark.selenium
def test_selenium():
    driver.get(url_selenium)

    assert driver.title == 'Selenium'
    assert driver.current_url == url_selenium


@pytest.mark.selenium
def test_github():
    driver.get(url_gitHub)

    assert driver.title == 'GitHub · Change is constant. GitHub keeps you ahead. · GitHub'
    assert driver.current_url == url_gitHub


@pytest.mark.selenium
def test_dzen():
    driver.get(url_dzen)

    assert "Dzen" in driver.title
