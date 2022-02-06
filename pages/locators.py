from selenium.webdriver.common.by import By

class NewsPageLocators(object):
  IMAGES = (By.ID, "recyclerViewNews")
  IMAGE = (By.ID, "imageView")
  ERROR_MESSAGE = (By.ID, "textViewError")

class LoginPageLocators(object):
   LOGO = (By.ID, "textViewLogo")
   LOGIN_BUTTON = (By.ID, "buttonLogin")
   LOGIN_INPUT = (By.ID, "editTextUserName")
   PASSWORD_INPUT = (By.ID, "editTextPassword")
   WRONG_LOGIN_POPUP = (By.XPATH, "//*[@text='Wrong user name']")
   WRONG_PASSWORD_POPUP = (By.XPATH, "//*[@text='Wrong password']")
  
