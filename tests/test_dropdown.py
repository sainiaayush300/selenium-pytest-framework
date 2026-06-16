from selenium.webdriver.support.ui import Select
from utilities.config import BASE_URL
def test_dropdown_india(driver):
    driver.get(BASE_URL+'dropdown.php')
    s=Select(driver.find_element('id','country'))
    s.select_by_value('IN')
    assert s.first_selected_option.text=='India'
