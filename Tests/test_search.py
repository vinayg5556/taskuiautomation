import time
import unittest
import pytest
from PageObjects.loginPage import Login_page
from PageObjects.checkCart import Cart_data
from PageObjects.searchMobiles import Search_mobile


@pytest.mark.usefixtures("beforeClass")
class checkCart(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = Login_page(self.driver)
        self.cart = Cart_data(self.driver)
        self.sm = Search_mobile(self.driver)

    def test_cartCount(self):
        self.lp.page_login()
        data = self.cart.cart_data()
        time.sleep(5)
        if data == "cart empty":
            self.sm.search_mobile()

