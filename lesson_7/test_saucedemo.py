import pytest
from selenium import webdriver
from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from CheckPage import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_complete_purchase(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product in products_to_add:
        main_page.add_product_to_cart_by_name(product)

    main_page.go_to_cart()
    for product in products_to_add:
        cart_page.verify_product_in_cart(product)

    cart_page.proceed_to_checkout()

    checkout_page.fill_shipping_info(
        first_name="Александр",
        last_name="Сударчиков",
        postal_code="453560"
    ).continue_to_overview()

    total = checkout_page.get_total_price()
    print(f"Итоговая стоимость на странице: ${total}")

    assert total == "58.29", f"Ожидалась сумма $58.29, но получено ${total}"


if __name__ == "__main__":
    # Для запуска теста напрямую без pytest
    driver_instance = webdriver.Firefox()
    driver_instance.maximize_window()
    test_complete_purchase(driver_instance)
    driver_instance.quit()
