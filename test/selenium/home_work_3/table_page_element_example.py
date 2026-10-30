import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# TODO: 4) Переписать используя PageFactory (Lesson 5)

# TODO: 2) Добана работа с таблицей 2 (проверки со строки 83)
# TODO: 3) Добавить TC в которых идет работа сразу с 2-я таблицами (проверки со строки 87)

# 1. Реализация Page Element для таблицы
class TableElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @property
    def element(self):
        return self.driver.find_element(*self.locator)

    def get_headers(self) -> list[str]:
        """Возвращает список заголовков таблицы."""
        header_elements = self.element.find_elements(By.CSS_SELECTOR, "thead th")
        return [header.text for header in header_elements]

    def get_row_data(self, row_index: int) -> list[str]:
        """Возвращает данные конкретной строки по её индексу (начиная с 0)."""
        rows = self.element.find_elements(By.CSS_SELECTOR, "tbody tr")
        cells = rows[row_index].find_elements(By.TAG_NAME, "td")
        return [cell.text for cell in cells]

    def get_cell_value(self, row_index: int, column_index: int) -> str:
        cells = self.get_row_data(row_index)
        # TODDO: 1) как переписать используя вызов get_row_data ? Переписан
        return cells[column_index]


# 2. Пример использования (Скрипт теста)
if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        # Открытие страницы
        driver.get("https://the-internet.herokuapp.com/tables")

        # Инициализация таблицы как Page Element через её локатор
        table1_locator = (By.ID, "table1")
        table_1 = TableElement(driver, table1_locator)
        table2_locator = (By.ID, "table2")
        table_2 = TableElement(driver, table2_locator)

        # Сбор данных для демонстрации
        headers_table_1 = table_1.get_headers()
        first_row_table_1 = table_1.get_row_data(0)
        specific_cell_table_1 = table_1.get_cell_value(row_index=2, column_index=3)  # Строка 3, Колонка 4 (Due)
        last_row_table_1 = table_1.get_row_data(-1)

        headers_table_2 = table_2.get_headers()
        last_row_table_2 = table_2.get_row_data(-1)
        specific_cell_table_2 = table_2.get_cell_value(1, 3)  # Строка 2, Колонка 4 (Due)
        first_row_table_2 = table_2.get_row_data(0)

        # Вывод результатов в консоль
        print("Заголовки первой таблицы:", headers_table_1)
        print("Первая строка данных первой таблицы:", first_row_table_1)
        print(f"Значение в строке 3, колонке 'Due' первой таблицы: {specific_cell_table_1}")

        print("Заголовки второй таблицы:", headers_table_2)
        print("Первая строка данных второй таблицы:", last_row_table_2)
        print(f"Значение в строке 2, колонке 'Due' второй таблицы: {specific_cell_table_2}")

        print("Заголовки таблиц одинаковые, данные в первой и последней строках обеих таблиц одинаковые ")

        # Простые проверки (Assertions)
        assert "Last Name" in headers_table_1, "Заголовок 'Last Name' не найден"
        assert "Smith" in first_row_table_1, "Фамилия 'Smith' должна быть в первой строке"
        assert specific_cell_table_1 == "$100.00", f"Ожидалось $100.00, но получено {specific_cell_table_1}"

        # Проверки со второй таблицей
        assert "First Name" in headers_table_2, "Проверка что в заголовках есть 'First Name'"
        assert "Conway" and "tconway@earthlink.net" in last_row_table_2, "Проверка что в последней строке 'Conway' и его имейл"
        assert specific_cell_table_2 == "$51.00", "Проверка что в строке 2, стоимость '51$'"

        # Проверки с обеими таблицами
        assert headers_table_1 == headers_table_2, "Проверка что заголовки в таблицах одинаковые"
        assert first_row_table_1 == first_row_table_2, "Проверка что первые строки в таблицах одинаковые"
        assert last_row_table_1 == last_row_table_2, "Проверка что последние строки в таблицах одинаковые"

        print("\n✅ Тест таблиц 1 и 2 успешно пройден!")
        time.sleep(5)

    finally:
        driver.quit()
