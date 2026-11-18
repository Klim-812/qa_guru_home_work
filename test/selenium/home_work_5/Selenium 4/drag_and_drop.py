import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Инициализация браузера
driver = webdriver.Chrome()

try:
    # Открытие тестового сайта
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    time.sleep(3)
    
    # Находим элементы для перемещения
    source_element = driver.find_element(By.ID, "column-a")
    target_element = driver.find_element(By.ID, "column-b")
    title_element = driver.find_element(By.XPATH,"//h3[text()='Drag and Drop']")
    
    # Создаем цепочку действий для Drag and Drop
    actions = ActionChains(driver)

    # Зажимаем элемент A, переносим на B и отпускаем
    actions.drag_and_drop(source_element, target_element).perform()
    
    # Задержка для наглядности
    time.sleep(3)

    # Зажимаем элемент B, перетягиваем на заголовок и отпускаем
    actions.click_and_hold(source_element).move_to_element(title_element).release().perform()
    time.sleep(3)

finally:
    # Закрытие браузера
    driver.quit()
