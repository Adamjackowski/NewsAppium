from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import NewsPageLocators

class NewsPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    '''
    Method check is page open
    '''
    def is_opened(self, error_message=False):
        if error_message == True:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            NewsPageLocators.ERROR_MESSAGE))
            return self.is_element_displayed(*NewsPageLocators.ERROR_MESSAGE)
        else:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                NewsPageLocators.IMAGES))
            return self.is_element_displayed(*NewsPageLocators.IMAGES)
    
    def check_redirection(self):
        # Check if chrome is set to current package
        return self.driver.current_package == "com.android.chrome"
    
    def click_image(self):
        WebDriverWait(self.driver, 10).until(lambda condition: len(self.elements(*NewsPageLocators.IMAGES)) >= 1)
        self.click((self.elements(*NewsPageLocators.IMAGES)[0]))
        return True
   
    
    def check_if_many_images(self):
        # Currently at least 1 image is enough to pass
        WebDriverWait(self.driver, 10).until(lambda condition: len(self.elements(*NewsPageLocators.IMAGES)) >= 1)
        return True

    