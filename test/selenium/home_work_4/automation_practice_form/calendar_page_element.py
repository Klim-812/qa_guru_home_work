from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from typing import Tuple

class CalendarPageElement:
    YEAR_OF_BIRTH_SELECT = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    MONTH_OF_BIRTH_SELECT = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    DAY_OF_BIRTH_SELECT = (By.CSS_SELECTOR, ".react-datepicker__week")

    def __init__(self, driver):
        self.driver = driver

    def set_date(self,date: Tuple[str, str, str]):
        Select(self.driver.find_element(*self.YEAR_OF_BIRTH_SELECT)).select_by_value(date[0])
        Select(self.driver.find_element(*self.MONTH_OF_BIRTH_SELECT)).select_by_value(date[1])
        self.driver.find_element(By.CSS_SELECTOR, f".react-datepicker__day--0{date[2]}[tabindex='0']").click()
