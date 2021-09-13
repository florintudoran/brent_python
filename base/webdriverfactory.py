"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://dev-brent.4you2test.com/login"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            #driver = webdriver.Chrome()
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe",
                                          options=chrome_options)
            driver.set_window_size(516, 990)
        else:
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--window-size=516x990")
            driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe",
                                      options=chrome_options)
            driver.set_window_size(516, 990)

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(5)
        # Maximize the windows
        #driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver