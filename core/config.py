"""Configuration for enterprise testing framework."""

import os
from dotenv import load_dotenv

load_dotenv()

# Application settings
BASE_URL = os.getenv("BASE_URL", "https://saucedemo.com")  # Default demo app
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

# Browser settings
BROWSER_NAME = os.getenv("BROWSER_NAME", "chromium")
VIEWPORT_WIDTH = int(os.getenv("VIEWPORT_WIDTH", "1920"))
VIEWPORT_HEIGHT = int(os.getenv("VIEWPORT_HEIGHT", "1080"))

# Test data (demo credentials)
DEMO_USERNAME = os.getenv("DEMO_USERNAME", "standard_user")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD", "secret_sauce")