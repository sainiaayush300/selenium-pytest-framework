from selenium.webdriver.common.by import By
from .base_page import BasePage
class LoginPage(BasePage):
    USERNAME=(By.ID,'username')
    PASSWORD=(By.ID,'password')
    LOGIN=(By.ID,'login-btn')
    ERROR=(By.ID,'error-msg')
    def login(self,u,p):
        self.visible(self.USERNAME).send_keys(u)
        self.driver.find_element(*self.PASSWORD).send_keys(p)
        self.driver.find_element(*self.LOGIN).click()
