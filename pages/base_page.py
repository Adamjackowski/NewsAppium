from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import *
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    '''
    Method which convert the locator to web element
    '''
    def element(self, *locator):
        WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    '''
    Method which convert the locator to web elements list
    '''
    def elements(self, *locator):
        return self.driver.find_elements(*locator)
    
    '''
    Method which input the text to text fields
    '''
    def type(self, element, value, text_hidden=False):
        # ADD HERE WAIT UNTIL THE BUTTON IS CLIKACBLE
       # clickable = False
        element.clear()
        element.send_keys(value)
        #element.click()
        #self.driver.keyevent(66)
        self.driver.hide_keyboard()
        #clickable = self.check_input_value(element, value, text_hidden)   
        return True
    
    '''
    Method clicks on the element
    '''
    def click(self, element):
        try:
            element.click()
            return True
        except:
            return False
    
    def scroll_up(self):
        TouchAction(self.driver).long_press(x=200, y=300).move_to(x=200, y=900).release().perform()


    def scroll_down(self):
        TouchAction(self.driver).long_press(x=200, y=900).move_to(x=200, y=300).release().perform()


    def scroll_to_element(self, locator, direction):
        if direction == "DOWN":
            self.scroll_down()
        elif direction == "UP":
            self.scroll_up()
        try:
            self.element(*locator)
            return True
        except:
            return False

    '''
    Method which gets the placeholder value of text field
    '''
    def get_input_value(self, element):
        if element is not None:
            while element.get_attribute("value") == "":
               continue
            return element.get_attribute("value")
    
    '''
    Method which gets the placeholder value of text field if empty
    '''
    def get_input_empty_value(self, element):
        if element is not None:
            while element.get_attribute("value") != "":
               continue
            return element.get_attribute("value")
    '''
    Method which checks the iput value is displayed correclty
    '''
    def check_input_value(self, element = None, expected_value=None, text_hidden=False):
        is_correct = False
        if text_hidden is True:
            is_correct = bool(len(expected_value) == len(element.text))
        else:
            is_correct =  bool(expected_value == element.text)
        return is_correct

    
    '''
    Method which check if element is displayed or not
    '''
    def is_element_displayed(self, *locator):
        try: 
            if self.driver.find_element(*locator).is_displayed():
                return True
        except:
            return False
    
    def is_each_element_displayed(self, element):
        try: 
            if element.is_displayed():
                return True
        except:
            return False
    
    def close_app(self):
        self.driver.close_app()
        return True
    
    def open_app(self):
        self.driver.start_activity("com.test.news", "com.test.news.features.login.presentation.LoginActivity"); 
        return True
    
    