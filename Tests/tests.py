import pytest
from Pages.registration_page import RegistrationPage
from Pages.login_page import LoginPage
from Pages.quest_home_page import HomePage
from Pages.delete_activity_page import DeleteEntry
from Pages.add_activity_page import AddManualyActivity
from selenium import webdriver
from Testdata.testdata import TestData

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(TestData.strava_url)
    assert TestData.welcome_strava_message in driver.title
    driver.maximize_window()
    yield driver
    driver.quit()


def test_registration_with_short_pswd(driver):
    useEmailIfIncessary = HomePage.navigate(driver, TestData.strava_url).useEmailIfIncessary()

    registrationpage = RegistrationPage(driver)
    registrationpage.type_invalid_fake_email()
    registrationpage.type_invalid_fake_paswd(useEmailIfIncessary)
    registrationpage.click_to_signUp()
    registrationpage.validate_improper_password_message()


def test_login_improper_data(driver):
    HomePage.navigate(driver, TestData.strava_url)
    loginpage = LoginPage(driver)
    loginpage.login_to_page()
    loginpage.type_valid_email()
    loginpage.type_invalid_short_pswd()
    loginpage.click_login_button()
    loginpage.validate_login_data_allert_msg()

def test_as_logged_adding_and_removing_training(driver):
    HomePage.navigate(driver, TestData.strava_url)
    loginpage = LoginPage(driver)
    loginpage.login_to_page()
    loginpage.type_valid_email()
    loginpage.type_valid_pswd()
    new_training = AddManualyActivity(driver)
    new_training.add_entry()
    training = DeleteEntry(driver)
    training.delete_entry_after_adding()
