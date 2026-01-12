import pytest
from selenium import webdriver

@pytest.fixture

#configuracion
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()