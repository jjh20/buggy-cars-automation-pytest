from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegisterPage:
    URL = 'https://buggy.justtestit.org/register'


    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    # localizadores (tuplas)
    username_input = (By.ID, 'username')
    first_name_input = (By.ID, 'firstName')
    last_name_input = (By.ID, 'lastName')
    password_input = (By.ID, 'password')
    confirm_password_input = (By.ID, 'confirmPassword')
    register_button = (By.CSS_SELECTOR, '.btn-default')
    
    #Metodos
    def fill_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
    

    def fill_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirm_password_input).send_keys(password)


    def click_register(self):
        self.driver.find_element(*self.register_button).click()

    error_message = (By.CSS_SELECTOR, ".result")

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located(self.error_message))

        wait.until(lambda d: d.find_element(*self.error_message).text.strip() != "")

        
        return self.driver.find_element(*self.error_message).text