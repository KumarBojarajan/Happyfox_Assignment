from Config.config import TestData
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.tickets_page import TicketsPage
from Resources.ui_repository import LoginPageLocators
class LoginPage(BasePage):
    
    """Constructor of the LoginPage class"""
    def __init__(self, driver):
        super().__init__(driver)
    
    """LoginPage Actions"""
    def launch_agent_portal(self):
        try:
            self.driver.get(TestData.AGENT_PORTAL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            return True
        except Exception as exc:
            print("launch_agent_portal: failed to launch_agent_portal {}".format(TestData.AGENT_PORTAL))
            print("launch_agent_portal: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def do_login(self):
        try:
            self.do_send_keys(By.NAME, LoginPageLocators.USERNAME, TestData.USER_NAME)
            self.do_send_keys(By.NAME, LoginPageLocators.PASSWORD, TestData.PASSWORD)
            self.do_click(By.CSS_SELECTOR, LoginPageLocators.LOGIN_BUTTON)
            self.driver.implicitly_wait(30)
            # returns landing page instance
            return TicketsPage(self.driver)
        except Exception as exc:
            print("do_login: agent {} failed to login".format(TestData.USER_NAME))
            print("do_login: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def do_logout(self):
        try:
            self.do_click(By.CSS_SELECTOR, LoginPageLocators.STAFF_MENU)
            self.do_click(By.CSS_SELECTOR, LoginPageLocators.LOGOUT_BUTTON)
            self.driver.implicitly_wait(30)
            self.do_find_element((By.CSS_SELECTOR, LoginPageLocators.LOGIN_BUTTON))
            return True
        except Exception as exc:
            print("do_logout: agent {} failed to logout".format(TestData.USER_NAME))
            print("do_logout: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False