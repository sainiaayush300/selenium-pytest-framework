from utilities.config import BASE_URL
def test_window(driver):
    driver.get(BASE_URL+'window.php')
    driver.find_element('id','new-window-link').click()
    driver.switch_to.window(driver.window_handles[1])
    assert 'New Window Opened' in driver.page_source
