import unittest

#----------IMPORTING CLASSES FROM PACKAGE1 & Package2

from Package1.TC_LoginTest import LoginTest

from Package1.TC_SignUpTest import SignUpTest

from Package2.TC_PaymentTest import PaymentTest

from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

#----------------------------------------------



class PaymentReturnsTest(unittest.TestCase):


    def paymentReturnByBank(self):

        print("This is Payment Return By Bank Test")

        self.assertTrue(True)





if __name__=="__main__":

    unittest.main()
