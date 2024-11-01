import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_name():
    return os.getenv("BROWSER_NAME", "chromium")  # Default to Chromium if not set

def test_example(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        title = page.title()
        assert title == "Example Domain"
        browser.close()
