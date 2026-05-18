import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import LogGen

logger = LogGen.loggen()


class LocationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

        # STATIC LOCATORS
        self.close_popup_xpath = "//button[@data-clickable='true']"
        self.book_now_xpath = "//div[contains(@class,'flex items-end')]//button[contains(.,'Book now')]"

    # HELPER METHOD: Smooth scroll with animation buffer
    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )
        time.sleep(0.8)

    # SCROLL TO PLACES TO VISIT
    def scroll_places_to_visit(self):
        logger.info("Scrolling down to Places To Visit section")

        chip_container = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-slot='chip']")))
        self.scroll_to_element(chip_container)

        logger.info("Scrolled down smoothly")

    # CLICK CATEGORY CHIP
    def click_category_chip(self, category_name):
        logger.info(f"Selecting category : {category_name}")

        category_xpath = f"//div[@data-slot='chip'][span[text()='{category_name}']]"
        category = self.wait.until(EC.element_to_be_clickable((By.XPATH, category_xpath)))

        self.scroll_to_element(category)
        self.driver.execute_script("arguments[0].click();", category)

        # Add a tiny buffer so the location cards have a moment to visually shuffle
        time.sleep(0.5)
        logger.info(f"{category_name} selected")

    # CLICK LOCATION CARD
    def click_location_card(self, location_name):
        logger.info(f"Waiting for location card : {location_name}")

        card_xpath = f"//div[contains(@class,'page_carouselItem')]//h3[contains(text(),'{location_name}')]"
        card = self.wait.until(EC.element_to_be_clickable((By.XPATH, card_xpath)))

        self.scroll_to_element(card)
        self.driver.execute_script("arguments[0].click();", card)
        logger.info(f"{location_name} selected")

        # WAIT FOR POPUP TO BE VISIBLE
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.close_popup_xpath)))

    # CLOSE POPUP
    def close_popup(self):
        logger.info("Closing popup")

        close_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.close_popup_xpath)))

        # Adding a slight delay just so it doesn't instantly close before human eyes can register it opened
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", close_btn)

        self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.close_popup_xpath)))
        logger.info("Popup closed successfully")

    # SCROLL TO HOW TO TRAVEL
    def scroll_how_to_travel(self):
        logger.info("Triggering page scroll to load bottom sections...")

        self.driver.execute_script("window.scrollBy(0, 1200);")

        time.sleep(1.5)

        logger.info("Locating the Book Now button...")

        book_now_btn = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.book_now_xpath))
        )

        self.scroll_to_element(book_now_btn)

        logger.info("Scrolled smoothly to Book Now section")
    # CLICK BOOK NOW
    def click_book_now(self):
        logger.info("Waiting for Book Now button")

        book_now = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.book_now_xpath)))

        # Let the user see the button before it gets clicked
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", book_now)

        logger.info("Book Now clicked")