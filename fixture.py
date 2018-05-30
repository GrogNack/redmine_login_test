from selenium import webdriver
import pytest

@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    request.addfinalizer(driver.quit)
    return driver
