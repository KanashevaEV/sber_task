import allure
from pages.sbermarket_page import SbermarketingActions
import pytest


class TestSbermarketing():
    link = 'https://sbermarketing.ru/'

    # встроена параметремизация, тк не понятно, что именно является критереем верного перехода на страницу авторизации
    @allure.testcase('Проверяем, что отработал переход на страницу авторизации')
    @pytest.mark.parametrize(
        "function_name",
        [
            ("presence_of_logo"),
            ("presence_of_mail_field"),
            ("presence_of_password_field"),
            ("presence_of_enter_button")
        ]
    )
    def test_presence_of_elements(self, driver, function_name):
        page = SbermarketingActions(driver, self.link)
        page.open()
        function = getattr(SbermarketingActions, function_name)
        function(page)
        return page
