from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def wait_for_element_to_disappear(self, locator):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))

    def wait_for_element_to_appear(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def long_wait_for_element_to_appear(self, locator):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(locator))

    def is_element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def get_text_from_element(self, locator):
        element_text = self.driver.find_element(*locator).text
        return element_text

    def hover_over_element(self, locator):
        element = self.driver.find_element(*locator)
        self.actions.move_to_element(element).perform()
