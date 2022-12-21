from Tests.test_base import Test_BaseAgent
class Test_Scenario13(Test_BaseAgent):
    
    def test_launch_agent_portal(self):
        self.loginpage = self.get_login_page_instance()
        assert self.loginpage.launch_agent_portal() == True
        tickets_page_instance = self.loginpage.do_login()
        assert (tickets_page_instance not in set([False, None])) == True, "expected ticket_page_instance but got {}".format(tickets_page_instance)
           
    def test_create_status(self):
        status_page_instance = self.get_tickets_page_instance().navigate_to_settings("statuses")
        assert (status_page_instance not in set([False, None])) == True, "expected status_page_instance but got {}".format(status_page_instance)
        assert status_page_instance.create_status() == True
    
    def test_create_priority(self):
        priority_page_instance = self.get_tickets_page_instance().navigate_to_settings("priorities")
        assert (priority_page_instance not in set([False, None])) == True, "expected priority_page_instance but got {}".format(priority_page_instance)
        assert priority_page_instance.create_priority() == True
    
    def test_delete_status(self):
        status_page_instance = self.get_tickets_page_instance().navigate_to_settings("statuses")
        assert (status_page_instance not in set([False, None])) == True, "expected status_page_instance but got {}".format(status_page_instance)
        assert status_page_instance.delete_status() == True
    
    def test_delete_priority(self):
        priority_page_instance = self.get_tickets_page_instance().navigate_to_settings("priorities")
        assert (priority_page_instance not in set([False, None])) == True, "expected priority_page_instance but got {}".format(priority_page_instance)
        assert priority_page_instance.delete_priority() == True
    
    def test_agent_logout(self):
        login_page_instance = self.get_login_page_instance()
        assert login_page_instance.do_logout() == True