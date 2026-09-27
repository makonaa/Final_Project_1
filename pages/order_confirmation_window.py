from pages.base_page import BasePage
from locators.order_confirmation_window_locators import OrderConfirmationWindowLocators


class OrderConfirmationWindow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderConfirmationWindowLocators()

    def is_header_present(self):
        return self.is_element_visible(self.locators.SEARCHING_FOR_CAR_HEADER_LOCATOR)

    def is_cancel_button_present(self):
        return self.is_element_visible(self.locators.CANCEL_BUTTON_LOCATOR)

    def is_details_button_present(self):
        return self.is_element_visible(self.locators.DETAILS_BUTTON_LOCATOR)

    def is_timer_present(self):
        return self.is_element_visible(self.locators.TIMER_LOCATOR)

    def wait_for_order_confirmation_window_to_load(self):
        self.wait_for_element_to_appear(self.locators.SEARCHING_FOR_CAR_HEADER_LOCATOR)

    def wait_for_driver_arrival_header_to_load(self):
        self.long_wait_for_element_to_appear(self.locators.DRIVER_WILL_ARRIVE_HEADER_LOCATOR)

    def is_driver_arrival_header_present(self):
        return self.is_element_visible(self.locators.DRIVER_WILL_ARRIVE_HEADER_LOCATOR)

    def is_license_plate_present(self):
        return self.is_element_visible(self.locators.LICENSE_PLATE_LOCATOR)

    def is_car_image_present(self):
        return self.is_element_visible(self.locators.CAR_IMAGE_LOCATOR)

    def is_driver_name_present(self):
        return self.is_element_visible(self.locators.DRIVER_NAME_LOCATOR)

    def is_driver_image_present(self):
        return self.is_element_visible(self.locators.DRIVER_IMAGE_LOCATOR)

    def is_driver_rating_present(self):
        return self.is_element_visible(self.locators.DRIVER_RATING_LOCATOR)

    def click_on_details_button(self):
        self.click_on_element(self.locators.DETAILS_BUTTON_LOCATOR)

    def click_on_cancel_button(self):
        self.click_on_element(self.locators.CANCEL_BUTTON_LOCATOR)

    def get_price_from_details(self):
        return self.get_text_from_element(self.locators.DETAILS_PRICE_INFO_LOCATOR)

    def wait_for_details_to_load(self):
        self.wait_for_element_to_appear(self.locators.ABOUT_THE_RIDE_DETAILS_LOCATOR)

    def wait_for_confirmation_window_to_close(self):
        self.wait_for_element_to_disappear(self.locators.CONFIRMATION_WINDOW_LOCATOR)

    def wait_for_timer_to_finish(self):
        self.wait_for_order_confirmation_window_to_load()
        self.wait_for_driver_arrival_header_to_load()

    def are_all_ui_elements_for_searching_car_window_present(self):
        return (self.is_header_present() and self.is_cancel_button_present()
                and self.is_details_button_present() and self.is_timer_present())

    def are_all_ui_elements_for_driver_arrival_window_present(self):
        return (self.is_driver_arrival_header_present() and self.is_cancel_button_present()
                and self.is_details_button_present() and self.is_license_plate_present()
                and self.is_car_image_present() and self.is_driver_name_present()
                and self.is_driver_image_present() and self.is_driver_rating_present())
