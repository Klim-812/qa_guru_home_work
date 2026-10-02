import pytest
from selenium import webdriver

driver = webdriver.Chrome()
url_google = 'https://www.google.com/'
url_git = 'https://github.com/'

@pytest.mark.selenium
def test_selenium():
   driver.get(url_google)

   assert driver.title == 'Google'
   assert driver.current_url == url_google

@pytest.mark.selenium
def test_github():
   driver.get(url_git)

   assert driver.title == 'GitHub · Change is constant. GitHub keeps you ahead. · GitHub'
   assert driver.current_url == url_git
