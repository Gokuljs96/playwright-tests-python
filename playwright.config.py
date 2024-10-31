# playwright.config.py

from playwright.sync_api import sync_playwright

def pytest_configure(config):
    config.playwright = {
        "use": {
            "headless": True,            # Run tests in headless mode
            "screenshot": "only-on-failure",  # Take screenshots on failure
            "timeout": 60000             # 60 seconds timeout per test
        }
    }
