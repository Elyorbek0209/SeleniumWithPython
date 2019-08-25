import unittest

from selenium import webdriver

#--------------ASSERTIONS -------------


# - Assertion is nothing but the check point or you can say it is verification
# for the TC to evaluate some item on the execution

# - If we don't provide any asertion inside a TC then there is no way
# to know whether a test case is Failed or Not.

# - Assertion helps in Report Generation, based on the Assertions the Test
# Execution Report will be generated

# - There are a few assertion which will accept all the value &
# few assertions will Accept Only Numeric Values



# - assertEqual

# - assertNotEqual

# - assertTrue

# - assertFalse

#--------------------------------------


class Test(unittest.TestCase):


    def testName(self):

        chromePath = "/home/elyor/Selenium/chromedriver"

        URL = "https://www.google.com/"


        driver = webdriver.Chrome(executable_path=chromePath)

        #Launching Browser
        driver.get(URL)


        #Get Title
        Title = driver.title


        #assertEqual
        #self.assertEqual("Google", Title, "WebPage Title is Not the Same as Expected")


        #assertNotEqual
        self.assertNotEqual("Google123", Title, "WebPage Title is Not the same as Expected")

        driver.quit()










