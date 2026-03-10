from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Класс для работы со страницей корзины интернет-магазина SauceDemo

    На этой странице отображаются все товары, которые пользователь
      добавил в корзину,
    и есть кнопка для перехода к оформлению заказа
    """
    def __init__(self, driver):
        """
        Создает объект страницы корзины
        """
        self.driver = driver
        # Ждем появления элементов до 10 секунд
        self.wait = WebDriverWait(driver, 10)

    def verify_product_in_cart(self, product_name: str):
        """
        Проверяет, есть ли товар в корзине
        1. Ждет пока загрузятся все товары в корзине
        2. Собирает названия всех товаров в список
        3. Проверяет, есть ли нужный товар в этом списке
        4. Если есть - выводит сообщение в консоль
        5. Если нет - ничего не делает (просто молча пропускает)
        """
        # Ждем пока все товары в корзине загрузятся
        cart_items = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
        )

        # Создаем список названий всех товаров в корзине
        item_names = [item.find_element(
            By.CLASS_NAME, "inventory_item_name").text for item in cart_items]

        # Проверяем есть ли наш товар в списке
        if product_name in item_names:
            print(f"Товар '{product_name}' успешно находится в корзине.")

    def proceed_to_checkout(self):
        """
        Переходит к оформлению заказа
        1. Ждет пока кнопка Checkout станет активной (можно нажать)
        2. Нажимает на кнопку Checkout
        3. Ждет пока загрузится страница оформления заказа (
        появится поле для имени)
        """
        # Ждем пока кнопка Checkout станет кликабельной и нажимаем
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        print("Нажимаем кнопку Checkout")

        # Ждем пока загрузится следующая страница
        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        print("Страница оформления загружена")

        return self
