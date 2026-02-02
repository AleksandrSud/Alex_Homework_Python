from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart_by_name(self, product_name):
        inventory_items = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item"))
        )

        for item in inventory_items:
            item_name = item.find_element(
                By.CLASS_NAME, "inventory_item_name").text
            if item_name == product_name:
                add_button = item.find_element(By.CLASS_NAME, "btn_inventory")
                add_button.click()
                print(f"Товар '{product_name}' добавлен в корзину.")
                return self

    def go_to_cart(self):
        cart_button = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()

        self.wait.until(
            EC.presence_of_element_located((By.ID, "cart_contents_container"))
        )
        return self
