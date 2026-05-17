import pytest
import time

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

    print(f"Browser from config: {browser}")

    # CHROME
    if browser == "chrome":

        chrome_options = ChromeOptions()

        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        driver = webdriver.Chrome()
        driver.maximize_window()

    # EDGE
    else:

        edge_options = EdgeOptions()

        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-infobars")
        edge_options.add_argument("--disable-extensions")

        driver = webdriver.Edge()
        driver.maximize_window()

    logger.info(f"Opened Browser : {browser}")

    driver.get(base_url)

    logger.info(f"Loaded URL : {base_url}")

    # wait for ixigo page to load
    time.sleep(2)

    # close popup
    # wait for ixigo page load
    time.sleep(2)

    try:

        # wait for popup iframe
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "wiz-iframe-intent") ) )

        # wait for close button inside iframe
        popup_close = WebDriverWait(driver, 20).until(  EC.element_to_be_clickable((By.ID, "closeButton") ) )

        # close popup
        popup_close.click()

        # switch back to main page
        driver.switch_to.default_content()

        print("Popup closed")

    except:
        print("Popup not found")


    yield driver

    time.sleep(3)

    driver.quit()

    logger.info("Browser Closed")
    logger.info("==================================================")