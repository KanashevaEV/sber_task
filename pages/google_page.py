import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators import *

class GoogleActions(BasePage):
    def google_search(self):
        self.do_click(GOOGLE_SEARCH_FIELD)
        self.do_send_text('sbermarketing')
        self.do_click(GOOGLE_SEARCH_BUTTON)
        with allure.step('Проверяем, что ссылка нашлась'):
            self.is_element_present(By.PARTIAL_LINK_TEXT, 'https://sbermarketing.ru/')