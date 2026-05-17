
from pages.filter_page import FilterPage
from pages.flight_page import FlightPage
from pages.login_page import LoginPage
from pages.malaysia_page import MalaysiaPage
from pages.map_page import GoogleMapPage
from pages.planner_page import PlannerPage

def test_start_page(driver):
    #login
    login = LoginPage(driver)

    #plan
    planner_page = PlannerPage(driver)

    #filter
    filter_page = FilterPage(driver)

    #malaysia_page
    malaysia_page = MalaysiaPage(driver)

    #google maps
    google_map = GoogleMapPage(driver)

    #flight page
    flight_page = FlightPage(driver)


    #login call
    login.click_login()

    #planner call
    planner_page.click_plan()
    planner_page.select_travel_month()
    planner_page.click_from_location()
    planner_page.enter_from_location()
    planner_page.click_from_list()

    #filter call
    filter_page.click_international()
    filter_page.click_pollution_free()
    filter_page.click_malaysia()


    #malaysia_page call
    malaysia_page.scroll_places_to_visit()
    malaysia_page.click_art()
    malaysia_page.click_perhentian_islands()

    #google_map
    google_map.verify_google_map_page()


    #malaysia
    malaysia_page.close_popup()
    malaysia_page.scroll_how_to_travel()
    malaysia_page.click_book_now()


    #flight
    flight_page.switch_to_flight_tab()
    flight_page.click_first_flight_details()