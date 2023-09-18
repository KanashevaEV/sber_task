from selenium.webdriver.common.by import By

YANDEX_SEARCH_FIELD = (By.XPATH, '//input[@id="text"]')
YANDEX_SEARCH_BUTTON = (By.XPATH, '//button[text()="Найти"]')
YANDEX_RESULT = (By.PARTIAL_LINK_TEXT, 'https://sbermarketing.ru/')
GOOGLE_SEARCH_FIELD = (By.XPATH, '//textarea[@title="Поиск"]')
GOOGLE_SEARCH_BUTTON = (By.XPATH, '//div[2]//input[@value="Поиск в Google"]')
ENTER_BUTTON = (By.PARTIAL_LINK_TEXT, 'https://sbermarketing.ru/')
