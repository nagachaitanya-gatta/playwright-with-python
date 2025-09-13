# 📘 Playwright with Python – Automation Framework

This is a **Python-based Playwright automation framework** built with **pytest**.  
It follows the **Page Object Model (POM)** and is designed to be **clean, scalable, and portfolio-ready**.  

## 🚀 Features
- ✅ Playwright with Python (sync API)  
- ✅ Page Object Model (POM) design pattern  
- ✅ Configurable base URL, browser, headless mode  
- ✅ Automatic screenshots on failure  
- ✅ Logging to console + file  
- ✅ HTML test reports (`pytest-html`)  
- ✅ Easy integration with CI/CD (GitHub Actions, Jenkins)  

Project Structure
playwright-python/
├─ pages/               # Page Objects
│  ├─ google_page.py
│  ├─ login_page.py
│  └─ dropdown_page.py
├─ tests/               # Test cases
│  ├─ test_google.py
│  ├─ test_login.py
│  └─ test_dropdown.py
├─ utils/               # Config & utilities
│  ├─ config.py
│  └─ logger.py
├─ conftest.py          # Pytest fixtures & hooks
├─ pytest.ini           # Pytest settings
├─ requirements.txt     # Python dependencies
└─ README.md            # Project documentation

⚙️ Setup Instructions
1. Clone the repo

git clone https://github.com/<your-username>/playwright-with-python.git
cd playwright-with-python

2. Create & activate virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Linux/Mac
# .venv\Scripts\activate    # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Install Playwright browsers & dependencies
python -m playwright install
python -m playwright install-deps   # only for Linux

Run all tests (headless by default):

pytest -q

Run in headed mode:
PLAYWRIGHT_HEADLESS=0 pytest -q

Run a specific test:
pytest tests/test_login.py -q

Run with markers (smoke, regression):
pytest -m smoke -q

Generate HTML report:
pytest --html=report.html -q

📊 Test Reports
HTML report: report.html
Screenshots on failure: stored in artifacts/screenshots/
Logs: stored in logs/test.log

🌐 Demo Website
Tests are executed against public demo sites like:
https://the-internet.herokuapp.com

🔮 Next Steps
Add CI/CD pipelines (GitHub Actions, Jenkins)
Add advanced test cases (file upload, downloads, shadow DOM, API testing)
Add parallel execution & cloud browser testing (BrowserStack, Playwright Cloud)