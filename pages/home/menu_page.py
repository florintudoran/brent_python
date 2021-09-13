import utilities.custom_logger as cl
import time
import logging
from base.basepage import BasePage


class MenuPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _menu_button = "//button[contains(@aria-label,'Menu')]"
    _menu_pathwayplan = "//div[contains(@class,'q-item__label') and contains(text(), 'Pathway Plan')]"
    _pathwayplan_checker = "//div[contains(@class,'q-toolbar__title ellipsis') and contains(text(), 'Pathway Plan')]"
    #menu_pathwayplan = "Pathway Plan"
    _menu_contacts = "//div[contains(@class,'q-item__label') and contains(text(), 'Contacts')]"
    _contacts_checker = "//div[contains(@class,'q-toolbar__title ellipsis') and contains(text(), 'Contacts')]"
    _menu_myprofile = "//div[contains(@class,'q-item__label') and contains(text(), 'My Profile')]"
    _myprofile_checker = "//div[contains(@class,'avatar-details')]"
    _menu_tasks = "//div[contains(@class,'q-item__label') and contains(text(), 'Tasks')]"
    _tasks_checker = "//div[contains(@class,'q-toolbar__title ellipsis') and contains(text(), 'Tasks')]"



    def clickMenuButton(self):
        self.elementClick(self._menu_button, locatorType="xpath")

    def clickPathwayPlan(self):
        self.elementClick(self._menu_pathwayplan, locatorType="xpath")

    def clickMyProfile(self):
        self.elementClick(self._menu_myprofile, locatorType="xpath")

    def clickContacts(self):
        self.elementClick(self._menu_contacts, locatorType="xpath")

    def clickTasks(self):
        self.elementClick(self._menu_tasks, locatorType="xpath")


    def verifyPathwayPlanDisplayed(self):
        self.clickMenuButton()
        time.sleep(2)
        self.clickPathwayPlan()
        time.sleep(2)
        result = self.isElementPresent(self._pathwayplan_checker, locatorType="xpath")
        return result

    def verifMyProfileDisplayed(self):
        self.clickMenuButton()
        time.sleep(2)
        self.clickMyProfile()
        time.sleep(2)
        result = self.isElementPresent(self._myprofile_checker, locatorType="xpath")
        return result

    def verifContactsDisplayed(self):
        self.clickMenuButton()
        time.sleep(2)
        self.clickContacts()
        time.sleep(2)
        result = self.isElementPresent(self._contacts_checker, locatorType="xpath")
        return result

    def verifTasksDisplayed(self):
        self.clickMenuButton()
        time.sleep(2)
        self.clickTasks()
        time.sleep(2)
        result = self.isElementPresent(self._tasks_checker, locatorType="xpath")
        return result
