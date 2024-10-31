# pages/home_page.py

class HomePage:
    def __init__(self, page):
        self.page = page
        self.example_header = self.page.locator("h1")

    def get_header_text(self):
        return self.example_header.inner_text()
