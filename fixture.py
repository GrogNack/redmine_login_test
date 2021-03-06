from selenium import webdriver
from model.application import Application
import pytest

@pytest.fixture
def app(request):
    driver = webdriver.Firefox()
    # driver.implicitly_wait(30)
    request.addfinalizer(driver.quit)
    return Application(driver)
