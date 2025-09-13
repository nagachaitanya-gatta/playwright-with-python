# pages/google_page.py
from playwright.sync_api import Page

class GooglePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = "textarea[name='q'], input[name='q']"

    def navigate(self):
        self.page.goto("https://www.google.com")

    def search(self, text: str):
        self.page.locator(self.search_box).fill(text)
        self.page.keyboard.press("Enter")
        self.page.wait_for_load_state("networkidle")
