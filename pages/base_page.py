from selenium.common.exceptions import NoSuchElementException
import allure
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage():
    def __init__(self, driver, url, timeout=10):
        self.window_handles = None
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def do_send_text(self, text):
        with allure.step('Вводим текст'):
            ActionChains(self.driver).send_keys(text).perform()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_element(self, how, what):
        assert self.is_element_present(how, what), "Element is not presented"

    def switch_to(self, driver):
        new_window = self.window_handles[1]
        driver.switch_to.window(new_window)
