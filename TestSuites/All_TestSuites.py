import unittest

#----------IMPORTING CLASSES FROM PACKAGE1 & Package2

from Package1.TC_LoginTest import LoginTest

from Package1.TC_SignUpTest import SignUpTest

from Package2.TC_PaymentTest import PaymentTest

from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

#----------------------------------------------



# Now Get all tests from LoginTest, SignUpTest, PaymentTest & PaymentReturnTest

#1 Here we'll use "TestLoader().loadTestsFromTestCase()" Method

TC1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

TC2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)

TC3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

TC4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)



#2 Here Creating Test Suites with the help of ".TestSuite()" Method

#Sanity Test Suite
sanityTestSuite = unittest.TestSuite([TC1, TC2])

#Functional Test Suite
functionalTestSuite = unittest.TestSuite([TC3, TC4])


#3 Here we use ".TextTestRunner()" Method & RUN "sanityTestSuite" above
unittest.TextTestRunner().run(functionalTestSuite)











