import utilities.custom_logger as cl
import time
import logging
from base.basepage import BasePage


class MyProfilePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _menu_button = "//button[contains(@aria-label,'Menu')]"
    #_edit_link = "//a[@role='link']"
    _edit_link = "//a[contains(@href,'/profile/edit')]"
    _input_first_name = "//input[contains(@placeholder,'first name')]"
    _input_last_name = "//input[contains(@placeholder,'last name')]"
    _select_sex_m = "//div[contains(@aria-label,'Male')]"
    _select_sex_f = "//div[contains(@aria-label,'Female')]"
    _button_next = "//button[@role='button'][.='Next']"
    _button_save = "//div[contains(@class,'saveBtn')]//button[@role='button'][.='Save']"
    _left_back_arrow = "//i[contains(text(), 'arrow_back_ios')]/ancestor::a"
    _menu_myprofile = "//div[contains(@class,'q-item__label') and contains(text(), 'My Profile')]"
    _menu_home = "//div[contains(@class,'q-item__label') and contains(text(), 'Home')]"
    _myprofile_checker = "//div[contains(@class,'avatar-details')]"
    _menu_logout = "//div[contains(@class,'q-item__label') and contains(text(), 'Logout')]/parent::*"
    def clickMenuButton(self):
        self.elementClick(self._menu_button, locatorType="xpath")

    def clickMenuHome(self):
        self.elementClick(self._menu_home, locatorType="xpath")

    def clickMyProfile(self):
        self.elementClick(self._menu_myprofile, locatorType="xpath")

    def clickLogout(self):
        self.elementClick(self._menu_logout, locatorType="xpath")

    def clickEdit(self):
        self.elementClick(self._edit_link, locatorType="xpath")

    def clickBackArrow(self):
        self.elementClick(self._left_back_arrow, locatorType="xpath")

    def enterFirstName(self, name):
        self.sendKeys(name, self._input_first_name, locatorType="xpath")

    def enterLastName(self, name):
        self.sendKeys(name, self._input_last_name, locatorType="xpath")

    def selectOpositeSex(self):
        """
        If is one is selected then choose the oposite
        if none selected choose male
        """
        xx = self.verifySelectedSex(self._select_sex_m, self._select_sex_f)
        if xx == 'm':
            self.elementClick(self._select_sex_f, locatorType="xpath")
        else:
            if xx == 'f':
                self.elementClick(self._select_sex_m, locatorType="xpath")
            else:
                self.elementClick(self._select_sex_m, locatorType="xpath")

    def clearFields(self):
        self.emptyDataField(self._input_first_name, locatorType="xpath")
        self.emptyDataField(self._input_last_name, locatorType="xpath")

    def fillEditForm(self, firstname="", lastname=""):
        self.clickMenuButton()
        self.clickMyProfile()
        self.clickEdit()
        time.sleep(4)
        self.clearFields()
        self.enterFirstName(firstname)
        self.enterLastName(lastname)
        #self.selectOpositeSex()
        self.elementClick(self._button_next, locatorType="xpath")
        time.sleep(2)
        self.webScroll("down")
        time.sleep(2)
        self.elementClick(self._button_next, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._button_save, locatorType="xpath")
        time.sleep(2)
        self.clickMenuButton()
        time.sleep(2)
        self.clickMenuHome()
        time.sleep(4)
    def logout(self):
        self.clickMenuButton()
        self.clickLogout()
        time.sleep(4)
    def verifyFormSavedData(self, firstname="", lastname=""):
        #verify if the data edited are stored properly
        self.clickMenuButton()
        time.sleep(2)
        self.clickMyProfile()
        time.sleep(2)
        self.clickEdit()
        time.sleep(2)
        result_firstname = self.verifyFieldData(firstname, self._input_first_name, "xpath")
        result_lastname = self.verifyFieldData(lastname, self._input_last_name, "xpath")
        resultsList = [result_firstname, result_lastname]
        finalResult = True
        for i in resultsList:
            if not i:
                finalResult = False
                self.log.info("a False is found")
                break
        self.log.info("results list is " + str(resultsList) + "final result is:" + str(finalResult))
        self.clickBackArrow()
        time.sleep(2)
        return finalResult

    def verifMyProfileDisplayeds(self):
        self.clickMenuButton()
        time.sleep(2)
        self.clickMyProfile()
        time.sleep(2)
        result = self.isElementPresent(self._myprofile_checker, locatorType="xpath")
        return result

    def verifySelectedSex(self, sex_m, sex_f):
        result = None
        sex_result_m = self.getRadioElementStatus(sex_m, locatorType="xpath")
        sex_result_f = self.getRadioElementStatus(sex_f, locatorType="xpath")
        if sex_result_m:
            result = "m"
        else:
            if sex_result_f:
                result = "f"
        return result
