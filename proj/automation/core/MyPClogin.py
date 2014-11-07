'''
Created on Nov 7, 2014

@author: avasilyev2
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from _hashlib import new


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        pass


    def tearDown(self):
        self.driver.quit()
        pass


    def testName(self):
        driver = self.driver
        wait = self.wait
        driver.get("http://10.10.32.66/loadtest")
       # elem = wait.until(driver.find_element_by_id("ctl00_PageContent_txtUserName"))
        assert "Performance center" in driver.title
        #elem.send_keys("admin")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()