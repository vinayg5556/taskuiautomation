import time

from Base.ActionsPage import ActionPage
from Utilities.configReader import readConfig


class loginPage(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _signIn_BTN_Link= "//a[@id='nav-link-accountList']"
    _userName_TB = "//input[@id='ap_email']"
    _continue_BTN = "//input[@id='continue']"
    _password_TB = "//input[@id='ap_password']"
    _signIn_BTN = "//input[@id='signInSubmit']"

    def pageLogin(self):
        self.click(self._signIn_BTN_Link, "XPATH")
        time.sleep(2)
        self.sendKeys(self._userName_TB, "XPATH", readConfig("login", "userName"))
        self.click(self._continue_BTN, "XPATH")
        self.sendKeys(self._password_TB, "XPATH", readConfig("login", "password"))
        self.click(self._signIn_BTN, "XPATH")
        time.sleep(3)

