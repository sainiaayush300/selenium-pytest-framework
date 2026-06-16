import pytest
from selenium import webdriver
@pytest.fixture
def driver():
    d=webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()
