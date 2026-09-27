from data.tariff_parametrization import PARAMETRIZATION_LIST_FOR_INFO_POPUP, PARAMETRIZATION_FOR_USER_INFO, PARAMETRIZATION_IDS
import pytest
import allure

class TestTaxiOrder:
    @allure.title('Тест - Форма с тарифами открывается при заказе такси')
    def test_ordering_taxi_opens_order_form_with_tariffs(self, routes_page, taxi_order_form):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.start_taxi_order()
        taxi_order_form.wait_for_tariff_form_to_load()
        assert taxi_order_form.is_tariff_form_present()

    @allure.title('Тест - В форме присутствуют все 6 тарифов, один из которых выбран')
    def test_all_tariffs_are_present_with_one_selected_when_ordering_taxi(self, routes_page, taxi_order_form):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.start_taxi_order()
        taxi_order_form.wait_for_tariff_form_to_load()
        assert taxi_order_form.are_all_tariffs_present() and taxi_order_form.is_any_tariff_selected()

    @allure.title('Тест - Попап открывается для тарифа {expected_title_text}')
    @pytest.mark.parametrize("tariff, info_icon, pop_up, title, subtitle, expected_title_text, expected_subtitle_text",
                             PARAMETRIZATION_LIST_FOR_INFO_POPUP, ids=PARAMETRIZATION_IDS)
    def test_hovering_over_tariff_icon_opens_popup_with_details(self, routes_page, taxi_order_form,
                                                              tariff, info_icon, pop_up, title, subtitle,
                                                              expected_title_text, expected_subtitle_text):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.start_taxi_order()
        taxi_order_form.check_out_tariff_info(tariff_locator = tariff, icon_locator = info_icon, popup_locator = pop_up)
        actual_title_text = taxi_order_form.get_text_from_tariff_popup(title)
        actual_subtitle_text = taxi_order_form.get_text_from_tariff_popup(subtitle)
        assert (actual_title_text == expected_title_text) and (actual_subtitle_text == expected_subtitle_text)

    @allure.title('Тест - Поля с пользовательской информацией присутствуют для тарифа {expected_title_text}')
    @pytest.mark.parametrize("tariff", PARAMETRIZATION_FOR_USER_INFO, ids=PARAMETRIZATION_IDS)
    def test_user_info_form_is_present_when_ordering_any_tariff(self, routes_page, taxi_order_form, tariff):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.start_taxi_order()
        taxi_order_form.click_on_tariff(tariff)
        assert taxi_order_form.check_if_all_user_info_fields_present()
