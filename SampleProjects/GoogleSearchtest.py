import HtmlTestRunner
from selenium import webdriver

#1. To make a Unit Test We should 1st IMPORT Python BuildIn Unit Test Module
import unittest


# ------------------------------------------

# ----Sample Project with Selenium Python---

# 1. Create a Test For Google Search

# 2. Add Implicit wait 10 Sec

# 3 Maximize Window

# 4 Create Unit Test

# 5 Add HTML REPORTING Library

# 6 Run From Command Line

# -------------------------------------------


#2. Then we'll create Class
class GoogleSearch(unittest.TestCase):

    # Creating Method To Instantiate our Driver
    # & it will run before every Test
    @classmethod
    def setUpClass(cls):

        chromePath = "/home/elyor/Selenium/chromedriver"

        geckoPath = "/home/elyor/Selenium/geckodriver"


        cls.driver = webdriver.Chrome(executable_path=chromePath)

        # 2. ---IMPLICIT WAIT--> Applicable for all the Element of the page & only 1 Time we'll Specify this code at the beggining of the Code
        cls.driver.implicitly_wait(10)

        # 3. Maximize Window
        cls.driver.maximize_window()




    #Now I'll Create test Method & NOTE: it should START with "test" word
    def test_search_automationStepByStep(self):

        URL = "https://www.google.com"

        # Launch the URL
        self.driver.get(URL)

        # Identifing Search Box element
        googleSearchBox = self.driver.find_element_by_xpath("//input[@name='q']")

        googleSearchBox.send_keys("Test Automation Expert")

        # Identifing Google Search Button

        googleSearchButton = self.driver.find_element_by_xpath("//input[@name='btnK']")

        googleSearchButton.click()




    def test_search_myName(self):

        URL = "https://www.google.com"

        # Launch the URL
        self.driver.get(URL)

        # Identifing Search Box element
        googleSearchBox = self.driver.find_element_by_xpath("//input[@name='q']")

        googleSearchBox.send_keys("My Name")

        # Identifing Google Search Button

        googleSearchButton = self.driver.find_element_by_xpath("//input[@name='btnK']")

        googleSearchButton.click()


    @classmethod
    def tearDownClass(cls):


        cls.driver.close()

        cls.driver.quit()

        print("Test Completed")



if __name__ == '__main__':

    ReportPath = "/home/elyor/PycharmProjects/Selenium/REPORTS"

    unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output=ReportPath))



