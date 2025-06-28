from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TextBoxPage(BasePage):
    URL = "https://demoqa.com/text-box"

    NAME_FIELD = (By.ID, "userName")
    EMAIL_FIELD = (By.ID, "userEmail")
    CURRENT_ADDRESS_FIELD = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_FIELD = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.URL)

    def fill_form(self, name, email, current_address, permanent_address):
        self.send_keys(self.NAME_FIELD, name)
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.CURRENT_ADDRESS_FIELD, current_address)
        self.send_keys(self.PERMANENT_ADDRESS_FIELD, permanent_address)
        self.click(self.SUBMIT_BUTTON)

    def get_output_name(self):
        return self.get_text(self.OUTPUT_NAME)

    def get_output_email(self):
        return self.get_text(self.OUTPUT_EMAIL)

    def get_output_current_address(self):
        return self.get_text(self.OUTPUT_CURRENT_ADDRESS)

    def get_output_permanent_address(self):
        return self.get_text(self.OUTPUT_PERMANENT_ADDRESS)