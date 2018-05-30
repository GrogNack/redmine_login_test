from selenium.common.exceptions import *
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
from page.login_page import LoginPage


class Application(object):

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.wait = WebDriverWait(driver, 10)

    def go_to_home_page(self):
        self.driver.get("https://task.htc-cs.com/login?back_url=http%3A%2F%2Ftask.htc-cs.com%2F")

    def login(self, user):
        lp = self.login_page
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        lp.submit_bitton.click()