import pytest


#_------------PYTEST FRAMEWORK-------------

# The Pytest Framework makes it easy to write
# Small Tests Implemented on Top of our UnitTest



#----NOTE ---> "PYTEST" Method should always with "test" word added ------

def testMethod1():

    print("This is Test Method 1")


def testMethod2():
    print("This is Test Method 2")


def testMethod3():

    print("This is Test Method 3")


def testMethod4():
    print("This is Test Method 4")

#------------------------------------------------------------------

#---------So to run this above "PYTEST" Method we use Terminal----

# How to open Terminal? - Got to "View" -> "Tool Windows" & Terminal

# To run the test we use "pytest" or "pytest -v -s PYTEST/test_PyTest_Fixtures.py" command in Terminal

# If we have multiple test in our package, we should specify test name
# like "pytest -v -s test_TestDemo.py" otherwise it will executed the test of the test cases

#-------------------------------------------------------------------


