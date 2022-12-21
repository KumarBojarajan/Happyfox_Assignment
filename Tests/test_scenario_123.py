from Tests.test_base import Test_BaseAgent, Test_BaseCustomer
from Config.config import TestData
import time
class Test_Home(Test_BaseAgent, Test_BaseCustomer):
    
    def test_launch_agent_portal(self):
        self.loginpage = self.get_login_page_instance()
        assert self.loginpage.launch_agent_portal() == True
        tickets_page_instance = self.loginpage.do_login()
        assert (tickets_page_instance not in set([False, None])) == True, "expected ticket_page_instance but got {}".format(tickets_page_instance)
           
    def test_create_status(self):
        status_page_instance = self.get_tickets_page_instance().navigate_to_settings("statuses")
        assert (status_page_instance not in set([False, None])) == True, "expected status_page_instance but got {}".format(status_page_instance)
        assert status_page_instance.create_status() == True
    
    def test_make_status_default(self):
        assert self.get_status_page_instance().make_status_default() == True
    
    def test_create_priority(self):
        priority_page_instance = self.get_tickets_page_instance().navigate_to_settings("priorities")
        assert (priority_page_instance not in set([False, None])) == True, "expected priority_page_instance but got {}".format(priority_page_instance)
        assert priority_page_instance.create_priority() == True
    
    def test_make_priority_default(self):
        assert self.get_priority_page_instance().make_priority_default() == True
    
    def test_create_new_ticket(self):
        support_page_instance = self.get_support_page_instance()
        assert support_page_instance.launch_support_portal() == True
        assert support_page_instance.create_ticket() == True
        time.sleep(7)

    def test_new_ticket_created_with_default_priority(self):
        priority_page_instance = self.get_priority_page_instance()
        assert priority_page_instance.navigate_to_module('tickets') == True
        ticket_page_instance = self.get_tickets_page_instance()
        assert ticket_page_instance.get_ticket_priority() == TestData.PRIORITY_NAME
    
    def test_new_ticket_created_with_default_status(self):
        ticket_page_instance = self.get_tickets_page_instance()
        assert ticket_page_instance.get_ticket_status(search_ticket=None) == TestData.STATUS_NAME
    
    def test_ticket_reply(self):
        ticket_page_instance = self.get_tickets_page_instance()
        assert ticket_page_instance.reply_to_ticket(search_ticket=None) == True
    
    def test_ticket_updated_details(self):
        expected_updates = ["Priority changed from {}".format(TestData.PRIORITY_NAME), "Status changed from {}".format(TestData.STATUS_NAME), "Added tags"]
        ticket_page_instance = self.get_tickets_page_instance()
        ticket_updates = ticket_page_instance.get_latest_ticket_update(search_ticket=None)
        print(ticket_updates)
        assert ticket_updates != False
        check_update_flag = True
        for i in range(len(ticket_updates)):
            if expected_updates[i] not in ticket_updates[i]:
                check_update_flag = False
                break
        assert check_update_flag == True
    
    def test_delete_status(self):
        status_page_instance = self.get_tickets_page_instance().navigate_to_settings("statuses")
        assert (status_page_instance not in set([False, None])) == True, "expected status_page_instance but got {}".format(status_page_instance)
        assert status_page_instance.delete_status(is_default=True) == True
    
    def test_delete_priority(self):
        priority_page_instance = self.get_tickets_page_instance().navigate_to_settings("priorities")
        assert (priority_page_instance not in set([False, None])) == True, "expected priority_page_instance but got {}".format(priority_page_instance)
        assert priority_page_instance.delete_priority(is_default=True) == True
    
    def test_agent_logout(self):
        login_page_instance = self.get_login_page_instance()
        assert login_page_instance.do_logout() == True