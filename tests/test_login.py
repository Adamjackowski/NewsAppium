from pages.main_page import MainPage
from pages.login_page import LoginPage
from tests.conftest import driver
from pages.news_page import NewsPage
from tests.test_base import TestBase
import pytest

class TestLogin(TestBase):
  # User opens the android app first time (when not logged in yet)
  def test_login_page_opened(self, driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    assert login_page.is_opened()

  # User login failed
  def test_login_fail(self, driver):
    login_page = LoginPage(driver)
    assert login_page.is_opened()
    # Wrong login and password
    assert login_page.proceed_with_login(TestBase.data()['not_existing_login'])
    assert login_page.proceed_with_password(TestBase.data()['not_existing_password'])
    assert login_page.login()
    # Can't check markers using Appium
    assert login_page.is_error_marker_displayed("login")
    assert not login_page.is_error_marker_displayed("password")

    # Proper login and wrong password
    assert login_page.proceed_with_login(TestBase.data()['existing_login'])
    assert login_page.proceed_with_password(TestBase.data()['not_existing_password'])
    assert login_page.login()
    assert not login_page.is_error_marker_displayed("login")
    assert login_page.is_error_marker_displayed("password")
    
    # Check if user is still on login page 
    assert login_page.is_opened()

  def test_login_passed(self, driver):
    login_page = LoginPage(driver)
    news_page = NewsPage(driver)
    assert login_page.is_opened()
    # Proper login and password
    assert login_page.proceed_with_login(TestBase.data()['existing_login'])
    assert login_page.proceed_with_password(TestBase.data()['existing_password'])
    assert login_page.login()
    assert news_page.is_opened()
  

  def test_reopen_app(self, driver):
    login_page = LoginPage(driver)
    news_page = NewsPage(driver)
    assert login_page.is_opened()
    # Proper login and password
    assert login_page.proceed_with_login(TestBase.data()['existing_login'])
    assert login_page.proceed_with_password(TestBase.data()['existing_password'])
    assert login_page.login()
    assert news_page.is_opened()
    # Close the app
    assert news_page.close_app()
    # Reopen the app
    assert news_page.open_app()
    assert news_page.is_opened()



    