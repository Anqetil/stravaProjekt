from Pages.locators import Locators
from Testdata.testdata import TestData
from time import  sleep
from Pages.base_page import BasePage


class DeleteEntry(BasePage):
    def delete_entry_after_adding(self):
        self.click_on(Locators.TrainingPage.actions_btn, 60)
        self.click_on(Locators.TrainingPage.delete_training_btn, 60)
        assert self.driver.switch_to.alert.text == TestData.warning_delete_message
        self.driver.switch_to.alert.accept()
        sleep(3)
        self.click_on(Locators.TrainingPage.dashboard_btn, 60)
        sleep(2)