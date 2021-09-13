import utilities.custom_logger as cl
import time
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _menu_button = "//button[contains(@aria-label,'Menu')]"
    _edit_link = "//a[contains(@href,'/profile/edit')]"
    _left_back_arrow = "//i[contains(text(), 'arrow_back_ios')]/ancestor::a"
    _menu_myprofile = "//div[contains(@class,'q-item__label') and contains(text(), 'My Profile')]"
    _menu_home = "//div[contains(@class,'q-item__label') and contains(text(), 'Home')]"
    _menu_logout = "//div[contains(@class,'q-item__label') and contains(text(), 'Logout')]/parent::*"
    _pathway_plan = "//a[@role='menuitem'][contains(@href,'/pathway-plan')]"
    _contacts = "//a[contains(@href,'/profile/edit')]"
    _tasks = "//a[contains(@href,'/profile/edit')]"
    _my_options = "//a[contains(@href,'/profile/edit')]"
    _app_settings = "//a[contains(@href,'/profile/edit')]"

    def clickMenuButton(self):
        self.elementClick(self._menu_button, locatorType="xpath")

    def clickMenuHome(self):
        self.elementClick(self._menu_home, locatorType="xpath")

    def clickPatwayPlans(self):
        self.elementClick(self._pathway_plan, locatorType="xpath")

    def clickMyProfile(self):
        self.elementClick(self._menu_myprofile, locatorType="xpath")

    def clickContacts(self):
        self.elementClick(self._contacts, locatorType="xpath")

    def clickTasks(self):
        self.elementClick(self._tasks, locatorType="xpath")

    def clickMyOptions(self):
        self.elementClick(self._my_options, locatorType="xpath")

    def clickAppSettings(self):
        self.elementClick(self._app_settings, locatorType="xpath")

    def clickLogout(self):
        self.elementClick(self._menu_logout, locatorType="xpath")

    def clickBackArrow(self):
        self.elementClick(self._left_back_arrow, locatorType="xpath")

    def logout(self):
        self.clickMenuButton()
        self.clickLogout()
        time.sleep(4)



