import pytest
from pages.register_page import RegisterPage
import time

@pytest.mark.ui 

def test_register_success(driver):
    register_page = RegisterPage(driver)

    register_page.open()
    register_page.fill_username("Cuco09")
    register_page.fill_first_name("Cuco")
    register_page.fill_last_name("Castillo")
    register_page.fill_password("Cuco__@2020")
    time.sleep(3)
    register_page.click_register()
    

    time.sleep(3)

    #Assert

    success_message = driver.find_element("css selector", ".alert-success").text
    assert success_message == "Registration is successful"

    time.sleep(5)

