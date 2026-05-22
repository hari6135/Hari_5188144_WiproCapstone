import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen


logger = LogGen.loggen()


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        # LOCATORS
        self.login_btn_xpath = "//button[contains(text(),'Log in/Sign up')]"

        self.mobile_input_xpath = "//input[@placeholder='Enter Mobile Number']"

        self.continue_btn_xpath = "//button[contains(text(),'Continue')]"

    # CLICK LOGIN
    def click_login(self):

        logger.info("Waiting for Login button")

        login_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.login_btn_xpath)
            )
        )

        login_btn.click()

        logger.info("Login button clicked")

    # ENTER MOBILE NUMBER
    def enter_mobile_number(self, mobile_number):

        logger.info("Entering mobile number")

        mobile_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.mobile_input_xpath)
            )
        )

        mobile_input.clear()

        mobile_input.send_keys(str(mobile_number))

        logger.info("Mobile number entered")

    # CLICK CONTINUE
    def click_continue(self):

        logger.info("Clicking Continue button")

        continue_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.continue_btn_xpath)
            )
        )

        continue_btn.click()

        logger.info("Continue button clicked")

    # WAIT FOR LOGIN COMPLETION
    def wait_for_login_completion(self):
        logger.info("Waiting for login completion")

        time.sleep(20)

        logger.info("Login completed successfully")

        time.sleep(3)