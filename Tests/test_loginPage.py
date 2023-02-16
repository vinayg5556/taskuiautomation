import unittest
import pytest
from PageObjects.loginPage import loginPage


@pytest.mark.usefixtures("beforeClass")
class loginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)

    @pytest.mark.login
    def test_pageLogin(self):
        self.lp.pageLogin()
