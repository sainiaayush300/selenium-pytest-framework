from utilities.config import BASE_URL
def test_iframe(driver):
    driver.get(BASE_URL+'iframe.php')
    driver.switch_to.frame(driver.find_element('id','demo-frame'))
    driver.find_element('id','frame-textbox').send_keys('hello')
    assert 'hello'==driver.find_element('id','frame-textbox').get_attribute('value')
