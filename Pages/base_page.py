from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,TimeoutException, WebDriverException, ElementClickInterceptedException, ElementNotInteractableException, ElementNotSelectableException, ScreenshotException, MoveTargetOutOfBoundsException
import time
import os
"""This class is the parent of all the pages"""
"""It contains all the generic methods and utilities for all the pages"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
    
    def do_find_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element
        except KeyError:
            raise Exception("do_find_element: unexpected kind of locator {}".format(by_locator[0]))
        except TimeoutException:
            raise Exception("do_find_element: unable to find element {}".format(by_locator))
        except WebDriverException as exc:
            raise Exception("do_find_element: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("do_find_element: {}".format(str(exc)))
    
    def do_find_elements(self, kind, locator):
        try:
            elements = self.driver.find_elements(kind, locator)
            return elements
        except KeyError:
            raise Exception("do_find_elements: unexpected kind of locator {}".format(kind))
        except NoSuchElementException:
            raise Exception("do_find_elements: unable to find element (kind={}, locator={})".format(kind, locator))
        except TimeoutException:
            raise Exception("do_find_elements: unable to find element (kind={}, locator={})".format(kind, locator))
        except WebDriverException as exc:
            raise Exception("do_find_elements: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("do_find_elements: {}".format(str(exc)))
    
    def do_click(self, kind, locator):
        by_locator = (kind, locator)
        try:
            self.do_find_element(by_locator).click()
        except ElementClickInterceptedException:
            raise Exception("do_click: unable to interact_with / click the element".format(locator))
        except WebDriverException as exc:
            raise Exception("do_click: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("do_click: {}".format(str(exc)))
    
    # def do_clear_input(self, kind, locator):
    #     by_locator = (kind, locator)
    #     self.do_find_element(by_locator).clear()
    
    def do_send_keys(self, kind, locator, text, press_enter=None, clear="Yes"):
        by_locator = (kind, locator)
        try:
            element = self.do_find_element(by_locator)
            if clear:
                element.clear()
            if press_enter:
                text = text + Keys.ENTER
            element.send_keys(text)
        except ElementNotInteractableException:
            raise Exception("do_send_keys: unable to type value into the input element {}".format(locator))
        except WebDriverException as exc:
            raise Exception("do_send_keys: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("do_send_keys: {}".format(str(exc)))
    
    def get_element_text(self, kind, locator):
        by_locator = (kind, locator)
        try:
            element = self.do_find_element(by_locator)
            return element.text
        except ElementNotInteractableException:
            raise Exception("get_element_text: unbale to get value from the element {}".format(locator))
        except WebDriverException as exc:
            raise Exception("get_element_text: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("get_element_text: {}".format(str(exc)))
    
    def is_enabled(self, kind, locator):
        by_locator = (kind, locator)
        try:
            element = self.do_find_element(by_locator)
            return bool(element)
        except WebDriverException as exc:
            raise Exception("get_element_text: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("get_element_text: {}".format(str(exc)))
    
    def do_select(self, kind, locator, value):
        by_locator = (kind, locator)
        try:
            select_class_obj = Select(self.do_find_element(by_locator))
            select_class_obj.select_by_value(value)
        except ElementNotSelectableException:
            raise Exception("do_select: cannot select option {}".format(value))
        except WebDriverException as exc:
            raise Exception("do_select: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("do_select: {}".format(str(exc)))
    
    def do_double_click(self, kind, locator):
        by_locator = (kind, locator)
        try:
            element = self.do_find_element(by_locator)
            self.action.double_click(element)
        except ElementClickInterceptedException:
            raise Exception("do_double_click: unable to interact_with / click the element {}".format(locator))
        except WebDriverException as exc:
            raise Exception("do_double_click: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("do_double_click: {}".format(str(exc)))
    
    def do_right_click(self, kind, locator):
        by_locator = (kind, locator)
        try:
            element = self.do_find_element(by_locator)
            self.action.context_click(element)
        except ElementClickInterceptedException:
            raise Exception("do_double_click: unable to interact_with / click the element {}".format(locator))
        except WebDriverException as exc:
            raise Exception("do_double_click: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("do_double_click: {}".format(str(exc)))
    
    def do_refresh(self):
        try:
            self.driver.refresh()
        except WebDriverException as exc:
            raise Exception("do_refresh: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("do_refresh: {}".format(str(exc)))
    
    def take_screenshot(self, test_name):
        try:
            test_screenshots_folder_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'TestScreenshots'))
            print(test_screenshots_folder_path)
            test_screenshot_path = os.path.join(test_screenshots_folder_path, test_name + '.png')
            print(test_screenshot_path)
            self.driver.save_screenshot(test_screenshot_path)
        except ScreenshotException:
            raise Exception("take_screenshot: unable to capture screenshot")
        except WebDriverException as exc:
            raise Exception("take_screenshot: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("take_screenshot: {}".format(str(exc)))
    
    def do_mouse_hover(self, kind, locator):
        by_locator = (kind, locator)
        try:
            element = self.do_find_element(by_locator)
            self.action.move_to_element(element).perform()
        except MoveTargetOutOfBoundsException:
            raise Exception("do_mouse_hover: cannot move to element{}".format(locator))
        except WebDriverException as exc:
            raise Exception("do_mouse_hover: {}".format(exc.msg))
        except Exception as exc:
            raise Exception("do_mouse_hover: {}".format(str(exc)))
    
    def do_check_element_not_exists(self, kind, locator):
        try:
            elements_list = self.do_find_elements(kind, locator)
            print(elements_list)
            assert len(elements_list) == 0
        except AssertionError:
            raise Exception("do_check_element_not_exists: element {} not found".format(locator))
        