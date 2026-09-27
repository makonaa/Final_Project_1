import allure


class TestOrderConfirmationWindow:
    @allure.title('Тест - окно ожидания открывается при заказе такси')
    def test_taxi_order_searching_car_window(self, routes_page, taxi_order_form, order_confirmation_window):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.start_taxi_order()
        taxi_order_form.choose_working_tariff_with_laptop_table()
        taxi_order_form.click_on_order_button()
        order_confirmation_window.wait_for_order_confirmation_window_to_load()
        assert order_confirmation_window.are_all_ui_elements_for_searching_car_window_present()

    @allure.title('Тест - окно с информацией о водителе открывается после окончания ожидания')
    def test_taxi_order_driver_arrival_window(self, routes_page, taxi_order_form, order_confirmation_window):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.start_taxi_order()
        taxi_order_form.choose_working_tariff_with_laptop_table()
        taxi_order_form.click_on_order_button()
        order_confirmation_window.wait_for_timer_to_finish()
        assert order_confirmation_window.are_all_ui_elements_for_driver_arrival_window_present()

    @allure.title('Тест - цена в деталях заказа соотвествует цене, которая была обозначена при оформлении заказа')
    def test_cost_is_shown_when_clicking_details(self, routes_page, taxi_order_form, order_confirmation_window):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.start_taxi_order()
        taxi_order_form.choose_working_tariff_with_laptop_table()
        expected_price = taxi_order_form.get_price_for_selected_tariff().replace(" ", "")
        taxi_order_form.click_on_order_button()
        order_confirmation_window.wait_for_order_confirmation_window_to_load()
        order_confirmation_window.click_on_details_button()
        order_confirmation_window.wait_for_details_to_load()
        actual_price = order_confirmation_window.get_price_from_details()
        assert expected_price in actual_price

    @allure.title('Тест - кнопка отмены закрывает окно ожидания')
    def test_cancel_button_closes_confirmation_window(self, routes_page, taxi_order_form, order_confirmation_window):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.start_taxi_order()
        taxi_order_form.choose_working_tariff_with_laptop_table()
        taxi_order_form.click_on_order_button()
        order_confirmation_window.wait_for_order_confirmation_window_to_load()
        order_confirmation_window.click_on_cancel_button()
        order_confirmation_window.wait_for_confirmation_window_to_close()
        assert not order_confirmation_window.is_header_present()
