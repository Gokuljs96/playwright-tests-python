# tests/test_example.py

from playwright.sync_api import sync_playwright
from pages.home_page import HomePage


def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the website
        page.goto("https://example.com")
        home_page = HomePage(page)

        # Check the header text
        header_text = home_page.get_header_text()
        print("Header text:", header_text)
        assert header_text == "Example Domain"

        browser.close()
