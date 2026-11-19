# pytest test_main.py -s

#pytest -m smoke -s
#pytest -m integration -s
#pytest -m db_config -s

# pytest test_main.py -k "behavior" -s
# Параметр -k в pytest — это мощный инструмент для фильтрации и выборочного запуска тестов по их имени.
# pytest ищет совпадение указанной строки без учета регистра в названиях функций, классов, файлов или параметризованных вариантов тестов.
# параметр -k поддерживает логические выражения and, or и not

# Флаги -x / --maxfail для остановки тестов при первой ошибке.
# Флаг --lf (--last-failed) для перезапуска только упавших тестов.
# Использование кастомных маркеров через ключ -m (альтернатива фильтрации по имени).

import pytest
import time

# Маркируем весь класс как integration
@pytest.mark.integration
class TestLifecycle:
    def test_first(self, session_resource, module_resource, class_resource, function_resource):
        print(f"-> Исполнение test_first. Доступно: {function_resource}")
        assert function_resource == "Новые данные"

    @pytest.mark.smoke # Этот тест одновременно и smoke, и integration
    def test_second(self, session_resource, module_resource, class_resource, function_resource):
        print("-> Исполнение test_second")
        assert True

def test_file_exception(safe_file_driver):
    print(f"-> Исполнение теста с файлом:{safe_file_driver.name} и данным в нем: {safe_file_driver.read_text()}")
    # Провоцируем падение теста для демонстрации работы try/finally в yield
    assert False 

@pytest.mark.smoke
def test_parametrized_db(db_driver):
    print(f"-> Тестирование логики с базой: {db_driver}")
    assert db_driver in ["PostgreSQL", "MySQL", "MongoDB"]

# В test_standard_behavior фикстура dynamic_environment выдаст дефолтный read-only.
def test_standard_behavior(dynamic_environment):
    # Фикстура benchmark_and_logger отработает сама (autouse)
    print(f"-> Выполнение стандартного теста. Окружение: {dynamic_environment}")
    time.sleep(0.1) # Специально задержим, чтобы autouse-фикстура замерила время
    assert dynamic_environment["mode"] == "read-only"

# В test_production_behavior посредством dynamic_environment объект request успешно перехватит строку "production" из декоратора и переключит режим на read-write.
@pytest.mark.db_config("production")
def test_production_behavior(dynamic_environment):
    # Тест помечен маркером, фикстура request прочитает это и изменит словарь
    print(f"-> Выполнение prod-теста. Окружение: {dynamic_environment}")
    assert dynamic_environment["mode"] == "read-write"
    assert dynamic_environment["timeout"] == 30

