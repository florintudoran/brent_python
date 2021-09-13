import utilities.custom_logger as cl
import time
import logging
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _login_link = "//a[contains(@class,'login-header')]"
    #name_field = "//input[contains(@class,'register-name')]"
    _email_field = "//input[contains(@type,'email')]"
    _password_field = "//input[contains(@type,'password')]"
    _answer_field = "//input[contains(@type,'text')]"
    _login_button = "//button[contains(@type,'button')]"
    _login_checker = "//button[contains(@aria-label,'Menu')]"

    _login_fail_checker = "//div[contains(@role,'alert') and contains(@class,'bg-red')]"
    _notification_turn_on = "//button//span[contains(text(), 'Turn on')]"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, name):
        self.sendKeys(name, self._password_field, locatorType="xpath")

    def enterSecretAnswer(self, answer):
        self.sendKeys(answer, self._answer_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def notificationPopUpTurnOn(self):
        self.elementClick(self._notification_turn_on, locatorType="xpath")
        time.sleep(4)

    def login(self, email="", password="", answer=""):
        #self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(3)
        self.enterSecretAnswer(answer)
        self.clickLoginButton()
        time.sleep(4)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._login_checker, locatorType="xpath")
        return result

    def verifyLoginFail(self):
        result = self.isElementPresent(self._login_fail_checker, locatorType="xpath")
        return result

    def clearFields(self):
        self.emptyDataField(self._email_field, locatorType="xpath")
        self.emptyDataField(self._password_field, locatorType="xpath")
        self.emptyDataField(self._answer_field, locatorType="xpath")

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Pathway App")

    def verifyLoginTitleMetaContent(self, titleName=""):
        return self.verifyPageMetaContent("title", titleName)