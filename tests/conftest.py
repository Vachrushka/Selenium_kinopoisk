import json
import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    with open('tests/browser_config.json', 'r', encoding='utf-8') as f:
        browser_config = json.load(f)
    #browser = browser_config["browser"]
    resolution = browser_config["resolution"]
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(resolution["width"], resolution["height"])
    yield driver
    driver.quit()