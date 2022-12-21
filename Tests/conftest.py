import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import os
from Config.config import TestData

# pytest_addoption allows users to register a user-defined command line parameter to facilitate users to pass data to pytest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=TestData.BROWSER)

def get_driver(getBrowser, driver_path, driver_log_path):
    # cross browser testing support
    driver=None
    if getBrowser == "firefox":
        # using gecko driver manager to automatically download and install respective compatible gecko driver
        driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager(path=driver_path).install(), log_path=driver_log_path))
    elif getBrowser == "chrome":
        # using chrome driver manager to automatically download and install respective compatible chrome driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(path=driver_path).install(), log_path=driver_log_path))
    elif getBrowser == 'edge':
        # using edge driver manager to automatically download and install respective compatible edge driver
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager(path=driver_path).install(), log_path=driver_log_path))
    return driver

@pytest.fixture(scope='class')
def getBrowser(request):
    # config.getoption gets parameter values from config file
    browser = request.config.getoption("--browser")
    return browser

@pytest.fixture(scope='class')
def agent_driver(request, getBrowser):
    
    # TEST SETUP STEPS
    driver_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'Drivers'))
    print(driver_path)
    driver_log_path = os.path.join(driver_path, 'agent_driver_log')
    print(driver_log_path)
    
    driver = get_driver(getBrowser, driver_path, driver_log_path)
    request.cls.ag_driver = driver
    yield
    # TEST TEARDOWN STEPS
    driver.quit()

@pytest.fixture(scope='class')
def customer_driver(request, getBrowser):
    
    # TEST SETUP STEPS
    driver_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'Drivers'))
    print(driver_path)
    driver_log_path = os.path.join(driver_path, 'customer_driver_log')
    print(driver_log_path)
    
    driver = get_driver(getBrowser, driver_path, driver_log_path)
    request.cls.cust_driver = driver
    yield
    # TEST TEARDOWN STEPS
    driver.quit()