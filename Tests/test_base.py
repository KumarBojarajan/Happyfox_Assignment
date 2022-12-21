import pytest
from Pages.login_page import LoginPage
from Pages.tickets_page import TicketsPage
from Pages.status_page import StatusPage
from Pages.priority_page import PriorityPage
from Pages.support_center_page import SupportCenterPage

@pytest.mark.usefixtures("agent_driver")
class Test_BaseAgent:
    def get_login_page_instance(self):
        return LoginPage(self.ag_driver)
    
    def get_tickets_page_instance(self):
        return TicketsPage(self.ag_driver)
    
    def get_status_page_instance(self):
        return StatusPage(self.ag_driver)
    
    def get_priority_page_instance(self):
        return PriorityPage(self.ag_driver)

@pytest.mark.usefixtures("customer_driver")
class Test_BaseCustomer:
    def get_support_page_instance(self):
        return SupportCenterPage(self.cust_driver)
