# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from fixture import app
import unittest, time, re
from model.user_data import User



def login(driver, user):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user.username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(user.password)
    driver.find_element_by_id("login-submit").click()

def test_login(app):
    app.driver.get("https://task.htc-cs.com/login?back_url=http%3A%2F%2Ftask.htc-cs.com%2F")
    login(app.driver, User.Admin())


# def test_login(driver):
#     driver.get("https://task.htc-cs.com/login?back_url=http%3A%2F%2Ftask.htc-cs.com%2F")
#     driver.find_element_by_id("username").clear()
#     driver.find_element_by_id("username").send_keys("mkazantsev")
#     driver.find_element_by_id("password").clear()
#     driver.find_element_by_id("password").send_keys("119074")
#     driver.find_element_by_id("login-submit").click()



# class Untitled(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "https://task.htc-cs.com/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
#
#     def test_untitled(self):
#         driver = self.driver
#         driver.get(self.base_url + "/login?back_url=http%3A%2F%2Ftask.htc-cs.com%2F")
#         driver.find_element_by_id("username").clear()
#         driver.find_element_by_id("username").send_keys("mkazantsev")
#         driver.find_element_by_id("password").clear()
#         driver.find_element_by_id("password").send_keys("119074")
#         driver.find_element_by_id("login-submit").click()
#
#     def is_element_present(self, how, what):
#         try:
#             self.driver.find_element(by=how, value=what)
#         except NoSuchElementException as e:
#             return False
#         return True
#
#     def is_alert_present(self):
#         try:
#             self.driver.switch_to_alert()
#         except NoAlertPresentException as e:
#             return False
#         return True
#
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally:
#             self.accept_next_alert = True
#
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)
#
#
# if __name__ == "__main__":
#     unittest.main()
