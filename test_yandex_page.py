import allure
from pages.yandex_page import YandexActions
import pytest


class TestYandex():
    link = 'https://ya.ru/'

    @allure.testcase('Проверяем поиск в Яндексе')
    def test_yandex_search(self, driver):
        page = YandexActions(driver, self.link)
        page.open()
        page.yandex_search()

    #встроена параметремизация, тк не понятно, что именно является критереем верной работы сайта
    @allure.testcase('Проверяем что переход на сайт отработал верно')
    @pytest.mark.parametrize(
        "function_name",
        [
            ("presence_of_main_picture"),
            ("presence_of_logo"),
            ("presence_of_mrm")
        ]
    )
    def test_presence_of_elements(self, driver, function_name):
        page = YandexActions(driver, self.link)
        page.open()
        function = getattr(YandexActions, function_name)
        function(page)
        return page