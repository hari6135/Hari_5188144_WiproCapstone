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

    # click international filter
    def click_international(self):

        logger.info("Waiting for International filter")

        international = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[contains(text(),'International')]"
                )
            )
        )

        international.click()

        logger.info("International filter selected")

        time.sleep(2)

    # click pollution free filter
    def click_pollution_free(self):

        logger.info("Small scroll down")

        body = self.driver.find_element(By.TAG_NAME, "body")

        body.send_keys(Keys.ARROW_DOWN)

        time.sleep(1)
        logger.info("Waiting for Pollution Free filter")

        pollution_free = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[contains(text(),'Pollution Free')]"
                )
            )
        )

        pollution_free.click()

        logger.info("Pollution Free filter selected")

        time.sleep(2)


    # click Malaysia card
    def click_malaysia(self):

        logger.info("Waiting for Malaysia location")

        malaysia = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(text(),'Malaysia')]"
                )
            )
        )

        malaysia.click()

        logger.info("Malaysia selected")

        time.sleep(2)