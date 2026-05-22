from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.screenshot_util import ScreenshotUtil

from utils.logger import LogGen

logger = LogGen.loggen()


class GoogleMapPage:

    def __init__(self, driver):
        self.driver = driver
        # 1. Centralized dynamic wait (20 seconds max)
        self.wait = WebDriverWait(self.driver, 20)

    # click directions and verify Google Maps
    def verify_google_map_page(self):

        logger.info("Waiting for Directions button")

        # Simplified the XPath slightly to make it less prone to breaking if Google changes their subdomain
        directions_xpath = "//a[contains(@href,'maps.google.com') and contains(text(),'Directions')]"

        directions = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, directions_xpath))
        )

        # store current tab and current number of open tabs
        main_window = self.driver.current_window_handle
        initial_windows = self.driver.window_handles

        logger.info("Clicking Directions button")

        # Scroll element into view before clicking to prevent "Element Not Clickable" errors
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", directions)
        directions.click()

        logger.info("Waiting for Google Maps tab to open...")

        # 2. DYNAMIC WAIT: Wait exactly until a new window/tab is detected by the browser
        self.wait.until(EC.number_of_windows_to_be(len(initial_windows) + 1))

        # switch to the newly opened Google Maps tab
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break

        logger.info("Switched to new tab. Waiting for title to load...")

        # 3. DYNAMIC WAIT: Wait for the title to update. Browsers default to "Untitled" for a split second!
        self.wait.until(EC.title_contains("Google Maps"))

        logger.info(f"Google Maps Title : {self.driver.title}")

        # verify Google Maps opened (100% safe now because of the wait above)
        assert "Google Maps" in self.driver.title
        logger.info("Google Maps page verified")
        ScreenshotUtil.capture_screenshot(self.driver, "google_map_page")

        # close Google Maps tab
        self.driver.close()
        logger.info("Google Maps tab closed")

        # switch back to Ixigo page
        self.driver.switch_to.window(main_window)
        logger.info("Switched back to Ixigo page")