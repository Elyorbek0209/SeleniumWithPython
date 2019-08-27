import pytest


#----How to Work with PyTest Fixtures----

# The purpose of the test fixtures is to provide a fixed baseline
# upon which tests can reliably & repeatedly execute


# @pytest.fixture()

# - Execute specific method before every test method


# @pytest.yield_fixture()

# - Execute specific method before & after every test method


@pytest.fixture()
def setup():

    print("Once Before Every Method")


def testMethod1(setup):

    print("This is Test Method 1")


def testMethod2(setup):
    print("This is Test Method 2")


















