import allure

from utils.logger import LogGen
from utils.config_reader import ConfigReader
from utils.screenshot_util import ScreenshotUtil

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import \
    WebDriverWait

from selenium.webdriver.support import \
    expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import \
    ChromeDriverManager


# =========================================================
# PAGE IMPORTS
# =========================================================

from pages.login_page import LoginPage
from pages.planner_page import PlannerPage
from pages.filter_page import FilterPage
from pages.location_page import LocationPage
from pages.map_page import GoogleMapPage
from pages.flight_page import FlightPage


logger = LogGen.loggen()


# =========================================================
# BEFORE SCENARIO
# =========================================================

def before_scenario(
        context,
        scenario
):

    logger.info(
        "========================================"
    )

    logger.info(
        f"STARTING SCENARIO : {scenario.name}"
    )

    # =====================================================
    # READ CONFIGURATION
    # =====================================================

    base_url = ConfigReader.get_base_url()

    implicit_wait = \
        ConfigReader.get_implicit_wait()

    headless = \
        ConfigReader.get_headless()

    # =====================================================
    # CHROME SETUP
    # =====================================================

    logger.info(
        "Launching Chrome Browser"
    )

    chrome_options = Options()

    chrome_options.add_argument(
        "--start-maximized"
    )

    chrome_options.add_argument(
        "--disable-notifications"
    )

    chrome_options.add_argument(
        "--disable-infobars"
    )

    chrome_options.add_argument(
        "--disable-extensions"
    )

    if headless:

        chrome_options.add_argument(
            "--headless"
        )

    context.driver = webdriver.Chrome(

        service=Service(
            ChromeDriverManager().install()
        ),

        options=chrome_options
    )

    # =====================================================
    # BROWSER SETUP
    # =====================================================

    context.driver.implicitly_wait(
        implicit_wait
    )

    context.driver.get(
        base_url
    )

    # =====================================================
    # WAIT FOR PAGE LOAD
    # =====================================================

    WebDriverWait(
        context.driver,
        implicit_wait
    ).until(

        lambda d:
        d.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    logger.info(
        "Page loaded successfully"
    )

    # =====================================================
    # HANDLE POPUP
    # =====================================================

    try:

        logger.info(
            "Checking for popup"
        )

        WebDriverWait(
            context.driver,
            10
        ).until(

            EC.frame_to_be_available_and_switch_to_it(
                (
                    By.ID,
                    "wiz-iframe-intent"
                )
            )
        )

        popup_close = WebDriverWait(
            context.driver,
            10
        ).until(

            EC.element_to_be_clickable(
                (
                    By.ID,
                    "closeButton"
                )
            )
        )

        popup_close.click()

        context.driver.switch_to.default_content()

        logger.info(
            "Popup closed successfully"
        )

    except Exception as e:

        logger.info(
            f"No popup displayed : {e}"
        )

    logger.info(
        "Browser Opened Successfully"
    )

    # =====================================================
    # PAGE OBJECT INITIALIZATION
    # =====================================================

    context.login_page = LoginPage(
        context.driver
    )

    context.planner_page = PlannerPage(
        context.driver
    )

    context.filter_page = FilterPage(
        context.driver
    )

    context.location_page = LocationPage(
        context.driver
    )

    context.google_map = GoogleMapPage(
        context.driver
    )

    context.flight_page = FlightPage(
        context.driver
    )

    logger.info(
        "All Page Objects Initialized Successfully"
    )


# =========================================================
# AFTER SCENARIO
# =========================================================

def after_scenario(
        context,
        scenario
):

    logger.info(
        f"Scenario Status : {scenario.status}"
    )

    # =====================================================
    # FAILURE SCREENSHOT
    # =====================================================

    if scenario.status == "failed":

        logger.error(
            f"SCENARIO FAILED : {scenario.name}"
        )

        if hasattr(context, "driver"):

            screenshot_path = \
                ScreenshotUtil.capture_screenshot(
                    context.driver,
                    scenario.name
                )

            logger.info(
                f"Screenshot Saved : "
                f"{screenshot_path}"
            )

    else:

        logger.info(
            f"SCENARIO PASSED : {scenario.name}"
        )

    # =====================================================
    # ATTACH LOG FILE TO ALLURE
    # =====================================================

    try:

        # FLUSH LOG HANDLERS

        for handler in logger.handlers:

            handler.flush()

        with open(
                "logs/automation.log",
                "r",
                encoding="utf-8"
        ) as log_file:

            log_content = log_file.read()

            allure.attach(

                log_content,

                name="Execution Logs",

                attachment_type=
                allure.attachment_type.TEXT
            )

        logger.info(
            "Logs attached to Allure report"
        )

    except Exception as e:

        logger.error(
            f"Unable to attach logs : {e}"
        )

    # =====================================================
    # CLOSE BROWSER
    # =====================================================

    if hasattr(context, "driver"):

        context.driver.quit()

        logger.info(
            "Browser Closed Successfully"
        )

    logger.info(
        "========================================"
    )