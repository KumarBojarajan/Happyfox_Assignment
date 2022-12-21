from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Resources.ui_repository import PriorityPageLocators
from Config.config import TestData
class PriorityPage(BasePage):

    """Constructor of Priority page"""
    def __init__(self, driver):
        super().__init__(driver)
    
    """PriorityPage actions"""
    def create_priority(self):
        try:
            self.do_click(By.CSS_SELECTOR, PriorityPageLocators.NEW_PRIORITY_BUTTON)
            self.do_send_keys(By.CSS_SELECTOR, PriorityPageLocators.PRIORITY_NAME_INPUT, TestData.PRIORITY_NAME)
            self.do_send_keys(By.CSS_SELECTOR, PriorityPageLocators.PRIORITY_DESCRIPTION_INPUT, TestData.PRIORITY_DESCRIPTION)
            self.do_click(By.CSS_SELECTOR, PriorityPageLocators.ADD_PRIOTIY_BUTTON)
            self.driver.implicitly_wait(30)
            self.do_find_element((By.XPATH, PriorityPageLocators.TEST_PRIORITY.format(TestData.PRIORITY_NAME)))
            return True
        except Exception as exc:
            print("create_priority: failed to create priority {}".format(TestData.PRIORITY_NAME))
            print("create_priority: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def delete_priority(self, is_default=False):
        try:
            self.do_click(By.XPATH, PriorityPageLocators.TEST_PRIORITY.format(TestData.PRIORITY_NAME))
            self.do_click(By.CSS_SELECTOR, PriorityPageLocators.DELETE_PRIORITY_LINK)
            if is_default:
                self.do_click(By.XPATH, PriorityPageLocators.PRIORITY_DROP_DOWN_BOX)
                self.do_click(By.XPATH, PriorityPageLocators.CLOSING_PRIORITY_OPTION)
            self.do_click(By.XPATH, PriorityPageLocators.DELETE_PRIORITY_CONFIRMATION_BUTTON)
            self.do_click(By.CSS_SELECTOR, PriorityPageLocators.TOAST_MESSAGE)
            self.driver.implicitly_wait(20)
            self.do_check_element_not_exists(By.XPATH, PriorityPageLocators.TEST_PRIORITY.format(TestData.PRIORITY_NAME))
            return True
        except Exception as exc:
            print("delete_priority: failed to delete priority {}".format(TestData.PRIORITY_NAME))
            print("delete_priority: failed with execption {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False

    def make_priority_default(self):
        try:
            self.do_mouse_hover(By.XPATH, PriorityPageLocators.TEST_PRIORITY.format(TestData.PRIORITY_NAME))
            self.do_click(By.XPATH, PriorityPageLocators.MAKE_DEFAULT_LINK.format(TestData.PRIORITY_NAME))
            self.do_find_element((By.XPATH, PriorityPageLocators.DEFAULT_PRIORITY_TICK.format(TestData.PRIORITY_NAME)))
            return True
        except Exception as exc:
            print("make_priority_default: failed to make test priority {} default".format(TestData.PRIORITY_NAME))
            print("make_priority_default: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def navigate_to_module(self, module_name):
        try:
            self.do_mouse_hover(By.CSS_SELECTOR, PriorityPageLocators.TITLE_BAR)
            self.do_click(By.CSS_SELECTOR, PriorityPageLocators.MODULE.format(module_name))
            self.driver.implicitly_wait(20)
            return True
        except Exception as exc:
            print("navigate_to_module: failed to navigate_to_module {}".format(module_name))
            print("navigate_to_module: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False