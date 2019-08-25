import unittest

from selenium import webdriver

#--------------ASSERTIONS -------------

# - assertIsNone

# - assertIsNotNone

#--------------------------------------


class Test(unittest.TestCase):


    def testName(self):

        chromePath = "/home/elyor/Selenium/chromedriver"

        URL = "https://www.google.com/"


        driver = webdriver.Chrome(executable_path=chromePath)

        #1 Launching Browser
        driver.get(URL)


        #2 Get Title
        Title = driver.title


        #3 assertIsNone Method
        #self.assertIsNone(Title) # False

        # 4 assertIsNotNone Method
        self.assertIsNotNone(Title) # True



if __name__=="__main__":

    unittest.main()






