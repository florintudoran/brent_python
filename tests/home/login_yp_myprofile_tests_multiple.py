from pages.home.login_page import LoginPage
from pages.home.menu_page import MenuPage
from pages.home.myprofile_page import MyProfilePage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoggedTestsMultiple(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.menu = MenuPage(self.driver)
        self.edit = MyProfilePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("florin.tudoran+YP@gmail.com", "test1234", "test", "Andrew", "Jonshon", "Andrew", "Jonshon"))
    @unpack
    def test_login(self, loginUsername, loginPass, loginSecret, editFirstName, editLastName, verFirstName, verLastName):
        #test the logins
        self.lp.login(loginUsername, loginPass, loginSecret)
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Valid login - good credentials - Verified")
        self.lp.notificationPopUpTurnOn()
        self.edit.fillEditForm(editFirstName, editLastName)
        result2 = self.edit.verifyFormSavedData(verFirstName, verLastName)
        self.ts.markFinal("test_entered_form_data", result2, "My profile Module - Data entered  -  Verified")
        self.edit.logout()