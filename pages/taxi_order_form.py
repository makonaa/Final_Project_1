from locators.taxi_order_form_locators import TaxiOrderFormLocators
from pages.base_page import BasePage


class TaxiOrderForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = TaxiOrderFormLocators()

    def wait_for_tariff_form_to_load(self):
        self.wait_for_element_to_appear(self.locators.TARIFF_FORM_LOCATOR)

    def is_tariff_form_present(self):
        return self.is_element_visible(self.locators.TARIFF_FORM_LOCATOR)

    def click_on_tariff(self, tariff_locator:tuple):
        self.click_on_element(tariff_locator)

    def hover_over_tariff_info(self, icon_locator:tuple):
        self.hover_over_element(icon_locator)

    def wait_for_tariff_popup_to_open(self, popup_locator:tuple):
        self.wait_for_element_to_appear(popup_locator)

    def get_text_from_tariff_popup(self, text_locator:tuple) -> str:
        return self.get_text_from_element(text_locator)

    def click_on_working_tariff(self):
        self.click_on_element(self.locators.WORKING_TARIFF_LOCATOR)

    def wait_for_working_tariff_requirements_to_load(self):
        self.wait_for_element_to_appear(self.locators.ORDER_REQUIREMENTS_BLOCK_LOCATOR)

    def click_on_working_tariff_requirements_block(self):
        self.click_on_element(self.locators.ORDER_REQUIREMENTS_BLOCK_LOCATOR)

    def click_on_laptop_table_toggle(self):
        self.click_on_element(self.locators.LAPTOP_TABLE_TOGGLE_LOCATOR)

    def click_on_order_button(self):
        self.click_on_element(self.locators.ORDER_BUTTON_LOCATOR)

    def get_price_for_selected_tariff(self):
        return self.get_text_from_element(self.locators.PRICE_FOR_CURRENT_TARIFF)

    def is_any_tariff_selected(self):
        return self.is_element_visible(self.locators.TARIFF_SELECTED_LOCATOR)

    def are_all_tariffs_present(self):
        return (self.is_element_visible(self.locators.WORKING_TARIFF_LOCATOR) and
                self.is_element_visible(self.locators.SLEEPY_TARIFF_LOCATOR) and
                self.is_element_visible(self.locators.VACATION_TARIFF_LOCATOR) and
                self.is_element_visible(self.locators.TALKING_TARIFF_LOCATOR) and
                self.is_element_visible(self.locators.COMFORTING_TARIFF_LOCATOR) and
                self.is_element_visible(self.locators.CHIC_TARIFF_LOCATOR))

    def choose_working_tariff_with_laptop_table(self):
        self.click_on_working_tariff()
        self.wait_for_working_tariff_requirements_to_load()
        self.click_on_working_tariff_requirements_block()
        self.click_on_laptop_table_toggle()

    def check_out_tariff_info(self, tariff_locator:tuple, icon_locator:tuple, popup_locator:tuple):
        self.click_on_tariff(tariff_locator)
        self.hover_over_tariff_info(icon_locator)
        self.wait_for_tariff_popup_to_open(popup_locator)

    def check_if_all_user_info_fields_present(self):
        return (
            self.is_element_visible(self.locators.PHONE_FIELD_LOCATOR) and
            self.is_element_visible(self.locators.PAYMENT_METHOD_LOCATOR) and
            self.is_element_visible(self.locators.COMMENT_FOR_DRIVER_FIELD_LOCATOR) and
            self.is_element_visible(self.locators.ORDER_REQUIREMENTS_BLOCK_LOCATOR) and
            self.is_element_visible(self.locators.ORDER_BUTTON_LOCATOR)
        )
