from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashBoardPage(BasePage):
    TOP_BAR= (By.ID, 'topBar')

    def isTopBar(self):
        return self.find_element(self.TOP_BAR).is_displayed()
