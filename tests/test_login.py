import pytest
from utilities.config import BASE_URL
from pages.login_page import LoginPage

@pytest.mark.parametrize('u,p',[
('admin','admin123'),
])
def test_valid_login(driver,u,p):
    driver.get(BASE_URL)
    LoginPage(driver).login(u,p)
    assert 'dashboard' in driver.current_url

@pytest.mark.parametrize('u,p',[
('wrong','wrong'),
('admin','wrong'),
('wrong','admin123'),
('',''),
('admin',''),
('','admin123')
])
def test_invalid_login(driver,u,p):
    driver.get(BASE_URL)
    LoginPage(driver).login(u,p)
    assert 'Invalid Credentials' in driver.page_source
