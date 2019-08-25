import unittest

from selenium import webdriver

#----------PYTHON Unit Test Framework------------

# - In Automation Testing, organizing your code is very important

# & client expects us to write automation scripts according to the

# manual test cases.


# - We can get good reporting structure if we can exactly map our

# automation code with manual test cases


# - In Python we can use UnitTest testing framework to organize our automation code

# & to extract Reports


# - To use the methods present in the UnitTest framework, we have to extend

# the TestCase class present in the UnitTest module




# class Test(unittest.TestCase):
#
#     def test_firstTest(self):
#
#         print("This is my first Unit Test Case")
#
# #Here we'll (__name__) Default Variable which is representing Current Module name
# if __name__=="__main__":
#
#     unittest.main()


#---------DECLARING VARIABLES -------------


chromePath = "/home/elyor/Selenium/chromedriver"

geckoPath = "/home/elyor/Selenium/geckodriver"

URL = "https://www.google.com"

URL2 = "https://bing.com"

#---------END OF THE DECLARING VARIABLES -------------



#----------- RUNNING Multiple Test in Class ----------

class SearchEngineTest(unittest.TestCase):



    def test_Google(self):

        self.driver = webdriver.Chrome(executable_path=chromePath)

        self.driver.get(URL)

        print("Title of the page is :" + self.driver.title)

        self.driver.close()



    def test_Bing(self):

        self.driver = webdriver.Chrome(executable_path=chromePath)

        self.driver.get(URL2)

        print("Title of the page is :" + self.driver.title)

        self.driver.close()



#Start Running if __name__equal to __main__
if __name__ == "__main__":

    unittest.main()














