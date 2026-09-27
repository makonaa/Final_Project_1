from browser_factory import BrowserFactory
import pytest
from Urls import BASE_URL
from pages.order_confirmation_window import OrderConfirmationWindow
from pages.routes_page import RoutesPage
from pages.taxi_order_form import TaxiOrderForm


@pytest.fixture(params=['chrome'])
def driver(request):
    driver = BrowserFactory.get_driver(request.param)
    driver.browser_name = request.param
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def routes_page(driver):
    return RoutesPage(driver)

@pytest.fixture
def taxi_order_form(driver):
    return TaxiOrderForm(driver)

@pytest.fixture
def order_confirmation_window(driver):
    return OrderConfirmationWindow(driver)
