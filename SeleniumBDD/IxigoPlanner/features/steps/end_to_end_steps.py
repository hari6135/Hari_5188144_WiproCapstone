
import time
from behave import given, when, then
from behave.runner import Context

from selenium.webdriver.remote.webdriver import WebDriver

from utils.excel_reader import ExcelReader
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil


logger = LogGen.loggen()


# =========================================================
# EXCEL DATA
# =========================================================

login_data = ExcelReader.read_excel(
    "testdata.xlsx",
    "LoginData"
)

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

mobile_number = login_data[0]["mobile"]

travel_month = planner_data[0]["Month"]

from_location = planner_data[0]["From"]

category_name = filter_data[0]["Category"]

filter_type = filter_data[0]["FilterType"]

country_name = filter_data[0]["Country"]

location_category = location_data[0]["Category"]

location_name = location_data[0]["Place"]


# =========================================================
# GIVEN
# =========================================================

@given("user launches ixigo application")
def step_impl(context: Context):

    logger.info(
        "Ixigo Application Launched Successfully"
    )


# =========================================================
# LOGIN FLOW
# =========================================================

@when("user performs login flow for end to end")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Login Flow"
    )

    context.login_page.click_login()

    logger.info(
        "Login popup opened successfully"
    )

    context.login_page.enter_mobile_number(
        mobile_number
    )

    logger.info(
        "Mobile number entered successfully"
    )

    context.login_page.click_continue()

    logger.info(
        "Continue button clicked successfully"
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "login_page"
    )

    # MANUAL OTP
    context.login_page.wait_for_login_completion()

    logger.info(
        "Login flow completed successfully"
    )


@then("user should login successfully")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    assert "ixigo" in \
           driver.title.lower(), \
        "Login failed after OTP verification"

    logger.info(
        "Login verified successfully"
    )


# =========================================================
# PLANNER FLOW
# =========================================================

@when("user completes planner flow for end to end")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Planner Flow"
    )

    context.planner_page.click_plan()

    logger.info(
        "Plan page clicked successfully"
    )

    context.planner_page.select_travel_month(
        travel_month
    )

    logger.info(
        "Travel month selected successfully"
    )

    context.planner_page.click_from_location()

    context.planner_page.enter_from_location(
        from_location
    )

    logger.info(
        "From location entered successfully"
    )

    context.planner_page.click_from_list(
        from_location
    )

    logger.info(
        "From location selected successfully"
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "planner_page"
    )

    logger.info(
        "Planner Flow Completed Successfully"
    )


@then("planner details should be displayed successfully")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    assert "plan" in \
           driver.current_url.lower(), \
        "Plan page not opened"

    assert travel_month.lower() in \
           driver.page_source.lower(), \
        "Travel month not selected"

    assert from_location.lower() in \
           driver.page_source.lower(), \
        "From location not selected"

    logger.info(
        "Planner details verified successfully"
    )


# =========================================================
# FILTER FLOW
# =========================================================

@when("user applies travel filters for end to end")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Filter Flow"
    )

    context.filter_page.click_category(
        category_name
    )

    logger.info(
        "Category selected successfully"
    )

    context.filter_page.click_filter_type(
        filter_type
    )

    logger.info(
        "Filter type selected successfully"
    )

    context.filter_page.click_country(
        country_name
    )

    logger.info(
        "Country selected successfully"
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "filter_page"
    )

    logger.info(
        "Filter Flow Completed Successfully"
    )


@then("travel filters should be applied successfully")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    assert filter_type.lower() in \
           driver.page_source.lower(), \
        "Filter type not applied"

    assert country_name.lower() in \
           driver.page_source.lower(), \
        "Country filter not applied"

    logger.info(
        "Travel filters verified successfully"
    )


# =========================================================
# LOCATION FLOW
# =========================================================

@when("user selects tourist location for end to end")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Tourist Location Flow"
    )

    context.location_page.scroll_places_to_visit()

    logger.info(
        "Places To Visit section reached successfully"
    )

    context.location_page.click_category_chip(
        location_category
    )

    logger.info(
        "Location category selected successfully"
    )

    context.location_page.click_location_card(
        location_name
    )

    logger.info(
        "Tourist location selected successfully"
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "location_page"
    )

    logger.info(
        "Tourist Location Selected Successfully"
    )


@then("tourist location should open successfully for end to end")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    assert "places to visit" in \
           driver.page_source.lower(), \
        "Places To Visit section not visible"

    assert location_name.lower() in \
           driver.page_source.lower(), \
        "Tourist location details page did not open"

    logger.info(
        "Tourist location verified successfully"
    )


# =========================================================
# GOOGLE MAP FLOW
# =========================================================

@then("user verifies google map page")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Google Map Verification"
    )

    context.google_map.verify_google_map_page()

    assert "map" in \
           driver.page_source.lower(), \
        "Google map section not loaded"

    ScreenshotUtil.capture_screenshot(
        driver,
        "google_map_page"
    )

    logger.info(
        "Google map verified successfully"
    )


# =========================================================
# BOOK NOW FLOW
# =========================================================

@then("book now button should be visible")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    assert "book now" in \
           driver.page_source.lower(), \
        "Book Now button not visible"

    logger.info(
        "Book Now button verified successfully"
    )


@then("user clicks book now")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Book Now Flow"
    )

    context.location_page.close_popup()

    context.location_page.scroll_how_to_travel()

    context.location_page.click_book_now()

    ScreenshotUtil.capture_screenshot(
        driver,
        "book_now_page"
    )

    logger.info(
        "Book Now Clicked Successfully"
    )


# =========================================================
# FLIGHT FLOW
# =========================================================

@then("flight details page should open successfully")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info(
        "Starting Flight Details Verification"
    )

    context.flight_page.switch_to_flight_tab()

    assert len(driver.window_handles) > 1, \
        "Flight tab did not open"

    logger.info(
        "Flight tab opened successfully"
    )

    context.flight_page.click_first_flight_details()

    assert "flight" in \
           driver.page_source.lower(), \
        "Flight details page not loaded"

    time.sleep(1)
    
    ScreenshotUtil.capture_screenshot(
        driver,
        "flight_page"
    )

    logger.info(
        "Flight details verified successfully"
    )

    logger.info(
        "========== END TO END FLOW COMPLETED =========="
    )