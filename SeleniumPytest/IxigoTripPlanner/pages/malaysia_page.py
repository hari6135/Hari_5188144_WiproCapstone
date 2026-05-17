import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen


logger = LogGen.loggen()


class MalaysiaPage:

    def __init__(self, driver):
        self.driver = driver

    # scroll down to Places To Visit section
    def scroll_places_to_visit(self):

        logger.info("Scrolling down to Places To Visit section")

        self.driver.find_element(By.TAG_NAME, "body")

        self.driver.execute_script(
            "window.scrollBy(0, 25)"
        )

        logger.info("Scrolled down")


    # click Islands option
    def click_art(self):

        logger.info("Waiting for Islands option")

        islands = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@data-slot='chip'][4]"
                )
            )
        )

        islands.click()

        logger.info("Islands option selected")

        time.sleep(2)

    # click Perhentian Islands card
    def click_perhentian_islands(self):

        logger.info("Waiting for Perhentian Islands card")

        island_card = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class,'page_carouselItem')]//h3[contains(text(),'Penang Street Art')]"
                )
            )
        )

        island_card.click()

        logger.info("Perhentian Islands selected")

        time.sleep(2)


    # close details popup
    def close_popup(self):

        close_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@data-clickable='true']"
                )
            )
        )
        close_btn.click()

        logger.info("Popup closed")

        time.sleep(2)

    # scroll to How To Travel section
    def scroll_how_to_travel(self):

        logger.info("Scrolling to How To Travel")

        self.driver.execute_script(
            "window.scrollBy(0, 900)"
        )

        time.sleep(2)

    # click Book Now
    def click_book_now(self):
        logger.info("Waiting for Book Now button")

        book_now = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class,'flex items-end')]//button[contains(.,'Book now')]"
                )
            )
        )

        book_now.click()

        logger.info("Book Now clicked")

        time.sleep(2)