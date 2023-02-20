import time

from Base.ActionsPage import Action_page
from Utilities.configReader import read_config


class Login_page(Action_page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    sign_in_BTN_Link= "//a[@id='nav-link-accountList']"
    user_name_TB = "//input[@id='ap_email']"
    continue_BTN = "//input[@id='continue']"
    password_TB = "//input[@id='ap_password']"
    sign_in_BTN = "//input[@id='signInSubmit']"

    def page_login(self):
        self.click(self.sign_in_BTN_Link, "XPATH")
        time.sleep(2)
        self.send_keys(self.user_name_TB, "XPATH", read_config("login", "userName"))
        self.click(self.continue_BTN, "XPATH")
        self.send_keys(self.password_TB, "XPATH", read_config("login", "password"))
        self.click(self.sign_in_BTN, "XPATH")
        time.sleep(3)

