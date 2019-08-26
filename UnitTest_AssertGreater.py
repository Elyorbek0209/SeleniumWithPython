import unittest


#--------------ASSERTIONS -------------

# - assertGreater() - verifies if 1st Value > than 2nd Value

# - assertGreaterEqual() - verifies if 1st Value >= than 2nd Value

# - assertLess() - verifies if 1st Value < than 2nd Value

# - assertLessEqual() - verifies if 1st Value =< than 2nd Value



#--------------------------------------


class Test(unittest.TestCase):


    def testName(self):

        #1 assertGreater() Method

        self.assertGreater(100, 10)

        print("First Number is greater than second Number")


        #2 assertGreaterEqual() Method
        self.assertGreaterEqual(100,100)

        print("First Number is greater or equal with second Number")

if __name__=="__main__":

    unittest.main()






