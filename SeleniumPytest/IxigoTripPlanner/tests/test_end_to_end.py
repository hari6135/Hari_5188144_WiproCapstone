import pytest

from pages.filter_page import FilterPage
from pages.flight_page import FlightPage
from pages.location_page import LocationPage
from pages.login_page import LoginPage
from pages.map_page import GoogleMapPage
from pages.planner_page import PlannerPage

from utils.excel_reader import ExcelReader
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil


logger = LogGen.loggen()


# LOGIN DATA
login_data = ExcelReader.read_excel(
    "testdata.xlsx",
    "LoginData"
)

# PLANNER DATA
planner_data = ExcelReader.read_excel(
    "testdata.xlsx",
    "PlannerData"
)

# FILTER DATA
filter_data = ExcelReader.read_excel(
    "testdata.xlsx",
    "FilterData"
)

# LOCATION DATA
location_data = ExcelReader.read_excel(
    "testdata.xlsx",
    "LocationData"
)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "login, planner, filter_data_row, location",
    zip(
        login_data,
        planner_data,
        filter_data,
        location_data
    )
)
def test_start_page(
        driver,
        login,
        planner,
        filter_data_row,
        location
):

    logger.info(
        "========== STARTING END TO END TRIP PLANNER =========="
    )

    # LOGIN DATA
    mobile_number = login["mobile"]

    # PLANNER DATA
    travel_month = planner["Month"]

    from_location = planner["From"]

    # FILTER DATA
    category_name = filter_data_row["Category"]

    filter_type = filter_data_row["FilterType"]

    country_name = filter_data_row["Country"]

    # LOCATION DATA
    location_category = location["Category"]

    location_name = location["Place"]

    # LOGIN PAGE
    login_page = LoginPage(driver)

    # PLANNER PAGE
    planner_page = PlannerPage(driver)

    # FILTER PAGE
    filter_page = FilterPage(driver)

    # LOCATION PAGE
    location_page = LocationPage(driver)

    # GOOGLE MAP PAGE
    google_map = GoogleMapPage(driver)

    # FLIGHT PAGE
    flight_page = FlightPage(driver)

    # LOGIN FLOW
    login_page.click_login()

    login_page.enter_mobile_number(mobile_number)

    login_page.click_continue()

    ScreenshotUtil.capture_screenshot(
        driver,
        "login_page"
    )

    # MANUAL OTP
    login_page.wait_for_login_completion()

    # ASSERTION
    assert "ixigo" in driver.title.lower()

    # PLANNER FLOW
    planner_page.click_plan()

    planner_page.select_travel_month(travel_month)

    planner_page.click_from_location()

    planner_page.enter_from_location(from_location)

    planner_page.click_from_list(from_location)

    ScreenshotUtil.capture_screenshot(
        driver,
        "planner_page"
    )

    # FILTER FLOW
    filter_page.click_category(category_name)

    filter_page.click_filter_type(filter_type)

    filter_page.click_country(country_name)

    ScreenshotUtil.capture_screenshot(
        driver,
        "filter_page"
    )

    # LOCATION FLOW
    location_page.scroll_places_to_visit()

    location_page.click_category_chip(location_category)

    location_page.click_location_card(location_name)

    ScreenshotUtil.capture_screenshot(
        driver,
        "location_page"
    )

    # ASSERTION
    assert location_name.lower() in driver.page_source.lower()

    # GOOGLE MAP
    google_map.verify_google_map_page()

    ScreenshotUtil.capture_screenshot(
        driver,
        "google_map_page"
    )

    # BOOK NOW FLOW
    location_page.close_popup()

    location_page.scroll_how_to_travel()

    location_page.click_book_now()

    ScreenshotUtil.capture_screenshot(
        driver,
        "book_now_page"
    )

    # FLIGHT FLOW
    flight_page.switch_to_flight_tab()

    flight_page.click_first_flight_details()

    ScreenshotUtil.capture_screenshot(
        driver,
        "flight_page"
    )

    logger.info(
        "========== END TO END TRIP PLANNER COMPLETED SUCCESSFULLY =========="
    )