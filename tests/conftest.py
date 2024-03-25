import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 800
    browser.config.window_height = 600

    yield

    browser.quit()
