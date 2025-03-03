from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    def find_element(self, locator, timeout=10):
        """Find element with wait"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            self.logger.error(f"Element {locator} not found on page")
            return None

    def click(self, locator):
        """Click on element"""
        element = self.find_element(locator)
        if element:
            element.click()
            return True
        return False

    def input_text(self, locator, text):
        """Input text into element"""
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False

    def get_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        if element:
            return element.text
        return None

    def is_element_present(self, locator, timeout=5):
        """Check if element is present"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_visible(self, locator, timeout=10):
        """Wait for element to be visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            self.logger.error(f"Element {locator} not visible after {timeout} seconds")
            return False 