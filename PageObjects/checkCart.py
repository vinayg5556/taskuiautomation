import time
from Base.ActionsPage import ActionPage


class cartData(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _cartData_count = "//span[@id='nav-cart-count']"
    _cart_BTN = "//div[@id='nav-cart-count-container']"
    _delete_item_BTN = "//body/div[@id='a-page']/div[2]/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[3]/div[4]/div[1]/div[3]/div[1]/span[2]/span[1]/input[1]"

    def cartData(self):
        element = self.getText(self._cartData_count, "XPATH", "textContent")
        if int(element) > 0:
            self.click(self._cart_BTN, "XPATH")
            for i in range(int(element)):
                time.sleep(2)
                self.click(self._delete_item_BTN, "XPATH")
                self.refreshPage()
            element = self.getText(self._cartData_count, "XPATH", "textContent")
            if int(element) == 0:
                return "cart empty"
            else:
                cartData(self.driver)
        else:
            return "cart empty"
