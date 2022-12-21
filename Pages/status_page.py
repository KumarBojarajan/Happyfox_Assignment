from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Resources.ui_repository import StatusPageLocators
from Config.config import TestData
import time
class StatusPage(BasePage):

    """Constructor of Status page"""
    def __init__(self, driver):
        super().__init__(driver)
    
    """StatusPage Actions"""
    def create_status(self):
        try:
            self.do_click(By.CSS_SELECTOR, StatusPageLocators.NEW_STATUS_BUTTON)
            self.do_send_keys(By.CSS_SELECTOR, StatusPageLocators.STATUS_NAME_INPUT, TestData.STATUS_NAME)
            self.do_click(By.CSS_SELECTOR, StatusPageLocators.STATUS_BEHAVIOUR)
            self.do_click(By.CSS_SELECTOR, StatusPageLocators.STATUS_BEHAVIOUR_OPTIONS)
            self.do_send_keys(By.CSS_SELECTOR, StatusPageLocators.STATUS_DESCRIPTION_INPUT, TestData.STATUS_DESCRIPTION)
            self.do_click(By.CSS_SELECTOR, StatusPageLocators.ADD_STATUS_BUTTON)
            self.driver.implicitly_wait(30)
            self.do_find_element((By.XPATH, StatusPageLocators.TEST_STATUS.format(TestData.STATUS_NAME)))
            return True
        except Exception as exc:
            print("create_status: failed to create status {}".format(TestData.STATUS_NAME))
            print("create_status: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def delete_status(self, is_default=False):
        try:
            self.do_click(By.XPATH, StatusPageLocators.TEST_STATUS.format(TestData.STATUS_NAME))
            self.do_click(By.CSS_SELECTOR, StatusPageLocators.DELETE_STATUS_BUTTON)
            if is_default:
                self.do_click(By.XPATH, StatusPageLocators.STATUS_DROP_DOWN_BOX)
                self.do_click(By.XPATH, StatusPageLocators.CLOSING_STATUS_OPTION)
            self.do_click(By.CSS_SELECTOR, StatusPageLocators.DELETE_STATUS_CONFIRM_BUTTON)
            self.do_click(By.CSS_SELECTOR, StatusPageLocators.TOAST_MESSAGE)
            time.sleep(5)
            self.do_check_element_not_exists(By.XPATH, StatusPageLocators.TEST_STATUS.format(TestData.STATUS_NAME))
            return True
        except Exception as exc:
            print("delete_status: failed to delete status {}".format(TestData.STATUS_NAME))
            print("delete_status: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False

    def make_status_default(self):
        try:
            self.do_mouse_hover(By.XPATH, StatusPageLocators.MAKE_DEFAULT_LINK.format(TestData.STATUS_NAME))
            self.do_click(By.XPATH, StatusPageLocators.MAKE_DEFAULT_LINK.format(TestData.STATUS_NAME))
            self.driver.implicitly_wait(30)
            self.do_find_element((By.XPATH, StatusPageLocators.DEFAULT_STATUS_TICK.format(TestData.STATUS_NAME)))
            return True
        except Exception as exc:
            print("make_status_default: failed to make status {} default".format(TestData.STATUS_NAME))
            print("make_status_default: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def navigate_to_module(self, module_name):
        try:
            self.do_mouse_hover(By.CSS_SELECTOR, StatusPageLocators.TITLE_BAR)
            self.do_click(By.CSS_SELECTOR, StatusPageLocators.MODULE.format(module_name))
            return True
        except Exception as exc:
            print("navigate_to_module: failed to navigate to module {}".format(TestData.module_name))
            print("navigate_to_module: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False