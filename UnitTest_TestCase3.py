import unittest


#----------setUpModule will be execute before the Class & Method ---

def setUpModule():

    print("Set Up Module")


def tearDownModule():
    print("Tear Down Module")
#-----------------------------------



class AppTesting(unittest.TestCase):


    # "setUp(self)" Method will execute before every single Method
    @classmethod
    def setUp(self):

        print("This is Login ")

    @classmethod
    def tearDown(self):

        print("This is Logout")



    @classmethod
    def setUpClass(cls):

        print("Launch Application")


    @classmethod
    def tearDownClass(cls):

        print("Close Application")



    #--------------------------------------------------------------


    def test_search(self):

        print("This is search test")


    def test_advancedsearch(self):

        print("This is Advanced search test")


    def test_prepaidRecharge(self):

        print("This is prepaid Recharge test")


    def test_postpaidRecharge(self):

        print("This is post paidRecharge test")



if __name__ == "__main__":

    unittest.main()






















