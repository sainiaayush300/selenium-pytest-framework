
from utilities.config import BASE_URL

def test_profile(driver):
    driver.get(BASE_URL + "profile.php")
    driver.find_element("id","first-name").send_keys("Aayush")
    assert driver.find_element("id","first-name").get_attribute("value")=="Aayush"
