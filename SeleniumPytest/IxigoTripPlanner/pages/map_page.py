import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen


logger = LogGen.loggen()


class GoogleMapPage:

    def __init__(self, driver):
        self.driver = driver

    # click directions and verify google maps
    def verify_google_map_page(self):

        logger.info("Waiting for Directions button")

        directions = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(@href,'maps.google.com') and contains(text(),'Directions')]"
                )
            )
        )

        # store ixigo tab
        main_window = self.driver.current_window_handle

        logger.info("Clicking Directions button")

        directions.click()

        time.sleep(3)

        # switch to google maps tab
        all_windows = self.driver.window_handles

        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break

        logger.info(f"Google Maps Title : {self.driver.title}")

        # verify google maps opened
        assert "Google" in self.driver.title

        logger.info("Google Maps page verified")

        time.sleep(2)

        # close google maps tab
        self.driver.close()

        logger.info("Google Maps tab closed")

        # switch back to ixigo page
        self.driver.switch_to.window(main_window)

        logger.info("Switched back to Ixigo page")

        time.sleep(2)