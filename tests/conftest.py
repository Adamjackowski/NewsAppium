import inspect
import json
import os
import smtplib
import sys
from datetime import datetime
import pytest
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webbrowser import Chrome
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from tests.test_base import TestBase

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

@pytest.fixture(scope='session')
def driver():
    desire_capability = {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': 'R58N35ZGQ7E',
    'app': parentdir + '/app-debug.apk',
    'noReset': False,
    'fullReset': True,
    'clearSystemFiles': True,
    'appPackage': 'com.test.news',
    'appActivity': 'com.test.news.features.login.presentation.LoginActivity'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_capability)
    driver.set_network_connection(6)
    yield driver
    driver.quit()

'''
Method for taking the screenshot and saving in the /screenshots directory. It is called in browser fixture
'''
def take_screenshot(driver, test_name):
    screenshots_dir = parentdir + '\screenshots'
    now = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    screenshot_file_path = '{}\{}_{}.png'.format(screenshots_dir, test_name, now)
    driver.save_screenshot(screenshot_file_path)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


def screenshot(driver, request):
    failed_before = request.session.testsfailed
    yield None
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(driver, test_name)

@pytest.fixture()
def users():
    def _users(user):
        return user
    return _users


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        driver = item.funcargs['driver']
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            if pytest_html != None:
                extra.append(pytest_html.extras.image("file:///" + take_screenshot(driver, item.name)))
            else:
                take_screenshot(driver, item.name)
        report.extra = extra