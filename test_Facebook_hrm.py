from selenium import webdriver

import pytest

import time

class TestFacebookHRM():


    @pytest.fixture() # what will do? - Below 'setup'Method we'll execute before & after every method
    def setup(self):

        #1 Below Launching Browser & Maximize Execute Before Every Method with the help "@pytest.fixture()"

        chromePath = "/home/elyor/Selenium/chromedriver"

        self.driver = webdriver.Chrome(executable_path=chromePath)

        self.driver.maximize_window()

        #2 Below Closing Browser Execute Before Every Method with the help "@pytest.fixture()"

        yield

        self.driver.close()
        self.driver.quit()



    def test_homePageTitle(self,setup):

        URL = "https://www.facebook.com/"

        self.driver.get(URL)

        assert self.driver.title == "Facebook"

        time.sleep(2)





    def test_login(self, setup):


        URL = "https://www.facebook.com/"

        self.driver.get(URL)



        # 1 Set Username
        email = self.driver.find_element_by_xpath("//input[@id='email']")

        print(email)

        email.send_keys("esoliev1661@gmail.com")

        # 2 Set Password
        password = self.driver.find_element_by_xpath("//input[@id='pass']")

        password.send_keys("Aisha2018$")

        # 3 LoginButton

        loginButton = self.driver.find_element_by_xpath("//input[@value='Log In']")

        loginButton.click()

        time.sleep(2)

        # 4 Verifying Login is Successful or Not

        # self.assertEqual("Facebook", self.driver.title, 'Login was Not Successful')

        assert self.driver.title == "Facebook"




#---NOTE - To Execute the test we use " pytest -v -s PYTEST/testCase_facebookLogIn_hrm.py
# in Terminal ----------


#-------HOW TO GENERATE "HTML REPORT" ? ---1st we should install "pytest-html"

# & " pytest -v -s --html=report.html PYTEST/testCase_facebookLogIn_hrm.py "





