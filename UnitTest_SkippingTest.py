import unittest


class Apptesting(unittest.TestCase):

    #1 Here we'll Skip "test_search" Method
    @unittest.SkipTest # this is called DECORATOR
    def test_search(self):

        print("This is search Test")


    #2 Here we'll Skip the test again
    @unittest.skip("I am Skipping current test case because it has some Uncompleted Steps")
    def test_advancedSearch(self):

        print("This is advanced Search Method")




    #3 Here we'll Skip the test case based on the Condition
    @unittest.skipIf(1==1, "One is Equal to One")
    def test_prepaidRecharge(self):

        print("This is pre paid Recharge Method")


    #4
    def test_postpaidRecharge(self):

        print("This is post paid Recharge Method")


    #5
    def test_loginGmail(self):

        print("This is GMAIL Login Method")

    #6
    def test_loginTWITTER(self):

        print("This is TWITTER Login Method")



if __name__=="__main__":

    unittest.main()










