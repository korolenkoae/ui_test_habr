import allure
from selenium.webdriver.common.by import By

from pages.main_page import MainPage, MainPageLocators
from tests.base_test import BaseTest


@allure.epic("Login tests")
class TestLogin(BaseTest):
    @allure.story("Login")
    @allure.title("Проверка успешного логина")
    def test_logout(self, browser):
        # Arrange
        mainpage = MainPage(browser, BaseTest.baseurl)  # Инициализируем mainpage
        mainpage.open(BaseTest.baseurl)  # Переходим на главную страницу
        mainpage.login_user()
        login = mainpage.login
        # Act
        mainpage.user_logout()
        # Assert
        with allure.step(f"Проверяем отсутствие контакта с почтой {login}"):
            xpath_selector = f"//a[contains(@class, 'tm-user-item__username') " \
                             f"and normalize-space(text())='{login}']"
            assert mainpage.is_not_element_present(By.XPATH, xpath_selector), f"пользователь {login} разлогирован"
