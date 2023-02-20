import time
from Base.ActionsPage import Action_page


class Cart_data(Action_page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    cart_data_count = "//span[@id='nav-cart-count']"
    cart_BTN = "//div[@id='nav-cart-count-container']"
    delete_item_BTN = "//*[@id='sc-active-C6502d5a6-a3ae-4b73-8571-90c1bf1a742e']//span[2]//input"

    def cart_data(self):
        element = self.get_text(self.cart_data_count, "XPATH", "textContent")
        if int(element) > 0:
            self.click(self.cart_BTN, "XPATH")
            for i in range(int(element)):
                time.sleep(2)
                self.click(self.delete_item_BTN, "XPATH")
                self.refresh_page()
            element = self.get_text(self.cart_data_count, "XPATH", "textContent")
            if int(element) == 0:
                return "cart empty"
            else:
                Cart_data(self.driver)
        else:
            return "cart empty"
