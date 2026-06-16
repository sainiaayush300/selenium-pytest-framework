from utilities.config import BASE_URL
def test_simple_alert(driver):
    driver.get(BASE_URL+'alert.php')
    driver.find_element('id','simple-alert').click()
    a=driver.switch_to.alert
    assert 'Simple Alert' in a.text
    a.accept()
