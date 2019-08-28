import pytest



#---------So to run this above "PYTEST" Method we use Terminal----

# How to open Terminal? - Got to "View" -> "Tool Windows" & Terminal

# To run the test we use "pytest" or "pytest -v -s PYTEST/test_PyTest_Fixtures.py" command in Terminal

# If we have multiple test in our package, we should specify test name
# like "pytest -v -s test_TestDemo.py" otherwise it will executed the test of the test cases

#-------------------------------------------------------------------



#----------- "@pytest.yield_fixture()"-------------


@pytest.yield_fixture()
def setup():

    print("Opening URL to Login")

    yield

    print("Closing browser after Login")




def testMethod3(setup):

    print("This is Login by email test")


def testMethod4(setup):
    print("This is Login by Facebook test")




























