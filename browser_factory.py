from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

class BrowserFactory:
    @staticmethod
    def get_driver(browser_name:str, headless:bool=False):
        if browser_name.lower() == 'chrome':
            options = ChromeOptions()
            if headless:
                options.add_argument('--headless')
            return webdriver.Chrome(options=options)
        else:
            raise NotImplementedError(
                f'{browser_name} is not supported for current test runs.'
            )
