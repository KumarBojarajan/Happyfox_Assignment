from Config.config import TestData
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Resources.ui_repository import SupportCenterPageLocators
import os
class SupportCenterPage(BasePage):
    
    """Constructor of the SupportCenterPage class"""
    def __init__(self, driver):
        super().__init__(driver)
    
    """SupportCenterPage Actions"""
    def launch_support_portal(self):
        try:
            self.driver.get(TestData.SUPPORT_PORTAL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
            return True
        except Exception as exc:
            print("launch_support_portal: failed to launch_support_portal {}".format(TestData.SUPPORT_PORTAL))
            print("launch_support_portal: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def create_ticket(self):
        try:
            try:
                attachment_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', TestData.FILE_PATH))
                print("\n Attachment_path {}".format(attachment_path))
            except OSError as err:
                print("create_ticket: cannot fetch attachment file path {}".format(str(err)))
                return False
            self.do_send_keys(By.CSS_SELECTOR, SupportCenterPageLocators.TICKET_SUBJECT_INPUT, TestData.TICKET_SUBJECT)
            self.do_send_keys(By.CSS_SELECTOR, SupportCenterPageLocators.TICKET_MESSAGE_INPUT, TestData.TICKET_MESSAGE)
            self.do_send_keys(By.CSS_SELECTOR, SupportCenterPageLocators.CUSTOMER_NAME_INPUT, TestData.TICKET_CUSTOMER_NAME)
            try:
                js_script_to_make_file_input_element_visible = "document.querySelector('{}').style.display='block'".format(SupportCenterPageLocators.FILE_ATTACHMENT_BOX)
                print("\n js_script_to_make_file_input_element_visible {}".format(js_script_to_make_file_input_element_visible))
                self.driver.execute_script(js_script_to_make_file_input_element_visible)
            except Exception as jsexc:
                print("create_ticket: js_script_to_make_file_input_element_visible failed {}".format(str(jsexc)))
                return False
            self.do_send_keys(By.CSS_SELECTOR, SupportCenterPageLocators.FILE_ATTACHMENT_BOX, attachment_path)
            self.do_find_element((By.CSS_SELECTOR, SupportCenterPageLocators.ATTACHED_FILE))
            self.do_send_keys(By.CSS_SELECTOR, SupportCenterPageLocators.CUSTOMER_EMAIL_INPUT, TestData.TICKET_CUSTOMER_EMAIL)
            self.do_click(By.CSS_SELECTOR, SupportCenterPageLocators.CREATE_TICKET_BUTTON)
            self.driver.implicitly_wait(30)
            return True
        except Exception as exc:
            print("create_ticket: failed to create ticket with subject {}".format(TestData.TICKET_SUBJECT))
            print("create_ticket: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False