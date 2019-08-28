import pytest


#----How to Work with PyTest Fixtures----

# The purpose of the test fixtures is to provide a fixed baseline
# upon which tests can reliably & repeatedly execute


# @pytest.fixture()

# - Execute specific method before every test method


# @pytest.yield_fixture()

# - Execute specific method before & after every test method

#------------------------------------------




#----------- "@pytest.fixture()"-------------

@pytest.fixture()
def setup():

    print("Once Before Every Method")


def testMethod1(setup):

    print("This is Test Method 1")


def testMethod2(setup):
    print("This is Test Method 2")


#---------So to run this above "PYTEST" Method we use Terminal----

# How to open Terminal? - Got to "View" -> "Tool Windows" & Terminal

# To run the test we use "pytest" or "pytest -v -s PYTEST/test_PyTest_Fixtures.py" command in Terminal

# If we have multiple test in our package, we should specify test name
# like "pytest -v -s test_TestDemo.py" otherwise it will executed the test of the test cases

#-------------------------------------------------------------------



#----------- "@pytest.yield_fixture()"-------------


@pytest.yield_fixture()
def setup():

    print("Once Before Every Method")

    yield

    print("Once After Every Method")



def testMethod3(setup):

    print("This is Test Method 3")


def testMethod4(setup):
    print("This is Test Method 4")















