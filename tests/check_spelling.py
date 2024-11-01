from playwright.sync_api import sync_playwright
from spellchecker import SpellChecker

# Initialize the spell checker
spell = SpellChecker()

# Launch Playwright to open and scrape the web page
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Set `headless=False` to see the browser window
    page = browser.new_page()
    page.goto("https://es.lipsum.com/")  # Replace with the URL you want to test

    # Extract visible text content from the body of the page
    page_text = page.inner_text("body")

    # Split the text into individual words and check for misspellings
    words = page_text.split()
    misspelled = spell.unknown(words)

    if misspelled:
        print("Misspelled words found:")
        for word in misspelled:
            print(f"- {word}")
    else:
        print("No spelling mistakes found.")

    # Close the browser
    browser.close()
