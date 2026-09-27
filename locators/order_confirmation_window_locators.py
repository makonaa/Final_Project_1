from selenium.webdriver.common.by import By


class OrderConfirmationWindowLocators:
    CONFIRMATION_WINDOW_LOCATOR = (By.CSS_SELECTOR, '.order-body')
    SEARCHING_FOR_CAR_HEADER_LOCATOR = (By.XPATH, '//div[text()="Поиск машины"]')
    TIMER_LOCATOR = (By.CSS_SELECTOR, '.order-header-time')
    CANCEL_BUTTON_LOCATOR = (By.XPATH, '//div[text()="Отменить"]/preceding-sibling::button')
    DETAILS_BUTTON_LOCATOR = (By.XPATH, '//div[text()="Детали"]/preceding-sibling::button')
    DRIVER_WILL_ARRIVE_HEADER_LOCATOR = (By.XPATH, '//div[text()=" мин. и приедет"]')
    LICENSE_PLATE_LOCATOR = (By.CSS_SELECTOR, '.number')
    CAR_IMAGE_LOCATOR = (By.CSS_SELECTOR, 'img[alt="Car"]')
    DRIVER_IMAGE_LOCATOR = (By.XPATH, '//img[contains(@src, "bender")]')
    DRIVER_NAME_LOCATOR = (By.XPATH, '//div[@class="order-btn-rating"]/../following-sibling::div')
    DRIVER_RATING_LOCATOR = (By.CSS_SELECTOR, '.order-btn-rating')
    ABOUT_THE_RIDE_DETAILS_LOCATOR = (By.XPATH, '//div[text()="Еще про поездку"]')
    DETAILS_PRICE_INFO_LOCATOR = (By.XPATH, '//img[@alt="Info"]/../..//div[@class="o-d-sh"]')
