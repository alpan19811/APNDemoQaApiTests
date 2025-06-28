import pytest
from selenium import webdriver
from pages.text_box_page import TextBoxPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_teхt_box_submission(driver):
    page = TextBoxPage(driver)
    page.open()

    name = "John Doe"
    email = "john@example.com"
    current_address = "123 Main St, City"
    permanent_address = "456 Oak Rd, Town"

    page.fill_form(name, email, current_address, permanent_address)

    assert page.get_output_name() == f"Name:{name}"
    assert page.get_output_email() == f"Email:{email}"
    assert page.get_output_current_address() == f"Current Address :{current_address}"
    assert page.get_output_permanent_address() == f"Permananet Address :{permanent_address}"