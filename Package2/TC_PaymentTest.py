import unittest

class PaymentTest(unittest.TestCase):

    def paymentInDollar(self):

        print("This is Payment in Dollar test")

        self.assertTrue(True)



    def paymentInRubl(self):

        print("This is Payment in Rubl test")

        self.assertTrue(True)



    def paymentInSum(self):

        print("This is Payment in Sum test")

        self.assertTrue(True)

    print("Hello Money")


if __name__=="__main__":

    unittest.main()


