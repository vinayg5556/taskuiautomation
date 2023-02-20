import unittest
import pytest
from PageObjects.loginPage import Login_page


@pytest.mark.usefixtures("beforeClass")
class Login_tests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_object(self):
        self.lp = Login_page(self.driver)

    @pytest.mark.login
    def test_page_login(self):
        self.lp.page_login()
