import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen


logger = LogGen.loggen()


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):

        logger.info("Waiting for Login button")

        # wait for login button
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,

                 "//button[contains(text(),'Log in/Sign up')]")
            )
        )

        logger.info("Login button found")

        # assertion
        assert login_btn.is_displayed(), "Login button is not displayed"

        logger.info("Clicking Login button")

        # click login
        login_btn.click()

        logger.info("Login button clicked successfully")

        # wait for manual login
        time.sleep(30)

        logger.info("Manual login wait completed")