import unittest


#--------------ASSERTIONS -------------

# - assertIn

# - assertNotIn

#--------------------------------------


class Test(unittest.TestCase):


    def testName(self):

        list=["python", "selenium", "java"]

        # assertIn Method
        self.assertIn("python", list) # True

        #assertNotIn Method
        #self.assertNotIn("selenium", list) # Fail



if __name__=="__main__":

    unittest.main()






