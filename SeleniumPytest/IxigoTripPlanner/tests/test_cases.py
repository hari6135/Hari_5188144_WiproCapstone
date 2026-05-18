import pytest
import allure

from pages.filter_page import FilterPage
from pages.location_page import LocationPage
from pages.planner_page import PlannerPage
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from utils.excel_reader import ExcelReader
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil

logger = LogGen.loggen()

# EXCEL DATA

planner_data = ExcelReader.read_excel(
    "testdata.xlsx",
    "PlannerData"
)

filter_data = ExcelReader.read_excel(
    "testdata.xlsx",
    "FilterData"
)

location_data = ExcelReader.read_excel(
    "testdata.xlsx",
    "LocationData"
)

travel_month = planner_data[0]["Month"]

from_location = planner_data[0]["From"]

category_name = filter_data[0]["Category"]

filter_type = filter_data[0]["FilterType"]

country_name = filter_data[0]["Country"]

location_category = location_data[0]["Category"]

location_name = location_data[0]["Place"]


# COMMON PLANNER FLOW

@allure.step("Execute Common Planner Navigation Flow")
def planner_flow(driver):
    planner_page = PlannerPage(driver)

    planner_page.click_plan()

    planner_page.select_travel_month(travel_month)

    planner_page.click_from_location()

    planner_page.enter_from_location(from_location)

    planner_page.click_from_list(from_location)


# POSITIVE TEST CASE 1

@pytest.mark.smoke
@allure.title("Verify Plan Page Navigation")
@allure.description("Tests if the user can successfully navigate to the trip planner page.")
def test_plan_page_navigation(driver):
    logger.info("========== TEST : PLAN PAGE NAVIGATION ==========")

    planner_page = PlannerPage(driver)

    planner_page.click_plan()

    ScreenshotUtil.capture_screenshot(
        driver,
        "plan_page_navigation"
    )

    assert "plan" in driver.current_url.lower()

    logger.info("PLAN PAGE TEST PASSED")


# POSITIVE TEST CASE 2

@pytest.mark.regression
@allure.title("Verify Travel Month Selection")
@allure.description("Tests if selecting a travel month updates the page accordingly.")
def test_travel_month_selection(driver):
    logger.info("========== TEST : TRAVEL MONTH ==========")

    planner_page = PlannerPage(driver)

    planner_page.click_plan()

    planner_page.select_travel_month(travel_month)

    ScreenshotUtil.capture_screenshot(
        driver,
        "travel_month_selection"
    )

    assert travel_month.lower() in driver.page_source.lower()

    logger.info("TRAVEL MONTH TEST PASSED")


# POSITIVE TEST CASE 3

@pytest.mark.regression
@allure.title("Verify Filter Selection")
@allure.description("Tests if selecting category and filter types works correctly.")
def test_filter_selection(driver):
    logger.info("========== TEST : FILTER SELECTION ==========")

    planner_flow(driver)

    filter_page = FilterPage(driver)

    filter_page.click_category(category_name)

    filter_page.click_filter_type(filter_type)

    ScreenshotUtil.capture_screenshot(
        driver,
        "filter_selection"
    )

    assert filter_type.lower() in driver.page_source.lower()

    logger.info("FILTER TEST PASSED")


# POSITIVE TEST CASE 4

@pytest.mark.regression
@allure.title("Verify Location Card Selection")
@allure.description("Tests if a specific location card can be found and selected.")
def test_location_card_selection(driver):
    logger.info("========== TEST : LOCATION CARD ==========")

    planner_flow(driver)

    filter_page = FilterPage(driver)

    filter_page.click_category(category_name)

    filter_page.click_filter_type(filter_type)

    filter_page.click_country(country_name)

    location_page = LocationPage(driver)

    location_page.scroll_places_to_visit()

    location_page.click_category_chip(location_category)

    location_page.click_location_card(location_name)

    ScreenshotUtil.capture_screenshot(
        driver,
        "location_card_selection"
    )

    assert location_name.lower() in driver.page_source.lower()

    logger.info("LOCATION CARD TEST PASSED")


# NEGATIVE TEST CASE 1
# VERIFY INVALID LOCATION SEARCH

