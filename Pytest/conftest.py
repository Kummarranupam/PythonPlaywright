import pytest

#scope = session : This is used to run once for all the test files
@pytest.fixture(scope="session")
def preSetupWork():
    print("I will setup new browser instance")



