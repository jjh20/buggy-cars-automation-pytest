import pytest
from pages.register_page import RegisterPage
import time

@pytest.mark.ui 
def test_register_invalid_password(driver):
   register_page = RegisterPage(driver)
   
   register_page.open()
   register_page.fill_username("Cuco09")
   register_page.fill_first_name("Cuco")
   register_page.fill_last_name("Castillo")
   register_page.fill_password('Cuco2020')
   register_page.click_register()

   error_message = register_page.get_error_message()
   assert "Password must have symbol characters" in error_message




