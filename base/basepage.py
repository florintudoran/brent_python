"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def verifyPageMetaContent(self, metaName, contentToBeVerify):
        """
        Verify the content of a Meta

        Parameters:
            metaName: The meta name that needs to be verified
        Result : the content of the meta
        """
        try:
            element = self.getElement("//meta[contains(@name,'" + metaName + "')]", locatorType="xpath")
            actualContent = element.get_attribute("content")
            return self.util.verifyTextContains(actualContent, contentToBeVerify)
        except:
            self.log.error("Failed to get meta content")
            print_stack()
            return False

    def verifyFieldData(self, dataToVerify, locator, locatorType):
        """
        Verify the data from one filed is corresponding

        Parameters:
            dataToVerify: Data that needs to be verified
        """
        try:
            #actualData = self.getText(locator, locatorType)
            actualData = self.getInputTextValueText(locator, locatorType)
            return self.util.verifyTextContains(actualData, dataToVerify)
        except:
            self.log.error("Failed to get data field")
            print_stack()
            return False