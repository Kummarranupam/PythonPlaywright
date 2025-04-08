import pytest

#Fixture : Making reusable code to be used across multiple test case
#scope=function means run before every test in page, scope=module means run once for all in the page,
# scope=class if the test is written in class format
@pytest.fixture(scope="module")
def preWork():
    print("I will setup browser instance")
    return "pass" # return any value

@pytest.fixture(scope="function")
def preWork2():
    print("I am setting prework2 module instance")   # setup condition
    yield # this creates separation between pre- and post-condition... test pauses here
    print("tear down validation")   # tear down condition (here can use database connection closing,
    # browser closing, cookies deletion)

#if any fixture is passed as an argument then it will first execute fixture and then the test will run
def test_initialCheck(preWork,preWork2):
    print("This is first test")
    assert preWork=="pass" # using the return value and validating it

#@pytest.mark.skip     #to skip any test
#@pytest.mark.smoke   # to give any specific tag name
def test_secondcheck(preWork,preWork2):
    print("This is second test")

def test_thirdcheck(preSetupWork):
    print("This is third test")
