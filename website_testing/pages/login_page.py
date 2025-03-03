from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..config.config import Config

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.BASE_URL}/login"
    
    def open(self):
        """Open login page"""
        self.driver.get(self.url)
        return self
    
    def login(self, username, password):
        """Perform login"""
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Get error message if present"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_logged_in(self):
        """Check if user is logged in"""
        return not self.is_element_present(self.LOGIN_BUTTON, timeout=3) 