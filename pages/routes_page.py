from pages.base_page import BasePage
from locators.routes_locators import RoutesLocators
from data.addresses import *

class RoutesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RoutesLocators()

    def wait_for_page_to_load(self):
        self.wait_for_element_to_appear(self.locators.FROM_INPUT_FIELD_LOCATOR)

    def fill_in_from_field_with_hamovnicheskiyi(self):
        self.send_keys_to_input(self.locators.FROM_INPUT_FIELD_LOCATOR, keys=HAMOVNICHESKIYI_VAL)

    def fill_in_to_field_with_hamovnicheskiyi(self):
        self.send_keys_to_input(self.locators.TO_INPUT_FIELD_LOCATOR, keys=HAMOVNICHESKIYI_VAL)

    def fill_in_from_field_with_zubovski(self):
        self.send_keys_to_input(self.locators.FROM_INPUT_FIELD_LOCATOR, keys=ZUBOVSKI_BOULEVARD)

    def fill_in_to_field_with_zubovski(self):
        self.send_keys_to_input(self.locators.TO_INPUT_FIELD_LOCATOR, keys=ZUBOVSKI_BOULEVARD)

    def is_hamovnicheskiyi_point_present(self):
        return self.is_element_visible(self.locators.HAMOVNICHESKIYI_VAL_MAP_PIN_LOCATOR)

    def is_zubovski_point_present(self):
        return self.is_element_visible(self.locators.ZUBOVSKI_BOULEVARD_MAP_PIN_LOCATOR)

    def wait_for_route_to_load(self):
        self.wait_for_element_to_appear(self.locators.MAP_PIN_LOCATOR)

    def is_route_picker_block_present(self):
        return self.is_element_visible(self.locators.ROUTE_PICKER_BLOCK_SHOWN_LOCATOR)

    def is_auto_free_of_charge_text_present(self):
        return self.is_element_visible(self.locators.AUTO_FREE_OF_CHARGE_TEXT_LOCATOR)

    def is_time_en_route_zero_text_present(self):
        return self.is_element_visible(self.locators.TIME_EN_ROUTE_ZERO_TEXT_LOCATOR)

    def click_on_optimal_route(self):
        self.click_on_element(self.locators.OPTIMAL_ROUTE_TAB_LOCATOR)

    def is_optimal_route_tab_active(self):
        return self.is_element_visible(self.locators.OPTIMAL_ROUTE_TAB_ACTIVE_LOCATOR)

    def wait_for_optimal_route_to_load(self):
        self.wait_for_element_to_appear(self.locators.OPTIMAL_ROUTE_TAB_ACTIVE_LOCATOR)

    def click_on_fast_route(self):
        self.click_on_element(self.locators.FAST_ROUTE_TAB_LOCATOR)

    def is_fast_route_tab_active(self):
        return self.is_element_visible(self.locators.FAST_ROUTE_TAB_ACTIVE_LOCATOR)

    def wait_for_fast_route_to_load(self):
        self.wait_for_element_to_appear(self.locators.FAST_ROUTE_TAB_ACTIVE_LOCATOR)

    def click_on_my_route(self):
        self.click_on_element(self.locators.MY_ROUTE_TAB_LOCATOR)

    def is_my_route_tab_active(self):
        return self.is_element_visible(self.locators.MY_ROUTE_TAB_ACTIVE_LOCATOR)

    def wait_for_my_route_to_load(self):
        self.wait_for_element_to_appear(self.locators.MY_ROUTE_TAB_ACTIVE_LOCATOR)

    def get_transport_and_cost_text(self):
        return self.get_text_from_element(self.locators.TRANSPORT_AND_COST_TEXT_LOCATOR)

    def get_duration_text(self):
        return self.get_text_from_element(self.locators.DURATION_TEXT_LOCATOR)

    def is_order_taxi_button_present(self):
        return self.is_element_visible(self.locators.ORDER_TAXI_BUTTON_LOCATOR)

    def click_on_order_taxi_button(self):
        self.click_on_element(self.locators.ORDER_TAXI_BUTTON_LOCATOR)

    def click_on_drive_type(self):
        self.click_on_element(self.locators.DRIVE_ROUTE_TYPE_ACTIVE_LOCATOR)

    def wait_for_drive_type_to_load(self):
        self.wait_for_element_to_appear(self.locators.RESERVE_A_CAR_BUTTON_LOCATOR)

    def is_reserve_a_car_button_present(self):
        return self.is_element_visible(self.locators.RESERVE_A_CAR_BUTTON_LOCATOR)

    def wait_for_tariff_form_to_load(self):
        self.wait_for_element_to_appear(self.locators.TARIFF_FORM_LOCATOR)

    def is_tariff_form_present(self):
        return self.is_element_visible(self.locators.TARIFF_FORM_LOCATOR)

    def create_route_from_hamovnicheskiyi_to_zubovski(self):
        self.wait_for_page_to_load()
        self.fill_in_from_field_with_hamovnicheskiyi()
        self.fill_in_to_field_with_zubovski()
        self.wait_for_route_to_load()

    def create_route_from_zubovski_to_zubovski(self):
        self.wait_for_page_to_load()
        self.fill_in_from_field_with_zubovski()
        self.fill_in_to_field_with_zubovski()
        self.wait_for_route_to_load()

    def choose_optimal_route(self):
        self.click_on_optimal_route()
        self.wait_for_optimal_route_to_load()

    def choose_my_route(self):
        self.click_on_my_route()
        self.wait_for_my_route_to_load()

    def choose_fast_route(self):
        self.click_on_fast_route()
        self.wait_for_fast_route_to_load()

    def choose_drive_type(self):
        self.click_on_drive_type()
        self.wait_for_drive_type_to_load()

    def start_taxi_order(self):
        self.choose_fast_route()
        self.click_on_order_taxi_button()
        self.wait_for_tariff_form_to_load()

    def are_all_route_types_active(self):
        return (
                self.is_element_visible(self.locators.CAR_ROUTE_TYPE_ACTIVE_LOCATOR) and
                self.is_element_visible(self.locators.WALK_ROUTE_TYPE_ACTIVE_LOCATOR) and
                self.is_element_visible(self.locators.TAXI_ROUTE_TYPE_ACTIVE_LOCATOR) and
                self.is_element_visible(self.locators.BIKE_ROUTE_TYPE_ACTIVE_LOCATOR) and
                self.is_element_visible(self.locators.SCOOTER_ROUTE_TYPE_ACTIVE_LOCATOR) and
                self.is_element_visible(self.locators.DRIVE_ROUTE_TYPE_ACTIVE_LOCATOR)
                )
