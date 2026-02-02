from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_product_in_cart(self, product_name):
        cart_items = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
        )

        item_names = [item.find_element(
            By.CLASS_NAME, "inventory_item_name").text for item in cart_items]

        if product_name in item_names:
            print(f"Товар '{product_name}' успешно находится в корзине.")

    def proceed_to_checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        return self
