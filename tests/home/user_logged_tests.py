from pages.home.login_page import LoginPage
from pages.home.menu_page import MenuPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoggedTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.menu = MenuPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_accessCategFromMenu(self):
        result2 = self.menu.verifyPathwayPlanDisplayed()
        self.ts.mark(result2, "PathwayPlan Module - displayed-  Verified")
        result3 = self.menu.verifMyProfileDisplayed()
        self.ts.mark(result3, "My profile Module - displayed-  Verified")
        result4 = self.menu.verifContactsDisplayed()
        self.ts.mark(result4, "Contacts Module - displayed-  Verified")
        resultf5 = self.menu.verifTasksDisplayed()
        self.ts.markFinal("test_display_categories_from_menu", resultf5, "Tasks Module - displayed - Verified")

    @pytest.mark.run(order=1)
    def test_login(self):
        #test the login
        self.lp.login("florint_yp2@standby.team", "test1234", "florin")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Valid login - good credentials - Verified")
