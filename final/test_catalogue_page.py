from .pages.catalogue_page import CataloguePage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


link = "http://selenium1py.pythonanywhere.com/catalogue"


class TestCataloguePage:

    @pytest.mark.guest_order_routine
    class TestGuestOrderRoutine():
        # Тестовый сценарий 1.1.1 - Проверка листинга содержимого корня каталога
        def test_guest_can_view_catalogue(self, browser):
            # Arrange
            link = "http://selenium1py.pythonanywhere.com"
            page = MainPage(browser, link)
            page.open()
            # Act
            page.go_to_catalogue_page()
            catalogue_page = CataloguePage(browser, browser.current_url)
            # Assert
            catalogue_page.should_have_product()
            catalogue_page.go_to_next_catalogue_page()
            catalogue_page.should_have_product()

        def test_guest_init_price_in_mini_basket(self, browser):
            # Arrange
            page = CataloguePage(browser, link)
            # Act
            page.open()
            # Assert
            page.should_be_zero_init_price_in_basket()

        # Тестовый сценарий 1.2.1 - Проверка наполнения корзины товарами напрямую со страницы корня каталога
        @pytest.mark.parametrize('page',
                                 ["1", "2", "3", "4", "5"])
        def test_guest_can_add_item_to_basket_from_catalogue_page(self, browser, page):
            # Arrange
            link = f"http://selenium1py.pythonanywhere.com/catalogue/?page={page}"
            page = CataloguePage(browser, link)
            page.open()
            # Act
            page.add_first_available_item_to_basket()
            page.add_second_available_item_to_basket()
            # Assert
            page.should_match_price_in_basket_and_alert()

        # Тестовый сценарий 2.1.0 - Проверка содержимого корзины (начальное состояние)
        def test_guest_basket_validation(self, browser):
            # Arrange
            page = CataloguePage(browser, link)
            # Act
            page.open()
            page.go_to_basket_page()
            basket_page = BasketPage(browser, browser.current_url)
            # Assert
            basket_page.should_have_correct_totals_without_discount()
            basket_page.should_have_correct_totals()

        # Тестовый сценарий 2.1.1 - Изменение содержимого корзины через удаление
        @pytest.mark.xfail(reason="delete item from the basket feature is broken, known issue")
        def test_guest_delete_item(self, browser):
            # Arrange
            link = "http://selenium1py.pythonanywhere.com/basket"
            basket_page = BasketPage(browser, link)
            # Act
            basket_page.open()
            basket_page.should_have_correct_totals_without_discount()
            basket_page.should_have_correct_totals()
            basket_page.should_delete_item()
            # Assert
            basket_page.should_have_correct_totals_without_discount()
            basket_page.should_have_correct_totals()

        # Тестовый сценарий 2.2.1 - Оформление заказа без изменений и промокодов
        @pytest.mark.xfail(reason="guest checkout is broken, known issue")
        def test_guest_basket_checkout(self, browser):
            # Arrange
            link = "http://selenium1py.pythonanywhere.com/basket"
            basket_page = BasketPage(browser, link)
            # Act
            basket_page.open()
            basket_page.go_to_checkout()
            basket_page.fill_guest_checkout_form()
            # Assert
            basket_page.should_be_delivery_form()

    @pytest.mark.user_order_routine
    class TestUserOrderRoutine():
        @pytest.fixture(scope="class", autouse=True)
        def setup(self, browser):
            page = CataloguePage(browser, link)
            page.open()
            page.go_to_login_page()
            login_page = LoginPage(browser, browser.current_url)
            email = str(time.time()) + "@fakemail.org"
            login_page.register_new_user(email=email, password=email)
            login_page.should_be_authorized_user()

        # Тестовый сценарий 1.1.1 - Проверка листинга содержимого корня каталога
        def test_user_can_view_catalogue(self, browser):
            # Arrange
            link = "http://selenium1py.pythonanywhere.com"
            page = MainPage(browser, link)
            page.open()
            # Act
            page.go_to_catalogue_page()
            catalogue_page = CataloguePage(browser, browser.current_url)
            # Assert
            catalogue_page.should_have_product()
            catalogue_page.go_to_next_catalogue_page()
            catalogue_page.should_have_product()

        def test_user_init_price_in_mini_basket(self, browser):
            # Arrange
            page = CataloguePage(browser, link)
            # Act
            page.open()
            # Assert
            page.should_be_zero_init_price_in_basket()

        # Тестовый сценарий 1.2.1 - Проверка наполнения корзины товарами напрямую со страницы корня каталога
        @pytest.mark.parametrize('page',
                                 ["1", "2", "3", "4", "5"])
        def test_user_can_add_item_to_basket_from_catalogue_page(self, browser, page):
            # Arrange
            link = f"http://selenium1py.pythonanywhere.com/catalogue/?page={page}"
            page = CataloguePage(browser, link)
            page.open()
            # Act
            page.add_first_available_item_to_basket()
            page.add_second_available_item_to_basket()
            # Assert
            page.should_match_price_in_basket_and_alert()

        # Тестовый сценарий 2.1.0 - Проверка содержимого корзины (начальное состояние)
        def test_user_basket_validation(self, browser):
            # Arrange
            page = CataloguePage(browser, link)
            # Act
            page.open()
            page.go_to_basket_page()
            basket_page = BasketPage(browser, browser.current_url)
            # Assert
            basket_page.should_have_correct_totals_without_discount()
            basket_page.should_have_correct_totals()

        # Тестовый сценарий 2.1.1 - Изменение содержимого корзины через удаление
        @pytest.mark.xfail(reason="delete item from the basket feature is broken, known issue")
        def test_user_delete_item(self, browser):
            # Arrange
            link = "http://selenium1py.pythonanywhere.com/basket"
            basket_page = BasketPage(browser, link)
            # Act
            basket_page.open()
            basket_page.should_have_correct_totals_without_discount()
            basket_page.should_have_correct_totals()
            basket_page.should_delete_item()
            # Assert
            basket_page.should_have_correct_totals_without_discount()
            basket_page.should_have_correct_totals()

        # Тестовый сценарий 2.2.1 - Оформление заказа без изменений и промокодов
        def test_user_basket_checkout(self, browser):
            # Arrange
            link = "http://selenium1py.pythonanywhere.com/basket"
            basket_page = BasketPage(browser, link)
            # Act
            basket_page.open()
            basket_page.go_to_checkout()
            basket_page.should_be_delivery_form()
            basket_page.fill_user_delivery_form()
            basket_page.go_to_checkout()
            basket_page.should_be_payment_form()
            basket_page.go_to_checkout()
            basket_page.should_be_preview_url()
            basket_page.go_to_checkout()
            # Assert
            basket_page.should_be_thank_you_url()
