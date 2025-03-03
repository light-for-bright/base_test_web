import pytest
from ..pages.login_page import LoginPage
from ..utils.driver_factory import DriverFactory
from ..config.config import Config
import allure

@pytest.fixture(scope="function")
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

class TestLogin:
    @allure.title("Test successful login")
    @allure.description("Test login with valid credentials")
    def test_successful_login(self, login_page):
        login_page.open()
        login_page.login(Config.USERNAME, Config.PASSWORD)
        assert login_page.is_logged_in(), "Login failed"
    
    @allure.title("Test failed login")
    @allure.description("Test login with invalid credentials")
    def test_failed_login(self, login_page):
        login_page.open()
        login_page.login("invalid_user", "invalid_password")
        assert not login_page.is_logged_in(), "Login should not be successful"
        assert login_page.get_error_message(), "Error message should be displayed"
    
    @allure.title("Test empty credentials")
    @allure.description("Test login with empty credentials")
    def test_empty_credentials(self, login_page):
        login_page.open()
        login_page.login("", "")
        assert not login_page.is_logged_in(), "Login should not be successful"
        assert login_page.get_error_message(), "Error message should be displayed" 