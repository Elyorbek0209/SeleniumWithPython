import HtmlTestRunner
from selenium import webdriver
import time


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

        # Launch the URL
        self.driver.get(URL)


        # Set Username
        userName = self.driver.find_element_by_xpath("//input[@id='txtUsername']")

        userName.send_keys("Admin")



        # Set password

        password= self.driver.find_element_by_xpath("//input[@id='txtPassword']")

        password.send_keys("admin123")





        # Click LOGIN Button

        login = self.driver.find_element_by_xpath("//input[@id='btnLogin']")

        login.click()

        time.sleep(3)




        # Click Welcome Link

        welcomeLink = self.driver.find_element_by_xpath("//a[@id='welcome']")

        welcomeLink.click()




        #Click LogOut Button

        logOut = self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]")

        logOut.click()









    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()

        print("Test Completed")




if __name__ == '__main__':
    ReportPath = '/home/elyor/PycharmProjects/Selenium/REPORTS'

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=ReportPath))

time.sleep(3)

























