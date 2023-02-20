import time
import unittest
import pytest
from PageObjects.loginPage import Login_page
from PageObjects.checkCart import Cart_data


@pytest.mark.usefixtures("beforeClass")
class Check_cart(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_object(self):
        self.lp = Login_page(self.driver)
        self.cart = Cart_data(self.driver)

    def test_cart_count(self):
        self.lp.page_login()
        self.cart.cart_data()

