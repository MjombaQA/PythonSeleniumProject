import unittest
import HtmlTestRunner
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod

    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="..//drivers//chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)




    def  test_search(self):
        self.driver.get("https://google.co.uk")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print (x)
        self.assertEqual(x,"Automation step by step - Google Search")


    def  test_search_2(self):
        self.driver.get("https://google.co.uk")
        self.driver.find_element_by_name("q").send_keys("Raghav Pal")
        self.driver.find_element_by_name("btnK").click()
        y = self.driver.title
        print (y)
        self.assertEqual(y,"Raghav Pal - Google Search")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Tina/PycharmProjects/Selenium/Demo/reports'),verbosity=2)

