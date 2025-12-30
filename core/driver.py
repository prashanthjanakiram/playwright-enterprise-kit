"""Playwright browser context manager for enterprise testing."""

from playwright.sync_api import sync_playwright
from core.config import BASE_URL, HEADLESS

class PlaywrightDriver:
    def __init__(self, browser_name="chromium"):
        self.browser_name = browser_name
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
    
    def start(self):
        """Start browser context with enterprise defaults."""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright[self.browser_name].launch(
            headless=HEADLESS,
            slow_mo=1000 if not HEADLESS else 0
        )
        self.context = self.browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        self.page = self.context.new_page()
        self.page.goto(BASE_URL)
    
    def stop(self):
        """Clean browser shutdown."""
        if self.page:
            self.page.close()
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()