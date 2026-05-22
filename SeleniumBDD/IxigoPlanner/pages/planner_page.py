from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen

logger = LogGen.loggen()

class PlannerPage:

    def __init__(self, driver):

        self.driver = driver

        # LOCATORS
        self.plan_btn_xpath = "//a[@data-testid='submenu-item' and contains(@href,'plan')]"

        self.travel_month_xpath = "//span[contains(text(),'Travel month')]"

        self.from_location_xpath = "//span[@class='body-xs' and contains(text(),'From')]"

        self.search_input_xpath = "//input[@placeholder='Search']"

    # CLICK PLAN
    def click_plan(self):

        logger.info("Waiting for Plan button")

        plan_btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, self.plan_btn_xpath)
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            plan_btn
        )

        logger.info("Plan page opened")

    # SELECT TRAVEL MONTH
    def select_travel_month(self, month_name):

        logger.info("Waiting for Travel Month")

        month_btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, self.travel_month_xpath)
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            month_btn
        )

        logger.info("Travel Month clicked")

        month_xpath = f"//span[text()='{month_name}']"

        month = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, month_xpath)
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            month
        )

        logger.info(f"{month_name} selected")

    # CLICK FROM LOCATION
    def click_from_location(self):

        logger.info("Waiting for From location field")

        from_place = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.from_location_xpath)
            )
        )

        from_place.click()

        logger.info("From location field clicked")

    # ENTER FROM LOCATION
    def enter_from_location(self, from_location):

        logger.info(f"Entering from location : {from_location}")

        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.search_input_xpath)
            )
        )

        search_input.clear()

        search_input.send_keys(from_location)

        logger.info("From location entered")

    # CLICK LOCATION FROM LIST
    def click_from_list(self, from_location):

        logger.info(f"Selecting location : {from_location}")

        location_xpath = f"//a[contains(.,'{from_location}')]"

        location = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, location_xpath)
            )
        )

        location.click()

        logger.info("Location selected successfully")