from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)   # Start browser (not hidden)
        page = browser.new_page()                     # Open a new browser tab
        page.goto("https://www.google.com")           # Go to Google
        search = page.locator('textarea[name="q"], input[name="q"]')  # Find the search box
        search.fill("Playwright Python")              # Type into the search box
        page.keyboard.press("Enter")                  # Press Enter key
        page.wait_for_selector("#search")             # Wait until search results appear
        print("Title:", page.title())                 # Print the title of the page
        browser.close()                               # Close the browser

if __name__ == "__main__":
    run()