@pytest.mark.negative
@allure.title("Negative: Verify Invalid Location Search")
@allure.description("Tests if an error message appears when searching for an invalid location.")
def test_invalid_location_search(driver):
    logger.info("========== STARTING INVALID LOCATION TEST ==========")

    planner_page = PlannerPage(driver)

    planner_page.click_plan()

    planner_page.click_from_location()

    planner_page.enter_from_location("abcd")

    logger.info("Invalid location entered")

    # WAIT FOR ERROR MESSAGE
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//span[contains(text(),\"Oops! We couldn't find any results\")]"
            )
        )
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "invalid_location_search"
    )

    # ASSERTION
    assert error_message.text == \
           "Oops! We couldn't find any results for that destination."

    logger.info("Error message verified successfully")

    logger.info("========== INVALID LOCATION TEST PASSED ==========")


# NEGATIVE TEST CASE 2
@pytest.mark.negative
@allure.title("Negative: Verify Book Now Button Not Available")
@allure.description("Tests if the Book Now button is successfully hidden when an invalid 'From' location is selected.")
def test_book_now_button_not_available(driver):
    logger.info(
        "========== STARTING BOOK NOW NEGATIVE TEST =========="
    )

    # =====================================================
    # PLANNER DATA
    # =====================================================

    planner_data = ExcelReader.read_excel(
        "testdata.xlsx",
        "PlannerData"
    )

    travel_month = planner_data[0]["Month"]

    from_location = planner_data[0]["From"]

    # =====================================================
    # FILTER DATA
    # =====================================================

    filter_data = ExcelReader.read_excel(
        "testdata.xlsx",
        "FilterData"
    )

    category_name = filter_data[0]["Category"]

    filter_type = filter_data[0]["FilterType"]

    country_name = filter_data[0]["Country"]

    # SECOND ROW -> HIKONE
    invalid_location = filter_data[1]["Country"]

    logger.info(f"Invalid Location : {invalid_location}")

    # PAGE OBJECTS
    planner_page = PlannerPage(driver)
    filter_page = FilterPage(driver)
    location_page = LocationPage(driver)

    # PLANNER FLOW
    planner_page.click_plan()
    planner_page.select_travel_month(travel_month)
    planner_page.click_from_location()
    planner_page.enter_from_location(from_location)
    planner_page.click_from_list(from_location)

    logger.info("Planner flow completed")

    # FILTER FLOW
    filter_page.click_category(category_name)
    filter_page.click_filter_type(filter_type)
    filter_page.click_country(country_name)

    logger.info("Malaysia selected successfully")

    ScreenshotUtil.capture_screenshot(
        driver,
        "malaysia_page"
    )

    # SCROLL TO HOW TO REACH
    logger.info("Smooth scrolling to How To Reach section")

    driver.execute_script(
        """
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
        """
    )

    logger.info("Scrolled to bottom successfully")

    # CLICK FROM DROPDOWN
    from_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[@class='text-ellipsis whitespace-nowrap overflow-hidden']"
            )
        )
    )

    from_dropdown.click()

    logger.info("From dropdown clicked")

    # ENTER INVALID LOCATION
    logger.info(
        f"Entering Invalid Location : {invalid_location}"
    )

    search_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[@placeholder='Search']"
            )
        )
    )

    search_input.clear()

    search_input.send_keys(invalid_location)

    logger.info("Invalid location entered")

    # CLICK LOCATION FROM LIST
    logger.info(
        f"Selecting location : {invalid_location}"
    )

    location_xpath = f"//a[contains(.,'{invalid_location}')]"

    location = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                location_xpath
            )
        )
    )

    location.click()

    logger.info("Location selected successfully")

    # WAIT FOR PAGE REFRESH
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (
                By.XPATH,
                "//span[@class='text-ellipsis whitespace-nowrap overflow-hidden']"
            ),
            invalid_location
        )
    )

    logger.info(
        f"Page refreshed with {invalid_location}"
    )

    # WAIT FOR BOOK NOW BUTTON TO DISAPPEAR
    WebDriverWait(driver, 20).until(
        lambda driver: len(
            driver.find_elements(
                By.XPATH,
                "//button[contains(.,'Book now')]"
            )
        ) == 0
    )

    logger.info("Book Now button removed successfully")

    ScreenshotUtil.capture_screenshot(
        driver,
        "book_now_negative_test"
    )

    logger.info("Checking Book Now button")

    # FIND BOOK NOW BUTTON
    book_now_buttons = driver.find_elements(
        By.XPATH,
        "//button[contains(.,'Book now')]"
    )

    logger.info(
        f"Book Now Buttons Found : {len(book_now_buttons)}"
    )

    # NEGATIVE ASSERTION
    assert len(book_now_buttons) == 0, \
        "FAILED : Book Now button is displayed"

    logger.info(
        "========== BOOK NOW NEGATIVE TEST PASSED =========="
    )
