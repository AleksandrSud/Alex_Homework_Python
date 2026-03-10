from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс для работы со страницей входа на сайт SauceDemo

    Содержит методы для открытия страницы и авторизации пользователя
    """

    def __init__(self, driver):
        """
        Создает объект страницы входа

        Параметры:
        driver - драйвер браузера (например: Chrome, Firefox)
        """
        self.driver = driver
        # Ждем появления элементов до 10 секунд
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Открывает страницу входа в браузере

        Возвращает:
        Объект LoginPage (тот же самый) чтобы можно было писать цепочки вызовов
        Пример: login_page.open().login("user", "pass")
        """
        self.driver.get("https://www.saucedemo.com")
        return self

    def login(self, username: str, password: str):
        """
        Выполняет вход в систему с указанными данными

        Что делает метод:
        1. Ждет появления поля для логина и вводит логин
        2. Находит поле для пароля и вводит пароль
        3. Нажимает кнопку входа
        4. Ждет пока загрузится главная страница

        Параметры:
        username - логин пользователя (строка, например "standard_user")
        password - пароль пользователя (строка, например "secret_sauce")

        Возвращает:
        Объект LoginPage (тот же самый) для цепочки вызовов
        """
        # Вводим логин
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

        # Вводим пароль
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        # Нажимаем кнопку Login
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        # Ждем пока загрузится страница с товарами
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        return self
