from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.configReader import read_config

class Driver:

    def getDriverMethod(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(read_config("url", "webUrl"))
        driver.maximize_window()
        driver.implicitly_wait(15)
        return driver



