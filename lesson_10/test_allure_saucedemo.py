import allure
import pytest
from selenium import webdriver
from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage


LOGIN = "standard_user"
PASSWORD = "secret_sauce"
PRODUCTS = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
FIRST_NAME = "Александр"
LAST_NAME = "Сударчиков"
POSTAL_CODE = "453560"
EXPECTED_TOTAL = "58.29"


@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест полной покупки трех товаров")
@allure.description("Проверяем что можно добавить 3 товара и итоговая сумма равна $58.29")
class TestCompletePurchase:

    @pytest.fixture
    def driver(self):

        with allure.step("Настраиваем браузер Firefox"):
            driver = webdriver.Firefox()
            driver.maximize_window()
            yield driver
        with allure.step("Закрываем браузер"):
            driver.quit()

    @allure.title("Полный цикл: вход → добавление → оформление")
    def test_complete_purchase(self, driver):

        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("1. Открываем сайт и авторизуемся"):
            login_page.open()
            login_page.login(LOGIN, PASSWORD)
            allure.attach(f"Вход выполнен как {LOGIN}", name="Авторизация")

        with allure.step("2. Добавляем товары в корзину"):
            products_to_add = PRODUCTS
            for product in products_to_add:
                with allure.step(f"Добавляем товар: {product}"):
                    main_page.add_product_to_cart_by_name(product)
            allure.attach(f"Добавлено товаров: {len(products_to_add)}", name="Корзина")

        with allure.step("3. Переходим в корзину"):
            main_page.go_to_cart()

        with allure.step("4. Проверяем наличие товаров в корзине"):
            for product in products_to_add:
                with allure.step(f"Проверяем товар: {product}"):
                    cart_page.verify_product_in_cart(product)

        with allure.step("5. Нажимаем Checkout"):
            cart_page.proceed_to_checkout()

        with allure.step("6. Заполняем информацию о покупателе"):
            checkout_page.fill_shipping_info(
                first_name=FIRST_NAME,
                last_name=LAST_NAME,
                postal_code=POSTAL_CODE
            )

        with allure.step("7. Переходим к просмотру заказа"):
            checkout_page.continue_to_overview()

        with allure.step("8. Получаем итоговую стоимость"):
            total = checkout_page.get_total_price()
            allure.attach(f"Получена сумма: ${total}", name="Итоговая стоимость")
            print(f"Итоговая стоимость на странице: ${total}")

        with allure.step("9. Проверяем что сумма равна ожидаемой"):
            expected = EXPECTED_TOTAL
            with allure.step(f"Ожидаемая сумма: ${expected}, Фактическая: ${total}"):
                assert total == expected, f"Ожидалась сумма ${expected}, но получено ${total}"
                print(f"Тест пройден! Сумма ${total} совпадает с ожидаемой ${expected}")
