import time
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, \
    NoSuchWindowException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.CustomLogger import custom_logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException)


class Action_page:
    log = custom_logger()

    def __init__(self, driver):
        self.driver = driver

    ignore_list = [ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)

    def click(self, locatorValue, locatorType):
        time.sleep(10)
        if str(locatorType) == "XPATH":
            self.driver.find_element(By.XPATH, locatorValue).click()
            self.log.info("Clicked on the element ::  " + locatorValue)
        elif str(locatorType) == "NAME":
            self.driver.find_element(By.NAME, locatorValue).click()
            self.log.info("Clicked on the element ::  " + locatorValue)
        elif str(locatorType) == "ID":
            self.driver.find_element(By.ID, locatorValue).click()
            self.log.info("Clicked on the element ::  " + locatorValue)
        elif str(locatorType) == "CLASS_NAME":
            self.driver.find_element(By.CLASS_NAME, locatorValue)

    def send_keys(self, locatorValue, locatorType, value):
        if str(locatorType) == "XPATH":
            self.driver.find_element(By.XPATH, locatorValue).send_keys(value)
            self.log.info("sent key as  ::  " + value)
        elif str(locatorType) == "NAME":
            self.driver.find_element(By.NAME, locatorValue).send_keys(value)
            self.log.info("sent key as  ::  " + value)
        elif str(locatorType) == "ID":
            self.driver.find_element(By.ID, locatorValue).send_keys(value)
            self.log.info("sent key as  ::  " + value)

    def get_text(self, locatorValue, locatorType, value):
        if str(locatorType) == "XPATH":
            element = self.driver.find_element(By.XPATH, locatorValue).get_attribute(value)
            self.log.info("got attribute value as  ::  " + str(element))
            return element
        elif str(locatorType) == "NAME":
            element = self.driver.find_element(By.NAME, locatorValue).get_attribute(value)
            self.log.info("got attribute values as ::  " + str(element))
            return element
        elif str(locatorType) == "ID":
            element = self.driver.find_element(By.ID, locatorValue).get_attribute(value)
            self.log.info("got attribute values as ::  " + str(element))
            return element

    def refresh_page(self):
        self.driver.refresh()

    def check_conditions(self, locatorValue, locatorType):
        if str(locatorType) == "XPATH":
            self.driver.find_element(By.XPATH, locatorValue)
        elif str(locatorType) == "ID":
            self.driver.find_element(By.ID, locatorValue)

    def move_to_the_element(self, locatorValue):
        element = self.driver.find_element(By.XPATH, locatorValue)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def scroll_to_view(self, locatorValue):
        element = self.driver.find_element(By.XPATH, locatorValue)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_index(self, locatorValue, locatorType, value):
        if str(locatorType) == "XPATH":
            self.driver.find_element(By.XPATH, str(locatorValue) + "[" + str(value) + "]").click()
            self.log.info("Clicked on the element ::  " + locatorValue)
        elif str(locatorType) == "CLASS_NAME":
            self.driver.find_element(By.CLASS_NAME, str(locatorValue) + "[" + str(value) + "]").click()

    def window_handles(self):
        currentWindow = self.driver.current_window_handle
        childWindows = self.driver.window_handles
        for i in childWindows:
            if i != currentWindow:
                print(i)
                self.driver.switch_to.window(i)

    def close_tab(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
        except (NoSuchWindowException, NoSuchElementException):
            pass

    def move_to_current_tab(self, windowNumber):
        self.driver.switch_to.window(self.driver.window_handles[int(windowNumber)])
