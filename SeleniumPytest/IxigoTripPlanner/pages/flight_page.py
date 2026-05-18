import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import LogGen

logger = LogGen.loggen()


class FlightPage:

    def __init__(self, driver):
        self.driver = driver
        # dynamic wait
        self.wait = WebDriverWait(self.driver, 20)

        # Locators
        self.first_flight_details_xpath = "(//p[contains(text(),'Flight Details')])[1]"

    # Scroll down function
    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )
        time.sleep(0.8)

    # SWITCH TO FLIGHT RESULT TAB
    def switch_to_flight_tab(self):
        logger.info("Switching to flight results tab")

        # Get all window handles and switch to the newest one
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

        # WAIT: Instead of time.sleep(2), wait for the browser to signal
        # that the new page's DOM has finished loading completely.
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        logger.info("Switched to flight tab and page is fully loaded")

    # CLICK FIRST FLIGHT DETAILS
    def click_first_flight_details(self):
        logger.info("Waiting for first Flight Details button")

        # Wait dynamically for the button to exist and be clickable
        flight_details = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.first_flight_details_xpath))
        )

        self.scroll_to_element(flight_details)

        #  Use JS Click to avoid overlapping
        self.driver.execute_script("arguments[0].click();", flight_details)

        logger.info("First Flight Details clicked successfully")
        time.sleep(1.5)