#any pytest filename should start with test_ or end with _test
#pytest method names should start with test
# All code should be wrapped in method and each method is treated as test case
# Py.test to run tests from cmd.
# Py.test -v for more information, here -v means verbose
# Py.test -v -s to see console logs
# If method names are same in a file then it will override, and latest method(test case) will be executed.
# py.test -k CreditCard -v -s, this flag executes all methods(test cases) which contains CreditCard as method name.
# py.test <file name>, to execute particular file in a package.
# py.test -m smoke -v -s, to execute marked tests. @pytest.mark.smoke (custom mark) is the syntax to mark any test.
# We can skip tests with @pytest.mark.skip tag. py.test -v -s marked tests will we skipped.
# We can mark a failed test case with @pytest.mark.xfail, so it will not consider the test result.
# Fixtures are used as setup and tear down methods for test cases. Create conftest.py and define fixtures, so that they will be used for all test cases
import pytest
def test_demo1():
    print("Hello Vino")
@pytest.mark.smoke
@pytest.mark.xfail
def test_sum(setup):
    a=10
    b=20
    c=a+b
    #print("sum is",c)
    assert c==35
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
def test_sub():
    a=30
    b=20
    c=a-b
    print(c)
    assert c==15
def test_demo7():
    print("test demo7")
def test_demo6():
    print("test demo6")
