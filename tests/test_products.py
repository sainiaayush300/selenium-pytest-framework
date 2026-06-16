
from utilities.config import BASE_URL

def test_products(driver):
    driver.get(BASE_URL + "products.php")
    checks=driver.find_elements("class name","product-check")
    checks[0].click()
    assert checks[0].is_selected()
