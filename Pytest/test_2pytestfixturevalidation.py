import pytest

#Fixture : Making reusable code to be used across multiple test case
#scope=function means run before every test in page, scope=module means run once for all in the page,
# scope=class if the test is written in class format


#if any fixture is passed as an argument then it will first execute fixture and then the test will run
def test_forthCheck(preSetupWork):
    print("This is forth test")

