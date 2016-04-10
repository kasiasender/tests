from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Page(object):
    def __init__(self, driver, base_url="http://demo.opencart.com/"):
        self.base_url = base_url
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_titile(self):
        return self.driver.title

    def check_element_exists(self, *locator):
        try:
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True



    def wait_for_element(self, *locator):
        return WebDriverWait(self.driver, 30).until(lambda self: self.find_element(*locator))
