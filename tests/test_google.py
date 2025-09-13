import pytest
from playwright.sync_api import Page
from pages.google_page import GooglePage

def test_google_search(page: Page):
    google = GooglePage(page)

    # Navigate and search
    google.navigate()
    google.search("Playwright Python")

    # Assert title
    assert "Playwright" in page.title()
