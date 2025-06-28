import pytest
import allure
from pages.text_box_page import TextBoxPage
from utils.logger import get_logger
from faker import Faker

logger = get_logger("TextBoxTests")
fake = Faker()

# Статичные данные
static_test_data = [
    ("John Doe", "john@example.com", "Main St", "Oak Rd"),
    ("", "", "", ""),  # пустые поля
    ("Alice", "invalid-email", "Some Address", ""),  # невалидный email
]


# Генератор случайных данных
def generate_fake_data():
    return (
        fake.name(),
        fake.email(),
        fake.address().replace("\n", " "),
        fake.city()
    )


@allure.feature("Text Box Form")
@allure.story("Form submission with multiple scenarios")
@allure.title("Test form submission: {name}, {email}")
@allure.severity(allure.severity_level.NORMAL)

@pytest.mark.parametrize("name, email, current_address, permanent_address", static_test_data + [generate_fake_data()])
def test_teхt_box_submission_parametrized(driver, name, email, current_address, permanent_address):
    logger.info(f"Running test with: {name}, {email}, {current_address}, {permanent_address}")

    page = TextBoxPage(driver)

    with allure.step("Открытие страницы"):
        page.open()
        allure.attach(driver.get_screenshot_as_png(), name="step_open", attachment_type=allure.attachment_type.PNG)

    with allure.step(f"Заполнение формы: {name}, {email}, {current_address}, {permanent_address}"):
        page.fill_form(name, email, current_address, permanent_address)
        allure.attach(driver.get_screenshot_as_png(), name="step_fill_form", attachment_type=allure.attachment_type.PNG)

    try:
        with allure.step("Проверка результатов формы"):
            if "@" not in email and email:
                with allure.step("Невалидный email — проверяем отсутствие результата"):
                    with pytest.raises(Exception):
                        page.get_output_email()
            else:
                assert page.get_output_name() == f"Name:{name}" if name else True
                assert page.get_output_email() == f"Email:{email}" if email else True
                assert page.get_output_current_address() == f"Current Address :{current_address}" if current_address else True
                assert page.get_output_permanent_address() == f"Permananet Address :{permanent_address}" if permanent_address else True

        allure.attach(driver.get_screenshot_as_png(), name="step_check_results", attachment_type=allure.attachment_type.PNG)
        logger.info("Тест прошёл успешно")

    except Exception as e:
        with allure.step("Ошибка выполнения теста"):
            logger.error(f"Ошибка в тесте {name}, {email}: {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="error_screenshot", attachment_type=allure.attachment_type.PNG)
        raise

