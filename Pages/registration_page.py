from Pages.locators import Locators
from Testdata.testdata import TestData
from Pages.base_page import BasePage
import re


class RegistrationPage(BasePage):

    def type_invalid_fake_email(self):
        self.enter_txt(Locators.HomePage.email_box, self.fake.email())

    def type_invalid_fake_paswd(self, is_use_email_flow):
        password_input = self.find_element((Locators.HomePage.password_box, Locators.HomePage.valid_password)
        [is_use_email_flow])
        password_input.send_keys(re.sub("[^A-Z]", "", self.fake.password(7).lower(), 7, re.IGNORECASE))

    def click_to_signUp(self):
        self.click_on(Locators.HomePage.signUp_btn, 60)

    def validate_improper_password_message(self):
        error_message = self.find_element(Locators.HomePage.incorrect_password_message).text
        expected_error_message = TestData.password_to_short
        assert expected_error_message == error_message, f"Oczekiwany komunikat: '{expected_error_message}" \
                                                        f"', otrzymany komunikat: '{error_message}'"