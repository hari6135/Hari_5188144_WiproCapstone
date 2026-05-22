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

    # ---------------------- Assert -----------------------------------------
    assert "login" in context.driver.page_source.lower(), \
        "Login popup did not open"

    context.login_page.enter_mobile_number(
        mobile_number
    )

    context.login_page.click_continue()

    ScreenshotUtil.capture_screenshot(
        driver,
        "login_page"
    )

    # MANUAL OTP
    context.login_page.wait_for_login_completion()

    assert "ixigo" in \
           driver.title.lower(), \
        "Login failed after OTP verification"

    logger.info("Login Flow Completed Successfully")


# =========================================================
# PLANNER FLOW
# =========================================================

@when("user completes planner flow for end to end")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info( "Starting Planner Flow" )

    context.planner_page.click_plan()

    # ------------ PLAN PAGE ASSERT ---------------------------------
    assert "plan" in \
           driver.current_url.lower(), \
        "Plan page not opened"
    context.planner_page.select_travel_month(
        travel_month
    )

    #  ------------- TRAVEL MONTH ASSERT ------------------------------
    assert travel_month.lower() in \
           driver.page_source.lower(), \
        "Travel month not selected"


    context.planner_page.click_from_location()

    context.planner_page.enter_from_location(
        from_location
    )

    context.planner_page.click_from_list(
        from_location
    )
    #  ------------- FROM LOCATION ASSERT ------------------------------
    assert from_location.lower() in \
           driver.page_source.lower(), \
        "From location not selected"

    ScreenshotUtil.capture_screenshot(
        driver,
        "planner_page"
    )

    logger.info("Planner Flow Completed Successfully")


# =========================================================
# FILTER FLOW
# =========================================================

@when("user applies travel filters for end to end")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info("Starting Filter Flow")

    context.filter_page.click_category(
        category_name
    )

    context.filter_page.click_filter_type(
        filter_type
    )
    # -------------------- FILTER TYPE ASSERT ----------------------
    assert filter_type.lower() in \
           driver.page_source.lower(), \
        "Filter type not applied"


    context.filter_page.click_country(
        country_name
    )

    # ---------------- COUNTRY FILTER ASSERT ---------------------
    assert country_name.lower() in \
           driver.page_source.lower(), \
        "Country filter not applied"

    ScreenshotUtil.capture_screenshot(
        driver,
        "filter_page"
    )

    logger.info("Filter Flow Completed Successfully")


# ================================= LOCATION FLOW =======================

@when("user selects tourist location for end to end")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info("Starting Tourist Location Flow")

    context.location_page.scroll_places_to_visit()

    # ------------ PLACES SECTION ASSERT ----------------
    assert "places to visit" in \
           driver.page_source.lower(), \
        "Places To Visit section not visible"

    context.location_page.click_category_chip(
        location_category
    )

    # ------------ TOURIST LOCATION SECTION ASSERT ----------------
    assert location_name.lower() in \
           driver.page_source.lower(), \
        "Tourist location page not opened"

    context.location_page.click_location_card(
        location_name
    )

    ScreenshotUtil.capture_screenshot(
        driver,
        "location_page"
    )

    logger.info("Tourist Location Selected Successfully")


@then("tourist location should open successfully for end to end")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    assert location_name.lower() in \
           driver.page_source.lower()

    logger.info("Tourist Location Verified Successfully")


# =========================================================
# GOOGLE MAP FLOW
# =========================================================

@then("user verifies google map page")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info("Starting Google Map Verification")

    context.google_map.verify_google_map_page()

    # ------------ GOOGLE MAP ASSERT ----------------------------
    # assert "Google Maps" in \
    #        driver.current_url.lower(), \
    #     "Google Map page not opened"

    ScreenshotUtil.capture_screenshot(
        driver,
        "google_map_page"
    )

    logger.info("Google Map Verified Successfully")


# =========================================================
# BOOK NOW FLOW
# =========================================================

@then("user clicks book now")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info("Starting Book Now Flow")

    context.location_page.close_popup()

    context.location_page.scroll_how_to_travel()


    # ---------------------- BOOK NOW -------------------------------
    assert "book now" in \
           driver.page_source.lower(), \
        "Book Now button not visible"


    context.location_page.click_book_now()

    ScreenshotUtil.capture_screenshot(
        driver,
        "book_now_page"
    )

    logger.info("Book Now Clicked Successfully")


# =========================================================
# FLIGHT FLOW
# =========================================================

@then("flight details page should open successfully")
def step_impl(context: Context):

    driver: WebDriver = context.driver

    logger.info("Starting Flight Details Verification")

    context.flight_page.switch_to_flight_tab()

    # -------------- FLIGHT TAB ASSERT ------------------------------
    assert len(driver.window_handles) > 1, \
        "Flight tab did not open"

    context.flight_page.click_first_flight_details()
    # ------------------ FLIGHT PAGE ASSERT ------------------------
    assert "flight" in \
           driver.page_source.lower(), \
        "Flight details page not loaded"

    logger.info("Flight Details Verified Successfully")

    ScreenshotUtil.capture_screenshot(
        driver,
        "flight_page"
    )

    logger.info("Flight Details Verified Successfully")

    logger.info("========== END TO END FLOW COMPLETED ==========")