from time import sleep

from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Pages.base_page import BasePage
from Pages.locators import Locators
from Testdata.testdata import TestData


class HomePage(BasePage):
    @staticmethod
    def navigate(driver, url):
        page = HomePage(driver, url)
        page.navigate_to()
        page.click_on(Locators.HomePage.cookie_accept_btn, 360)
        return page

    def useEmailIfIncessary(self):
        try:
            WebDriverWait(self.driver, 2).until(
                expected_conditions.visibility_of_element_located(Locators.HomePage.use_email))
            email_path_element = self.find_element(*Locators.HomePage.use_email)
            email_path_element.click()

            return True
        except:
            return False
