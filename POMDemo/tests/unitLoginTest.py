from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMDemo.pages.homepage import HomePage
from POMDemo.pages.loginpage import LoginPage
import HtmlTestRunner




class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="..//drivers///chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login=LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage=HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__=='__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Tina/PycharmProjects/Selenium\POMDemo/reports"))
