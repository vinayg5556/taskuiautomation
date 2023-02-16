import time
import unittest
import pytest
from PageObjects.loginPage import loginPage
from PageObjects.checkCart import cartData


@pytest.mark.usefixtures("beforeClass")
class checkCart(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        self.cart = cartData(self.driver)

    def test_cartCount(self):
        self.lp.pageLogin()
        self.cart.cartData()

