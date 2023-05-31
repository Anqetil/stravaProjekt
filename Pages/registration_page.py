from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Pages.locators import Locators
from Testdata.testdata import TestData
from Pages.base_page import BasePage
from faker import Faker
import re


class RegistrationPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    #     self.fake = Faker("pl_PL")

    # def accept_cookie(self):
    #     self.driver.find_element(*Locators.HomePage.cookie_accept_btn).click()


    def type_invalid_fake_email(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located
                                            (Locators.HomePage.email_box))
        self.click_on(*Locators.HomePage.email_box, self.fake.email())

    def type_invalid_fake_paswd(self, is_use_email_flow):
        password_input = self.find_element(*((Locators.HomePage.password_box, Locators.HomePage.valid_password)
        [is_use_email_flow]))
        password_input.send_keys(re.sub("[^A-Z]", "", self.fake.password(7).lower(), 7, re.IGNORECASE))

    def click_to_signUp(self):
        self.click_on(*Locators.HomePage.signUp_btn, 60)

    def validate_improper_password_message(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located
                                             (Locators.HomePage.incorrect_password_message))
        error_message = self.find_element(*Locators.HomePage.incorrect_password_message).text
        expected_error_message = TestData.password_to_short
        assert expected_error_message == error_message, f"Oczekiwany komunikat: '{expected_error_message}" \
                                                        f"', otrzymany komunikat: '{error_message}'"