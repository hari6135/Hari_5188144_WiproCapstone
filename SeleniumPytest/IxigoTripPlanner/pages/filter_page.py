import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import LogGen

logger = LogGen.loggen()


class FilterPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # HELPER METHOD: Smooth scroll with animation buffer
    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )
        # CRITICAL: 0.8s buffer allows the CSS smooth scroll animation to finish before the JS click fires
        time.sleep(0.8)

        # CLICK CATEGORY

    def click_category(self, category_name):
        logger.info(f"Selecting category : {category_name}")

        category_xpath = f"//span[contains(text(),'{category_name}')]"
        category = self.wait.until(EC.element_to_be_clickable((By.XPATH, category_xpath)))

        self.scroll_to_element(category)
        self.driver.execute_script("arguments[0].click();", category)

        logger.info(f"{category_name} selected")

    # CLICK FILTER TYPE
    def click_filter_type(self, filter_name):
        logger.info(f"Selecting filter : {filter_name}")

        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ARROW_DOWN)

        filter_xpath = f"//span[contains(text(),'{filter_name}')]"
        filter_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, filter_xpath)))

        self.scroll_to_element(filter_element)
        self.driver.execute_script("arguments[0].click();", filter_element)

        logger.info(f"{filter_name} selected")

        # WAIT FOR COUNTRY CARDS TO LOAD
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Malaysia')]")))
        logger.info("Country cards loaded")

    # CLICK COUNTRY
    def click_country(self, country_name):
        logger.info(f"Selecting country : {country_name}")

        country_xpath = f"//div[contains(text(),'{country_name}')]"
        country = self.wait.until(EC.element_to_be_clickable((By.XPATH, country_xpath)))

        self.scroll_to_element(country)
        self.driver.execute_script("arguments[0].click();", country)
        logger.info(f"{country_name} selected")

        # PAGE TRANSITION BUFFER: Wait a moment for the new page DOM to start rendering
        # before the script hands off to LocationPage.
        time.sleep(1.5)