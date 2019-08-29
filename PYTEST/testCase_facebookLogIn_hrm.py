from selenium import webdriver

#To work with the Unit Test we'll Import "unittest"
import unittest

#To Generate the HTML Test Report we'll import "HtmlTestRunner"
import HtmlTestRunner

import time


#---------PYTHON UNITTEST HTML TESTRUNNER REPORTS-------



#---------DECLARING VARIABLES -------------

ExcelPath = "//home//elyor//Selenium//EXCEL.xlsx"

chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.facebook.com/"

#-----------TEST CASE------------

#Step 1: Launch Browser

#Step 2: Verify Home Page Title

#Step 3: Verify Login

#Step 4: Close Browser


#-------------------------------------

#We can create a FUNCTION in a PYTHON without Having the Class
#We can't create the METHOD in a PYTHON without Class
#That's a DIFFERENCE between FUNCTION & METHOD in PYTHON

#So If I don't have any Class & I can Create directly FUNCTION
#If Insert the same FUNCTION inside the Class that's call METHOD

#--------------------------------------


#Here we are Extending our FacebookHRMTest Class with "unittest.TestCase"
class FacebookHRMTest(unittest.TestCase):


    #Here Inside the Class we'll create Multiple Methods

    #Step 1 Launch the Browser

    @classmethod
    def setUpClass(cls): #predefined class & it will execute only one time before actual method we'll start

        cls.driver = webdriver.Chrome(executable_path=chromePath)

        # ---MAXIMIZE THE WINDOW ---
        cls.driver.maximize_window()

        # ---DECLARE IMPLICIT WAIT FOR ALL OBJECT---
        cls.driver.implicitly_wait(30)




    #Step 2 Verify Home Page Title

    def test_homePageTitle(self):

        self.driver.get(URL)

        #Verifying TITLE with "assert" Method
        self.assertEqual("Facebook - Log In or Sign Up", self.driver.title, 'WebPage Title is not Matching')





    # Step 3: Verify Login

    def test_loginFacebook(self):

        #1 Set Username
        email = self.driver.find_element_by_xpath("//input[@id='email']")

        print(email)

        email.send_keys("esoliev1661@gmail.com")



        #2 Set Password
        password = self.driver.find_element_by_xpath("//input[@id='pass']")

        password.send_keys("Aisha2018$")



        #3 LoginButton

        loginButton = self.driver.find_element_by_xpath("//input[@value='Log In']")

        loginButton.click()

        time.sleep(2)

        #4 Verifying Login is Successful or Not

        self.assertEqual("Facebook", self.driver.title, 'Login was Not Successful')



    # Step 4: Log Out From Application
    # def test_logOutFacebook(self):
    #     # 1.Click Log Out Drop down
    #     logOutDropDown = self.driver.find_element_by_xpath("//div[@id='userNavigationLabel']")
    #
    #     logOutDropDown.click()
    #
    #     # 2. Select Log Out From List
    #     logOutButton = self.driver.find_element_by_xpath("//span[contains(text(),'Log Out')]")
    #
    #     logOutButton.click()




    # Step 5: Close the Application

    @classmethod
    def tearDown(cls):

        time.sleep(5)

        #1 Close all the browser
        #cls.driver.quit()

        print("Test completed")


#---Finally To EXECUTE  THE TEST we should Write Below Method

if __name__=='__main':

    #To Generate the we'll use
    # "testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\REPORTS'))" inside the parenthesis

    #To run the Test we'll use TERMINAL & "pytest -v -s PYTEST/testCase_facebookLogIn_hrm.py" command

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='//home//elyor//PycharmProjects//Selenium//REPORTS//')) # (..//REPORTS) - means current project directory)

























