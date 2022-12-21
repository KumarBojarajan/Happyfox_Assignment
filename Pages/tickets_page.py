import time
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.priority_page import PriorityPage
from Pages.status_page import StatusPage
from Resources.ui_repository import TicketPageLocators
from Config.config import TestData
class TicketsPage(BasePage):
    
    """Constructor of Ticket page"""
    def __init__(self, driver):
        super().__init__(driver)
    
    """TicketPage Actions"""
    def navigate_to_settings(self, settings_name):
        try:
            self.do_mouse_hover(By.CSS_SELECTOR, TicketPageLocators.TITLE_BAR)
            self.do_click(By.CSS_SELECTOR, TicketPageLocators.SETTINGS.format(settings_name))
            if settings_name == 'priorities':
                return PriorityPage(self.driver)
            if settings_name == 'statuses':
                return StatusPage(self.driver)
        except Exception as exc:
            print("navigate_to_settings: failed to navigate to settings {}".format(settings_name))
            print("navigate_to_settings: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def search_ticket(self):
        try:
            self.do_click(By.CSS_SELECTOR, TicketPageLocators.ALL_TICKETS)
            self.do_click(By.CSS_SELECTOR, TicketPageLocators.GLOBAL_SEARCH)
            # self.do_clear_input(By.CSS_SELECTOR, TicketPageLocators.SEARCH_INPUT)
            self.do_send_keys(By.CSS_SELECTOR, TicketPageLocators.SEARCH_INPUT, TestData.TICKET_SUBJECT, press_enter='yes')
            self.driver.implicitly_wait(30)
            return True
        except Exception as exc:
            print("search_ticket: failed to find ticket {}".format(TestData.TICKET_SUBJECT))
            print("search_ticket: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def get_ticket_status(self, search_ticket = "Yes"):
        try:
            if search_ticket:
                self.search_ticket()
                self.do_click(By.CSS_SELECTOR, TicketPageLocators.TEST_TICKET.format(TestData.TICKET_SUBJECT))
            status = self.get_element_text(By.CSS_SELECTOR, TicketPageLocators.TEST_TICKET_STATUS)
            print(status)
            return status
        except Exception as exc:
            print("get_ticket_status: failed to get ticket {} status".format(TestData.TICKET_SUBJECT))
            print("get_ticket_status: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def get_ticket_priority(self, search_ticket = "Yes"):
        try:
            if search_ticket:
                self.search_ticket()
                self.do_click(By.CSS_SELECTOR, TicketPageLocators.TEST_TICKET.format(TestData.TICKET_SUBJECT)) 
            priority = self.get_element_text(By.CSS_SELECTOR, TicketPageLocators.TEST_TICKET_PRIORITY)
            print(priority)
            return priority
        except Exception as exc:
            print("get_ticket_priority: failed to get ticket {} priority".format(TestData.TICKET_SUBJECT))
            print("get_ticket_priority: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
    
    def reply_to_ticket(self, search_ticket = "Yes"):
        try:
            if search_ticket:
                self.search_ticket()
                self.do_click(By.CSS_SELECTOR, TicketPageLocators.TEST_TICKET.format(TestData.TICKET_SUBJECT))
            self.do_click(By.CSS_SELECTOR, TicketPageLocators.REPLY)
            self.do_click(By.CSS_SELECTOR, TicketPageLocators.CANNED_ACTION_DROP_DOWN_BOX)
            canned_action_elements = self.do_find_elements(By.CSS_SELECTOR, TicketPageLocators.CANNED_ACTIONS)
            for action_el in canned_action_elements:
                action_name = action_el.text
                print(action_name)
                if action_name == TestData.CANNED_ACTION_TYPE:
                    action_el.click()
                    time.sleep(5)
                    break
            self.do_click(By.CSS_SELECTOR, TicketPageLocators.CANNED_ACTION_APPLY_BUTTON)
            self.do_click(By.CSS_SELECTOR, TicketPageLocators.ADD_REPLY_BUTTON)
            return True
        except Exception as exc:
            print("reply_to_ticket: failed to reply to the ticket {}".format(TestData.TICKET_SUBJECT))
            print("reply_to_ticket: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False
        
    
    def get_latest_ticket_update(self, search_ticket = "Yes"):
        try:
            if search_ticket:
                self.search_ticket()
                self.do_click(By.CSS_SELECTOR, TicketPageLocators.TEST_TICKET.format(TestData.TICKET_SUBJECT))
            self.do_click(By.CSS_SELECTOR, TicketPageLocators.EXPAND_TICKET_UPDATES)
            time.sleep(7)
            latest_updates = self.do_find_elements(By.XPATH, TicketPageLocators.LATEST_TICKET_UPDATES)
            ticket_updates = []
            for update in latest_updates:
                ticket_updates.append(update.text)
            print(ticket_updates)
            return ticket_updates
        except Exception as exc:
            print("get_latest_ticket_update: failed to get latest updates of the ticket {}".format(TestData.TICKET_SUBJECT))
            print("get_latest_ticket_update: failed with exception {}".format(str(exc)))
            self.take_screenshot(__name__)
            return False