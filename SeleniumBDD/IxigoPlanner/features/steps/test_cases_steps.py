from behave import given, when, then
from behave.runner import Context

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


# =========================================================
# TEST DATA
# =========================================================

travel_month = planner_data[0]["Month"]

from_location = planner_data[0]["From"]

filter_type = filter_data[0]["FilterType"]

country_name = filter_data[0]["Country"]

invalid_location = filter_data[1]["Country"]

location_category = location_data[0]["Category"]

location_name = location_data[0]["Place"]


# =========================================================
# GIVEN
# =========================================================

@given("user launches the ixigo planner page")
def step_impl(context: Context):

    logger.info(
        "Ixigo Planner Page Launched Successfully"
    )


# =========================================================
# POSITIVE TEST CASE 1
# PLAN PAGE NAVIGATION
# =========================================================

@when("user clicks on plan page for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Plan Page Navigation"
    )

    context.planner_page.click_plan()

    ScreenshotUtil.capture_screenshot(
        driver,
        "plan_page"
    )


@then("planner page should open successfully for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    assert "plan" in \
           driver.current_url.lower()

    logger.info(
        "Plan Page Verified Successfully"
    )


# =========================================================
# POSITIVE TEST CASE 2
# TRAVEL MONTH
# =========================================================

@when("user selects travel month for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Travel Month Selection"
    )

    context.planner_page.click_plan()

    context.planner_page.select_travel_month(
        travel_month
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "travel_month"
    )


@then("selected travel month should be displayed for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    assert travel_month.lower() in \
           driver.page_source.lower()

    logger.info(
        "Travel Month Verified Successfully"
    )


# =========================================================
# COMMON PLANNER FLOW
# =========================================================

@when("user completes planner flow for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Planner Flow"
    )

    context.planner_page.click_plan()

    context.planner_page.select_travel_month(
        travel_month
    )

    context.planner_page.click_from_location()

    context.planner_page.enter_from_location(
        from_location
    )

    context.planner_page.click_from_list(
        from_location
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "planner_page"
    )

    logger.info(
        "Planner Flow Completed Successfully"
    )


# =========================================================
# FILTER FLOW
# =========================================================

@when("user selects category filter for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Filter Flow"
    )

    context.filter_page.click_category(
        "International"
    )

    context.filter_page.click_filter_type(
        filter_type
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "filter_page"
    )

    logger.info(
        "Filter Applied Successfully"
    )


@then("filter should be applied successfully for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    assert filter_type.lower() in \
           driver.page_source.lower()

    logger.info(
        "Filter Verification Successful"
    )


# =========================================================
# COUNTRY FLOW
# =========================================================

@when("user selects destination country for test cases")
def step_impl(context: Context):

    context.filter_page.click_country(
        country_name
    )

    logger.info(
        "Destination Country Selected Successfully"
    )


# =========================================================
# LOCATION FLOW
# =========================================================

@when("user selects tourist location card for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Tourist Location Selection"
    )

    context.location_page.scroll_places_to_visit()

    context.location_page.click_category_chip(
        location_category
    )

    context.location_page.click_location_card(
        location_name
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "location_page"
    )

    logger.info(
        "Tourist Location Selected Successfully"
    )


@then("tourist location card should open successfully for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    assert location_name.lower() in \
           driver.page_source.lower()

    logger.info(
        "Tourist Location Verified Successfully"
    )


# =========================================================
# NEGATIVE TEST CASE 1
# INVALID LOCATION SEARCH
# =========================================================

@when("user enters invalid location for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Invalid Location Test"
    )

    context.planner_page.click_plan()

    context.planner_page.click_from_location()

    context.planner_page.enter_from_location(
        "abcd"
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "invalid_location"
    )

    logger.info(
        "Invalid Location Entered"
    )


@then("invalid location error message should appear for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    error_message = WebDriverWait(
        driver,
        10
    ).until(

        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//span[contains(text(),\"Oops! We couldn't find any results\")]"
            )
        )
    )

    assert error_message.is_displayed()

    logger.info(
        "Invalid Location Error Verified"
    )


# =========================================================
# NEGATIVE TEST CASE 2
# BOOK NOW BUTTON VALIDATION
# =========================================================

@when("user selects invalid from location for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Invalid Route Validation"
    )

    driver.execute_script(
        """
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
        """
    )

    from_dropdown = WebDriverWait(
        driver,
        20
    ).until(

        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[@class='text-ellipsis whitespace-nowrap overflow-hidden']"
            )
        )
    )

    from_dropdown.click()

    search_input = WebDriverWait(
        driver,
        20
    ).until(

        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[@placeholder='Search']"
            )
        )
    )

    search_input.send_keys(
        invalid_location
    )

    location_xpath = \
        f"//a[contains(.,'{invalid_location}')]"

    location = WebDriverWait(
        driver,
        20
    ).until(

        EC.element_to_be_clickable(
            (
                By.XPATH,
                location_xpath
            )
        )
    )

    location.click()

    ScreenshotUtil.capture_screenshot(
        driver,
        "invalid_route"
    )

    logger.info(
        "Invalid Route Selected"
    )


@then("book now button should not be displayed for test cases")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    WebDriverWait(
        driver,
        15
    ).until(

        lambda x: len(
            x.find_elements(
                By.XPATH,
                "//button[contains(.,'Book now')]"
            )
        ) == 0
    )

    book_now_buttons = \
        driver.find_elements(
            By.XPATH,
            "//button[contains(.,'Book now')]"
        )

    assert len(book_now_buttons) == 0

    logger.info(
        "Book Now Button Absence Verified"
    )