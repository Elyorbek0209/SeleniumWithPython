import HtmlTestRunner
from selenium import webdriver
import time

import sys

import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


from SampleProjects.POM_Project.Pages.loginPage import LoginPage

from SampleProjects.POM_Project.Pages.homePage import HomePage



#1. To make a Unit Test We should 1st IMPORT Python BuildIn Unit Test Module
import unittest



# ------------------------------------------

# ----POM | Unit Test | HTML Reports---

# 1. Create a Simple Login

# 2. Implement Unit Testing

# 3. Implement POM

# 4. Separate Test Scripts And Objects

# 5. Create a Separate Class for Locators

# 6. Run From Command Line

# 7. Add HTML Reports

# -------------------------------------------

#2. Then we'll create Class
class LoginTest(unittest.TestCase):

    # Creating Method To Instantiate our Driver
    # & it will run before every Test
    @classmethod
    def setUpClass(cls):

        #CHROME PATH
        chromePath = "/home/elyor/Selenium/chromedriver"

        #Create WebDriver Object
        cls.driver = webdriver.Chrome(executable_path=chromePath)


        # 2. ---IMPLICIT WAIT--> Applicable for all the Element of the page & only 1 Time we'll Specify this code at the beggining of the Code
        cls.driver.implicitly_wait(10)


        # 3. Maximize Window
        cls.driver.maximize_window()







    # Now I'll Create test Method & NOTE: it should START with "test" word
    def test_login_valid(self):

        URL = "https://opensource-demo.orangehrmlive.com/"

        driver = self.driver


        # Launch the URL
        driver.get(URL)

        #Create LoginPage Object
        login = LoginPage(driver)


        #1
        login.enter_username("Admin")

        #2
        login.enter_password("admin123")

        #3
        login.click_login_button()




        #create HomePage Object
        homepage = HomePage(driver)


        #1
        homepage.click_WelcomeLink()

        #2
        homepage.click_LogOut()








    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()

        print("Test Completed")




if __name__ == '__main__':
    ReportPath = '/home/elyor/PycharmProjects/Selenium/REPORTS'

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=ReportPath))

time.sleep(3)

























