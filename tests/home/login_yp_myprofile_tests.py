from pages.home.login_page import LoginPage
from pages.home.menu_page import MenuPage
from pages.home.myprofile_page import MyProfilePage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoggedTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.menu = MenuPage(self.driver)
        self.edit = MyProfilePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_accessCategFromMenu(self):
        #result3 = self.menu.verifMyProfileDisplayed()
        #self.ts.mark(result3, "My profile Module - displayed-  Verified")
        self.lp.notificationPopUpTurnOn()
        self.edit.fillEditForm("Diaconu", "Maria")
        result2 = self.edit.verifyFormSavedData("fDiaconu", "fMaria")
        self.ts.markFinal("test_entered_form_data", result2, "My profile Module - Data entered  -  Verified")

    @pytest.mark.run(order=1)
    def test_login(self):
        #test the login
        self.lp.login("maria.tdiaconu+YP41@gmail.com", "test1234", "test")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Valid login - good credentials - Verified")
