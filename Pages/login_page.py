from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.base_page import BasePage
from Pages.locators import Locators
from Testdata.testdata import TestData


class LoginPage(BasePage):

   def login_to_page(self):
        self.click_on(*Locators.HomePage.go_to_login_btn, 60)

   def type_valid_email(self):
        self.enter_txt(*Locators.HomePage.email_box, TestData.email)

   def type_valid_pswd(self):
       self.enter_txt(*Locators.HomePage.valid_password, TestData.valid_pswd)
       self.click_on(*Locators.HomePage.loogin_accept_btn, 60)

   def type_invalid_short_pswd(self):
        self.click_on(*Locators.HomePage.valid_password, TestData.invalid_pswd)

   def click_login_button(self):
       self.click_on(*Locators.HomePage.loogin_accept_btn, 60)
       self.click_on(*Locators.HomePage.incorrect_login_alert, 60)

   def validate_login_data_allert_msg(self):
       WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.HomePage.incorrect_login_alert))
       login_error_message_element = self.find_element(*Locators.HomePage.incorrect_login_alert)
       error_message = login_error_message_element.text
       expected_error_message = TestData.incorrect_login_information
       assert expected_error_message == error_message, f"Oczekiwany komunikat: '{expected_error_message}'" \
                                                       f", otrzymany komunikat: '{error_message}'"