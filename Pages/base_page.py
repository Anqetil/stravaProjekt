from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

class BasePage:
    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.fake = Faker("pl_PL")
        self.base_url = base_url

    def find_element(self, locator, timeout_sec=2):
        return WebDriverWait(self.driver, timeout_sec).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")

    def click_on(self, locator, timeout_sec):
        self.find_element(locator, timeout_sec).click()

    def navigate_to(self, url=''):
        url = self.base_url + url
        self.driver.get(url)
        self.driver.maximize_window()

    def enter_txt(self, locator, text):
        self.find_element(locator).send_keys(text)