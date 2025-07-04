import allure
import pytest
from selenium import webdriver
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='test_run.log'
)
logger = logging.getLogger(__name__)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, "rep_" + call.when, outcome.excinfo)
    return outcome

@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Chrome()
    logger.info("Браузер запущен")

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call and hasattr(request.node.rep_call, "failed") and request.node.rep_call.failed:
        logger.error(f"Тест упал: {request.node.name}")
        os.makedirs("allure-results", exist_ok=True)
        driver.save_screenshot(f"allure-results/{request.node.name}_fail.png")
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

    driver.quit()
    logger.info("Браузер закрыт")






