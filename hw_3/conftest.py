import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_settings():
    browser.config.driver_name = "firefox"
    browser.config.window_height = 1024
    browser.config.window_width = 768
