
from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    WELCOME=(By.ID,'welcome')
    LOGOUT=(By.ID,'logout-link')
    def get_welcome_text(self):
        return self.wait_visible(self.WELCOME).text
    def is_logout_visible(self):
        return self.wait_visible(self.LOGOUT).is_displayed()
