import time
import unittest
import pytest
from PageObjects.loginPage import loginPage
from PageObjects.checkCart import cartData
from PageObjects.searchMobiles import searchMobile


@pytest.mark.usefixtures("beforeClass")
class checkCart(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        self.cart = cartData(self.driver)
        self.sm = searchMobile(self.driver)

    def test_cartCount(self):
        self.lp.pageLogin()
        data = self.cart.cartData()
        time.sleep(5)
        if data == "cart empty":
            self.sm.searchMobile()

