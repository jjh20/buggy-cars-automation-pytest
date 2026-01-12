
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


