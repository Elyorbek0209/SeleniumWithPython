import unittest

class PaymentTest(unittest.TestCase):


    def test_paymentInDollar(self):

        print("This is Payment in Dollar test")

        self.assertTrue(True)



    def test_paymentInRubl(self):

        print("This is Payment in Rubl test")

        self.assertTrue(True)



if __name__ == "__main__":

    unittest.main()


