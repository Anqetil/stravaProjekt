from Pages.base_page import BasePage
from Pages.locators import Locators

class HomePage(BasePage):
    @staticmethod
    def navigate(driver, url):
        page = HomePage(driver, url)
        page.navigate_to()
        page.click_on(Locators.HomePage.cookie_accept_btn, 360)
        return page

    def useEmailIfIncessary(self):
        try:
            email_path_element = self.find_element(Locators.HomePage.use_email)
            email_path_element.click()

            return True
        except:
            return False