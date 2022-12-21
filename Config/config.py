import uuid
class TestData:
    BROWSER = 'chrome'
    AGENT_PORTAL = "https://interview2.supporthive.com/staff"
    SUPPORT_PORTAL = 'https://interview2.supporthive.com/new'
    USER_NAME = "Agent1"
    PASSWORD = "Agent@123"
    TICKET_SUBJECT = "Internet connection issue" + str(uuid.uuid4())[-5:]
    TICKET_MESSAGE = "Slow internet connection"
    TICKET_CUSTOMER_NAME = "Test Customer"
    TICKET_CUSTOMER_EMAIL = "Customer@happyfox.com"
    STATUS_NAME = "ISSUE CREATED"
    STATUS_BEHAVIOUR = "Pending"
    STATUS_DESCRIPTION = "Status when a new ticket is created in HappyFox"
    PRIORITY_NAME = "ASSISTANCE REQUIRED"
    PRIORITY_DESCRIPTION = "Priority of the newly created tickets"
    CANNED_ACTION_TYPE = "Reply to Customer Query"
    FILE_PATH = "Config\\Data\\sample_attachment.pdf"