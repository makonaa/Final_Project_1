from selenium.webdriver.common.by import By


class TaxiOrderFormLocators:
    TARIFF_FORM_LOCATOR = (By.CSS_SELECTOR, '.tariff-picker.shown')
    TARIFF_SELECTED_LOCATOR = (By.CSS_SELECTOR, '.tcard.active')

    WORKING_TARIFF_LOCATOR = (By.XPATH, '//div[@class="tcard-title"][text()="Рабочий"]')
    WORKING_TARIFF_INFO_ICON_LOCATOR = (By.CSS_SELECTOR, 'button[data-for="tariff-card-0"]')
    WORKING_TARIFF_POPUP_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-0')
    WORKING_TARIFF_POPUP_TITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-0 .i-title')
    WORKING_TARIFF_POPUP_SUBTITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-0 .i-dPrefix')

    SLEEPY_TARIFF_LOCATOR = (By.XPATH, '//div[@class="tcard-title"][text()="Сонный"]')
    SLEEPY_TARIFF_INFO_ICON_LOCATOR = (By.CSS_SELECTOR, 'button[data-for="tariff-card-1"]')
    SLEEPY_TARIFF_POPUP_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-1')
    SLEEPY_TARIFF_POPUP_TITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-1 .i-title')
    SLEEPY_TARIFF_POPUP_SUBTITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-1 .i-dPrefix')

    VACATION_TARIFF_LOCATOR = (By.XPATH, '//div[@class="tcard-title"][text()="Отпускной"]')
    VACATION_TARIFF_INFO_ICON_LOCATOR = (By.CSS_SELECTOR, 'button[data-for="tariff-card-2"]')
    VACATION_TARIFF_POPUP_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-2')
    VACATION_TARIFF_POPUP_TITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-2 .i-title')
    VACATION_TARIFF_POPUP_SUBTITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-2 .i-dPrefix')

    TALKING_TARIFF_LOCATOR = (By.XPATH, '//div[@class="tcard-title"][text()="Разговорчивый"]')
    TALKING_TARIFF_INFO_ICON_LOCATOR = (By.CSS_SELECTOR, 'button[data-for="tariff-card-3"]')
    TALKING_TARIFF_POPUP_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-3')
    TALKING_TARIFF_POPUP_TITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-3 .i-title')
    TALKING_TARIFF_POPUP_SUBTITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-3 .i-dPrefix')

    COMFORTING_TARIFF_LOCATOR = (By.XPATH, '//div[@class="tcard-title"][text()="Утешительный"]')
    COMFORTING_TARIFF_INFO_ICON_LOCATOR = (By.CSS_SELECTOR, 'button[data-for="tariff-card-4"]')
    COMFORTING_TARIFF_POPUP_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-4')
    COMFORTING_TARIFF_POPUP_TITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-4 .i-title')
    COMFORTING_TARIFF_POPUP_SUBTITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-4 .i-dPrefix')

    CHIC_TARIFF_LOCATOR = (By.XPATH, '//div[@class="tcard-title"][text()="Глянцевый"]')
    CHIC_TARIFF_INFO_ICON_LOCATOR = (By.CSS_SELECTOR, 'button[data-for="tariff-card-5"]')
    CHIC_TARIFF_POPUP_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-5')
    CHIC_TARIFF_POPUP_TITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-5 .i-title')
    CHIC_TARIFF_POPUP_SUBTITLE_LOCATOR = (By.CSS_SELECTOR, '#tariff-card-5 .i-dPrefix')

    PHONE_FIELD_LOCATOR = (By.XPATH, '//div[text()="Телефон"]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="form"]//div[text()="Способ оплаты"]')
    COMMENT_FOR_DRIVER_FIELD_LOCATOR = (By.CSS_SELECTOR, '#comment')
    ORDER_REQUIREMENTS_BLOCK_LOCATOR = (By.CSS_SELECTOR, '.reqs-header')
    ORDER_BUTTON_LOCATOR = (By.XPATH, '//span[text()="Ввести номер и заказать"]')
    PRICE_FOR_CURRENT_TARIFF = (By.CSS_SELECTOR, '.tcard.active .tcard-price')

    LAPTOP_TABLE_TOGGLE_LOCATOR = (By.CSS_SELECTOR, '.slider.round')
