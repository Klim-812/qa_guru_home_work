import pytest
import os

# функции и фикстуры для тудушек из домашки
@pytest.fixture
def auth_headers(request):
    # Получаем роль из indirect-параметра
    role = request.param

    # Просто возвращаем строку с токеном (или "None")
    if role == "User":
        return "Bearer user_token_123"
    elif role == "Admin":
        return "Bearer admin_token_456"
    else:  # Guest
        return "None"

def pytest_generate_tests(metafunc):
    if "dynamic_file_scenario" in metafunc.fixturenames:
        folder_path = "data"
        scenarios = []
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith((".txt", ".json")):
                    scenarios.append({
                        "id": filename,
                        "filepath": os.path.join(folder_path, filename)
                    })

        if not scenarios:
            scenarios = [{"id": "empty_folder", "filepath": None}]
        # Генерируем ID для отчетов (используем имя файла)
        ids = [scen["id"] for scen in scenarios]

        # Динамически параметризуем тест!
        metafunc.parametrize("dynamic_file_scenario",scenarios, ids=ids)
