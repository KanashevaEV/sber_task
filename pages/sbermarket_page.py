import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import *

class SbermarketingActions(BasePage):
    def presence_of_logo(self):
        enter_button = self.is_element_present(By.XPATH, '//a[@class="header__mrm"]')
        enter_button.click()
        self.switch_to()
        with allure.step('Проверяем, что отображается лого'):
            self.is_element_present(By.PARTIAL_LINK_TEXT, 'http://www.w3.org/1999/xlink')

    def presence_of_mail_field(self):
        self.do_click(ENTER_BUTTON)
        self.switch_to()
        with allure.step('Проверяем, что отображается поле ввода почты'):
            self.is_element_present(By.XPATH, '//input[@id="firstInput"]')

    def presence_of_password_field(self):
        self.do_click(ENTER_BUTTON)
        self.switch_to()
        with allure.step('Проверяем, что отображается поле ввода пароля'):
            self.is_element_present(By.XPATH, '//input[@id="secondInput"]')

    def presence_of_enter_button(self):
        self.do_click(ENTER_BUTTON)
        self.switch_to()
        with allure.step('Проверяем, что отображается кнопка входа'):
            self.is_element_present(By.XPATH, '//div[@id="saveButton"]')