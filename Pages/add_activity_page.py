from Pages.locators import Locators
from Testdata.testdata import TestData
from Pages.base_page import BasePage

class AddManualyActivity(BasePage):
    def add_entry(self):
        self.click_on(*Locators.TrainingPage.select_training, 60)
        self.click_on(*Locators.TrainingPage.manual_entry_training, 60)
        self.click_on(*Locators.TrainingPage.distance_btn, 60)
        self.enter_txt(*Locators.TrainingPage.distance_btn, TestData.dictance)

        hour_input = self.find_element(*Locators.TrainingPage.hours_btn)
        hour_input.clear()
        hour_input.send_keys(TestData.hours)

        minute_input = self.find_element(*Locators.TrainingPage.minute_btn)
        minute_input.clear()
        minute_input.send_keys(TestData.minutes)

        second_input = self.find_element(*Locators.TrainingPage.seconds_btn)
        second_input.clear()
        second_input.send_keys(TestData.seconds)

        self.enter_txt(*Locators.TrainingPage.elevation_gain_btn, TestData.elevation)
        title_input = self.find_element(*Locators.TrainingPage.title_btn)
        title_input.clear()
        title_input.send_keys(TestData.training_title)
        self.enter_txt(*Locators.TrainingPage.description_btn, TestData.training_description)
        self.click_on(*Locators.TrainingPage.create_training_btn, 60)