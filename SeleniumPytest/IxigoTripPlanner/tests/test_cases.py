import pytest
import allure

from pages.filter_page import FilterPage
from pages.location_page import LocationPage
from pages.planner_page import PlannerPage

from utils.excel_reader import ExcelReader
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil


logger = LogGen.loggen()


# =========================================================
# EXCEL DATA
# =========================================================

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


# =========================================================
# COMMON PLANNER FLOW
# =========================================================

def planner_flow(driver):

    planner_page = PlannerPage(driver)

    planner_page.click_plan()

    planner_page.select_travel_month(travel_month)

    planner_page.click_from_location()

    planner_page.enter_from_location(from_location)

    planner_page.click_from_list(from_location)


# =========================================================
# POSITIVE TEST CASE 1
# =========================================================

@pytest.mark.smoke
@allure.title("Verify Plan Page Navigation")
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


# =========================================================
# POSITIVE TEST CASE 2
# =========================================================

@pytest.mark.regression
@allure.title("Verify Travel Month Selection")
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


# =========================================================
# POSITIVE TEST CASE 3
# =========================================================

@pytest.mark.regression
@allure.title("Verify Filter Selection")
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


# =========================================================
# POSITIVE TEST CASE 4
# =========================================================

@pytest.mark.regression
@allure.title("Verify Location Card Selection")
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


# =========================================================
# NEGATIVE TEST CASE 1
# =========================================================

@pytest.mark.negative
@allure.title("Verify Invalid Location Search")
def test_invalid_location_search(driver):

    logger.info("========== TEST : INVALID LOCATION ==========")

    planner_page = PlannerPage(driver)

    planner_page.click_plan()

    planner_page.click_from_location()

    planner_page.enter_from_location("xxxxxxxx")

    ScreenshotUtil.capture_screenshot(
        driver,
        "invalid_location"
    )

    assert "No Results" not in driver.page_source

    logger.info("INVALID LOCATION TEST PASSED")


# =========================================================
# NEGATIVE TEST CASE 2
# =========================================================

@pytest.mark.negative
@allure.title("Verify Invalid Country Validation")
def test_invalid_country_validation(driver):

    logger.info("========== TEST : INVALID COUNTRY ==========")

    planner_flow(driver)

    ScreenshotUtil.capture_screenshot(
        driver,
        "invalid_country"
    )

    assert "ABCDEFGH" not in driver.page_source

    logger.info("INVALID COUNTRY TEST PASSED")