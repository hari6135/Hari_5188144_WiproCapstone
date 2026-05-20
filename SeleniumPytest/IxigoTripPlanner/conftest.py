import os
import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from utils.config_reader import ConfigReader
from utils.logger import LogGen

logger = LogGen.loggen()


@pytest.fixture(scope="function")
def driver():
    logger.info("==================================================")
    logger.info("Starting Test")

    browser = ConfigReader.get("browser").strip().lower()
    base_url = ConfigReader.get("base_url").strip()
    timeout = int(ConfigReader.get("timeout"))

    logger.info(f"Browser from config : {browser}")

    # CHROME
    if browser == "chrome":

        chrome_options = ChromeOptions()

        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(options=chrome_options)

    # EDGE
    else:

        edge_options = EdgeOptions()

        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-infobars")
        edge_options.add_argument("--disable-extensions")

        driver = webdriver.Edge(options=edge_options)

    logger.info(f"Opened Browser : {browser}")

    driver.get(base_url)

    logger.info(f"Loaded URL : {base_url}")

    # wait until page fully loads
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    logger.info("Page loaded successfully")

    # HANDLE POPUP
    try:

        logger.info("Checking for popup")

        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.ID, "wiz-iframe-intent")
            )
        )

        popup_close = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "closeButton")
            )
        )

        popup_close.click()

        driver.switch_to.default_content()

        logger.info("Popup closed successfully")

    except Exception as e:

        logger.info(f"No popup displayed : {e}")

    yield driver

    logger.info("Closing Browser")

    driver.quit()

    logger.info("Browser Closed")
    logger.info("------------------------------------------------")


# Allure test
def pytest_unconfigure(config):
    """
    This built-in Pytest hook runs exactly once after
    all tests have finished and the browsers are closed.
    """
    print("-------TESTS COMPLETE! GENERATING AND OPENING ALLURE REPORT--------")
    print("-------------------------------------------------------\n")

    # Automatically triggers the terminal command to open the report
    os.system("allure serve reports/allure-results")
