import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen


logger = LogGen.loggen()


class FlightPage:

    def __init__(self, driver):
        self.driver = driver

    # switch to flight result tab
    def switch_to_flight_tab(self):

        logger.info("Switching to flight results tab")

        all_windows = self.driver.window_handles

        self.driver.switch_to.window(all_windows[-1])

        time.sleep(2)

    # click first Flight Details
    def click_first_flight_details(self):
        logger.info("Scrolling down")

        self.driver.execute_script("window.scrollBy(0,300)")

        time.sleep(2)

        logger.info("Waiting for Flight Details button")

        flight_details = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//p[contains(text(),'Flight Details')])[1]"
                )
            )
        )

        self.driver.find_element(By.TAG_NAME, "body")

        self.driver.execute_script(
            "window.scrollBy(0, 5)"
        )

        time.sleep(1)

        flight_details.click()

        logger.info("First Flight Details clicked")

        time.sleep(3)