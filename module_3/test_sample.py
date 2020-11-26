"""
Тестовый сценарий 1.2.1 - Проверка наполнения корзины товарами напрямую со страницы корня каталога
Предусловия:
Начальное значение "Всего в корзине: 0,00 £", на странице имеются товары в наличии на складе.
Шаги:
- Шаг 1, открыть страницу http://selenium1py.pythonanywhere.com/ru/catalogue/ напрямую, ожидаемый результат - страница открылась успешно
- Шаг 2, клик по первой встречной кнопке "Добавить в корзину", ожидаемый результат - перезагрузка страницы с отображением алерта с текстом "Стоимость корзины теперь составляет"
- Шаг 3, сверяем значение поля "Всего в корзине: X £" со значением в тексте алерта "Стоимость корзины теперь составляет Y £", ожидаемый результат - значения совпадают
- Шаг 4, клик по второй встречной кнопке "Добавить в корзину", ожидаемый результат - перезагрузка страницы с отображением алерта с текстом "Стоимость корзины теперь составляет"
- Шаг 5, сверяем значение поля "Всего в корзине: X £" со значением в тексте алерта "Стоимость корзины теперь составляет Y £", ожидаемый результат - значения совпадают
- Шаг 6, клик по кнопке "Посмотреть корзину", ожидаемый результат - страница открылась успешно
"""

from selenium import webdriver
import time


# Data generale
catalogue_page_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
basket_mini_locator = ".basket-mini"
first_button_locator = "button.btn-primary"
basket_update_alert_locator = ".alert-info .alertinner p strong"


def test_basket_add_item():
    # Data specifique
    basket_init_price = "0,00"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(catalogue_page_link)
        # Начальное значение "Всего в корзине: 0,00 £"
        basket_price_value = browser.find_element_by_css_selector(basket_mini_locator).text.split(':')[1].split(' ')[1]
        assert basket_price_value == basket_init_price, \
            f"Expected \"{basket_init_price}\" for initial basket price, got \"{basket_price_value}\""

        # Act
        button_first = browser.find_element_by_css_selector(first_button_locator)
        button_first.click()

        # Assert
        alert_price_value = browser.find_element_by_css_selector(basket_update_alert_locator).text.split(' ')[0]
        basket_price_value = browser.find_element_by_css_selector(basket_mini_locator).text.split(':')[1].split(' ')[1]

        # Шаг 3, сверяем значение поля "Всего в корзине: X £" со значением в тексте алерта "Стоимость корзины теперь составляет Y £", ожидаемый результат - значения совпадают
        assert alert_price_value == basket_price_value, \
            f"Price in the alert and price in the basket should match."

    finally:
        # timeout just in case
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()


test_basket_add_item()

# не забываем оставить пустую строку в конце файла