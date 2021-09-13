from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=3)
    def test_validLogin(self):
        self.lp.login("florint_yp2@standby.team", "test1234", "florin")
        result_title = self.lp.verifyLoginTitleMetaContent("Pathway App")
        self.ts.mark(result_title, "Title Verified")
        result3 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_login", result3, "Valid login - good credentials - Verified")

    @pytest.mark.run(order=1)
    def test_invalidLogin_wrong_password(self):
        #invalid credentials
        self.lp.login("florint_yp2@standby.team", "wrongpass", "florin")
        result1 = self.lp.verifyLoginFail()
        self.ts.mark(result1, "Invalid login - wrong password - Verified")

    @pytest.mark.run(order=2)
    def test_invalidLogin_wrong_answer(self):
        #invalid credentials
        self.lp.login("florint_yp2@standby.team", "test1234", "wronganswer")
        result2 = self.lp.verifyLoginFail()
        self.ts.mark(result2, "Invalid login - wrong secret answer -  Verified")
