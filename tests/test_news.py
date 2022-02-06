from pages.login_page import LoginPage
from tests.conftest import driver
from pages.news_page import NewsPage
from tests.test_base import TestBase
import pytest

class TestNews(TestBase):
  
  def test_images_are_displayed(self, driver):
    login_page = LoginPage(driver)
    news_page = NewsPage(driver)
    assert login_page.is_opened()
    # Proper login and password
    assert login_page.proceed_with_login(TestBase.data()['existing_login'])
    assert login_page.proceed_with_password(TestBase.data()['existing_password'])
    assert login_page.login()
    assert news_page.is_opened()
    assert news_page.check_if_many_images()
  

  def test_offline_mode(self, driver):
    login_page = LoginPage(driver)
    news_page = NewsPage(driver)
    assert login_page.is_opened()
    # Disconnect from the Internet
    driver.set_network_connection(0)
    # Proper login and password
    assert login_page.proceed_with_login(TestBase.data()['existing_login'])
    assert login_page.proceed_with_password(TestBase.data()['existing_password'])
    assert login_page.login()
    # Check if error message is displayed
    assert news_page.is_opened(error_message=True)
  

  def test_redirection(self, driver):
    login_page = LoginPage(driver)
    news_page = NewsPage(driver)
    assert login_page.is_opened()
    # Proper login and password
    assert login_page.proceed_with_login(TestBase.data()['existing_login'])
    assert login_page.proceed_with_password(TestBase.data()['existing_password'])
    assert login_page.login()
    assert news_page.is_opened()
    assert news_page.click_image()
    assert news_page.check_redirection()
