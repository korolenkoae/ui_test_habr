import allure
import os

from example.base_page_old import BasePage
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


class MainPageLocators(object):
    # xpath кнопки входа в профиль
    PROFILE_LOGIN_BUTTON = (By.XPATH, "//div[@class='tm-dropdown']//div[@class='tm-dropdown__head']//*[name()='svg']")
    # xpath кнопки войти
    LOGIN_BUTTON = (By.XPATH, "//a[@class='tm-user-menu__auth-button']")
    # xpath поля Email
    EMAIL_LOGIN_INPUT = (By.XPATH, "//input[@id='email_field']")
    # xpath поля Password
    PASSWORD_LOGIN_INPUT = (By.XPATH, "//input[@id='password_field']")
    # xpath кнопки Sign in
    SIGN_IN_BUTTON = (By.XPATH, "//button[@name='go']")
    # xpath кнопки Sign in
    PROFILE_LOGIN_USER_BUTTON = (By.XPATH, "//div[@data-test-id='menu-toggle-user']//*[name()='svg']")
    # xpath кнопки Выход
    LOGOUT_BUTTON = (By.XPATH, "//span[contains(text(),'Выход')]")


class MainPage(BasePage):
    load_dotenv()
    email = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")
    login = os.environ.get("LOGIN")

    @allure.step("Логин в приложение: почта - {email}, пароль - {password}")
    def login_user(self, email=email, password=password):
        self.wait_and_click(*MainPageLocators.PROFILE_LOGIN_BUTTON)
        self.wait_and_click(*MainPageLocators.LOGIN_BUTTON)
        self.clear_and_set_value(*MainPageLocators.EMAIL_LOGIN_INPUT, email)
        password_field = self.browser.find_element(*MainPageLocators.PASSWORD_LOGIN_INPUT)
        password_field.send_keys(password)
        self.wait_and_click(*MainPageLocators.SIGN_IN_BUTTON)

    @allure.step("Клик на иконку профиля залогированным юзером")
    def click_profile_button(self):
        self.wait_and_click(*MainPageLocators.PROFILE_LOGIN_USER_BUTTON)

    @allure.step("Клик на кнопку Выход")
    def user_logout(self):
        self.click_profile_button()
        self.wait_and_click(*MainPageLocators.LOGOUT_BUTTON)
        self.wait_and_click(*MainPageLocators.PROFILE_LOGIN_BUTTON)
