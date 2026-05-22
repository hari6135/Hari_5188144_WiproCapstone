import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import LogGen

logger = LogGen.loggen()


class FilterPage:

    # DYNAMIC LOCATOR
    CATEGORY_XPATH = "//span[contains(text(),'{name}')]"
    FILTER_XPATH = "//span[contains(text(),'{name}')]"
    COUNTRY_XPATH = "//div[contains(text(),'{name}')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # Smooth scroll
    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )
        # CSS smooth scroll animation
        time.sleep(0.8)

    # CLICK CATEGORY
    def click_category(self, category_name):
        logger.info(f"Selecting category : {category_name}")

        xpath = self.CATEGORY_XPATH.format(name=category_name)
        category = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        self.scroll_to_element(category)
        self.driver.execute_script("arguments[0].click();", category)

        logger.info(f"{category_name} selected")

    # CLICK FILTER TYPE
    def click_filter_type(self, filter_name):
        logger.info(f"Selecting filter : {filter_name}")

        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ARROW_DOWN)

        xpath = self.FILTER_XPATH.format(name=filter_name)
        filter_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        self.scroll_to_element(filter_element)
        self.driver.execute_script("arguments[0].click();", filter_element)

        logger.info(f"{filter_name} selected")

        # NOTE: Removed the hardcoded wait for "Malaysia". 
        # The script will now dynamically wait for the target country in `click_country()`.

    # CLICK COUNTRY
    def click_country(self, country_name):
        logger.info(f"Selecting country : {country_name}")

        xpath = self.COUNTRY_XPATH.format(name=country_name)

        # Dynamically waits for the specific country card to appear in the DOM first
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        country = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        self.scroll_to_element(country)
        self.driver.execute_script("arguments[0].click();", country)
        logger.info(f"{country_name} selected")

        # PAGE TRANSITION: Dynamically wait for the current element to become stale 
        # (meaning the DOM has refreshed/navigated away) instead of a hardcoded 1.5s sleep.
        try:
            self.wait.until(EC.staleness_of(country))
            logger.info("Page transition to Location Page started")
        except Exception:
            time.sleep(1.5)
