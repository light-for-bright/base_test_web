from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ..config.config import Config

class DriverFactory:
    @staticmethod
    def get_driver(browser_name=None):
        """
        Get WebDriver instance based on browser name
        """
        browser = browser_name or Config.BROWSER

        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if Config.HEADLESS:
                options.add_argument('--headless')
            options.add_argument('--start-maximized')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )
            
        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if Config.HEADLESS:
                options.add_argument('--headless')
            
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
            
        else:
            raise ValueError(f"Browser {browser} is not supported")

        # Set timeouts
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        # Set window size
        driver.set_window_size(
            Config.WINDOW_SIZE['width'],
            Config.WINDOW_SIZE['height']
        )
        
        return driver 