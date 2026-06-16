
from pages.login_page import LoginPage
from utilities.config import BASE_URL

def test_logout(driver):
    driver.get(BASE_URL)
    LoginPage(driver).login("admin","admin123")
    driver.get(BASE_URL+"logout.php")
    assert "index.php" in driver.current_url or "selenium_demo" in driver.current_url
