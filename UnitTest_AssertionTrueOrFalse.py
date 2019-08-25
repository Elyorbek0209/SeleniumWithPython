import unittest

from selenium import webdriver

#--------------ASSERTIONS -------------

# - assertTrue

# - assertFalse

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


        #3 assertTrue Method
        #self.assertTrue(Title=="Google") # True

        # 4 assertFalse Method
        self.assertFalse(Title=="Google12345") # True



if __name__=="__main__":

    unittest.main()






