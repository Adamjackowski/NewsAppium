from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LoginPageLocators, LoginPageLocators

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    '''
    Method check is page open
    '''
    def is_opened(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            LoginPageLocators.LOGIN_INPUT))
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            LoginPageLocators.PASSWORD_INPUT))
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            LoginPageLocators.LOGIN_BUTTON))
        return True

    '''
    Method for login in.
    '''
    def proceed_with_login(self, login): 
        return self.type(self.element(*LoginPageLocators.LOGIN_INPUT), login)
    
    def proceed_with_password(self, password):
        return self.type(self.element(*LoginPageLocators.PASSWORD_INPUT), password)
    

    def login(self):
        return  self.click(self.element(*LoginPageLocators.LOGIN_BUTTON))
    
    def is_error_marker_displayed(self, marker_type):
        marker_locator = LoginPageLocators.WRONG_LOGIN_POPUP if marker_type == "login" else LoginPageLocators.WRONG_PASSWORD_POPUP 
        field_to_reclick = LoginPageLocators.LOGIN_INPUT if marker_type == "login" else LoginPageLocators.PASSWORD_INPUT
        self.click(self.element(*field_to_reclick))
        
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            marker_locator))
        return self.is_element_displayed(*marker_locator)
    


    