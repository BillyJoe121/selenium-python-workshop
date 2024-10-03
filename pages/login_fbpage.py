from selenium.webdriver.common.by import By
from .base_page import BasePage

class loginPage(BasePage):
    USER_NAME= (By.ID, 'username')
    USER_PASSWORD = (By.ID, 'password')
    USER_BTN = (By.ID, 'loginbtn')



    def login(self, email, password):
        self.enter_text(self.USER_NAME, email)
        self.enter_text(self.USER_PASSWORD, password)
        self.click(self.USER_BTN)
        
