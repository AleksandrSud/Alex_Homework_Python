from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    Класс для работы с главной страницей интернет-магазина SauceDemo

    На этой странице отображаются все товары, которые можно добавить в корзину
    """

    def __init__(self, driver):
        """
        Создает объект главной страницы
        """
        self.driver = driver
        # Ждем появления элементов до 10 секунд
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart_by_name(self, product_name: str):
        """
        Добавляет товар в корзину по его названию

        1. Ждет пока загрузятся все товары на странице
        2. Перебирает все товары и ищет нужный по названию
        3. Когда находит - нажимает кнопку "Add to cart"
        """
        # Ждем пока все товары загрузятся на странице
        inventory_items = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item"))
        )

        # Перебираем каждый товар
        for item in inventory_items:
            # Берем название текущего товара
            item_name = item.find_element(
                By.CLASS_NAME, "inventory_item_name").text

            # Если нашли нужный товар
            if item_name == product_name:
                # Находим кнопку добавления и кликаем
                add_button = item.find_element(By.CLASS_NAME, "btn_inventory")
                add_button.click()
                print(f"Товар '{product_name}' добавлен в корзину.")
                # Возвращаем себя для цепочки вызовов
                return self

        # Если товар не нашелся - ничего не возвращаем (None)
        print(f"Товар '{product_name}' не найден на странице")

    def go_to_cart(self):
        """
        Переходит на страницу корзины

        Что делает метод:
        1. Находит иконку корзины в правом верхнем углу
        2. Нажимает на нее
        3. Ждет пока загрузится страница корзины

        """
        # Находим иконку корзины и кликаем
        cart_button = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()
        print("Переходим в корзину")

        # Ждем пока загрузится страница корзины
        self.wait.until(
            EC.presence_of_element_located((By.ID, "cart_contents_container"))
        )

        return self
