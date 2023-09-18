import allure
from pages.google_page import GoogleActions


class TestGoogle():
    link = 'https://www.google.ru/'

    @allure.testcase('Проверяем поиск в Гугл')
    def test_google_search(self, driver):
        page = GoogleActions(driver, self.link)
        page.open()
        page.google_search()
