from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys("ipetrov@stepik.com")

    input4 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла