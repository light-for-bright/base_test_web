import pytest
import allure
import os
from datetime import datetime
from ..utils.driver_factory import DriverFactory
from ..config.config import Config

def pytest_configure(config):
    """Setup test configuration"""
    # Set up logging
    if not os.path.exists(Config.REPORTS_DIR):
        os.makedirs(Config.REPORTS_DIR)
    if not os.path.exists(Config.SCREENSHOTS_DIR):
        os.makedirs(Config.SCREENSHOTS_DIR)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Generate report for failed tests"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        try:
            driver = item.funcargs["driver"]
            take_screenshot(driver, item.name)
        except Exception as e:
            print(f"Failed to take screenshot: {e}")

def take_screenshot(driver, name):
    """Take screenshot on test failure"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"{name}_{timestamp}.png"
    screenshot_path = os.path.join(Config.SCREENSHOTS_DIR, screenshot_name)
    
    try:
        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        print(f"Failed to save screenshot: {e}")

@pytest.fixture(scope="session")
def base_url():
    """Return base URL from config"""
    return Config.BASE_URL

@pytest.fixture(scope="function")
def driver(request):
    """Create WebDriver instance"""
    driver = DriverFactory.get_driver()
    
    def fin():
        driver.quit()
    
    request.addfinalizer(fin)
    return driver 