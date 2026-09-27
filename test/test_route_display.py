import allure


class TestRouteDisplay:
    @allure.title('Тест - точки начала и конца отображаются на карте при выборе двух разных точек')
    def test_start_and_end_points_present_for_route_with_different_addresses(self, routes_page):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        assert routes_page.is_hamovnicheskiyi_point_present() and routes_page.is_zubovski_point_present()

    @allure.title('Тест - блок с выбором маршрута отображается при выборе двух разных точек')
    def test_route_picker_block_shown_for_route_with_different_addresses(self, routes_page):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        assert routes_page.is_route_picker_block_present()

    @allure.title('Тест - при вводе одинаковых адресов отображается блок с текстом - "Авто Бесплатно В пути 0 мин."')
    def test_route_picker_block_shows_zero_time_for_route_with_same_addresses(self, routes_page):
        routes_page.create_route_from_zubovski_to_zubovski()
        assert routes_page.is_auto_free_of_charge_text_present() and routes_page.is_time_en_route_zero_text_present()

    @allure.title('Тест - при переключении между видами маршрута происходит смена активного таба')
    def test_optimal_route_tab_active_when_selecting(self, routes_page):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.choose_optimal_route()
        assert routes_page.is_optimal_route_tab_active()

    @allure.title('Тест - при переключении между видами маршрута происходит перерасчет цены и времени')
    def test_duration_and_cost_change_when_selecting_another_route(self, routes_page):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        initial_transport_and_cost = routes_page.get_transport_and_cost_text()
        initial_duration = routes_page.get_duration_text()
        routes_page.choose_optimal_route()
        final_transport_and_cost = routes_page.get_transport_and_cost_text()
        final_duration = routes_page.get_duration_text()
        assert (initial_transport_and_cost != final_transport_and_cost) and (initial_duration != final_duration)

    @allure.title('Тест - при переключении на Свой маршрут происходит смена активного таба')
    def test_my_route_tab_active_when_selecting(self, routes_page):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.choose_my_route()
        assert routes_page.is_my_route_tab_active()

    @allure.title('Тест - при переключении на Свой маршрут все виды передвижений становятся доступны')
    def test_all_route_types_active_when_selecting_my_route(self, routes_page):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.choose_my_route()
        assert routes_page.are_all_route_types_active()

    @allure.title('Тест - при переключении на Быстрый маршрут появляется кнопка заказа такси')
    def test_order_taxi_button_present_when_selecting_fast_route(self, routes_page):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.choose_fast_route()
        assert routes_page.is_order_taxi_button_present()

    @allure.title('Тест - при переключении на Свой маршрут и выбора передвижения Драйв появляется кнопка бронирования машины')
    def test_reserve_a_car_button_active_when_selecting_my_route_with_drive_type(self, routes_page):
        routes_page.create_route_from_hamovnicheskiyi_to_zubovski()
        routes_page.choose_my_route()
        routes_page.choose_drive_type()
        assert routes_page.is_reserve_a_car_button_present()
