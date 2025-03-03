import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Browser settings
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'
    WINDOW_SIZE = {'width': 1920, 'height': 1080}
    
    # Timeouts
    IMPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 30
    
    # Test data
    BASE_URL = os.getenv('BASE_URL', 'https://example.com')
    USERNAME = os.getenv('USERNAME', 'test_user')
    PASSWORD = os.getenv('PASSWORD', 'test_password')
    
    # Report settings
    REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
    SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, 'screenshots')
    
    # Create directories if they don't exist
    os.makedirs(REPORTS_DIR, exist_ok=True)
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True) 