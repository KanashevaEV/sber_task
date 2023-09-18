import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import *


class YandexActions(BasePage):
    def yandex_search(self):
        self.do_click(YANDEX_SEARCH_FIELD)
        self.do_send_text('sbermarketing')
        self.do_click(YANDEX_SEARCH_BUTTON)
        with allure.step('Проверяем, что ссылка нашлась'):
            self.should_be_element(By.PARTIAL_LINK_TEXT, 'https://sbermarketing.ru/')

    def presence_of_main_picture(self):
        self.do_click(YANDEX_SEARCH_FIELD)
        self.do_send_text('sbermarketing')
        self.do_click(YANDEX_SEARCH_BUTTON)
        self.do_click(YANDEX_RESULT)
        with allure.step('Проверяем, что отображается картинка с девушкой'):
            self.should_be_element(By.PARTIAL_LINK_TEXT, 'https://sbermarketing.ru/local/templates/main/images/ico/arrow_down_white.svg')

    def presence_of_logo(self):
        self.do_click(YANDEX_SEARCH_FIELD)
        self.do_send_text('sbermarketing')
        self.do_click(YANDEX_SEARCH_BUTTON)
        self.do_click(YANDEX_RESULT)
        with allure.step('Проверяем, что отображается логотип'):
            self.should_be_element(By.PARTIAL_LINK_TEXT, 'https://sbermarketing.ru/local/templates/main/images/pic/logo.png')

    def presence_of_mrm(self):
        self.do_click(YANDEX_SEARCH_FIELD)
        self.do_send_text('sbermarketing')
        self.do_click(YANDEX_SEARCH_BUTTON)
        self.do_click(YANDEX_RESULT)
        with allure.step('Проверяем, что отображается вход в систему'):
            self.should_be_element(By.PARTIAL_LINK_TEXT, 'https://mrm.sbermarketing.ru/')

