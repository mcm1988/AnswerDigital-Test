import os
from selenium import webdriver
from Values import strings


class Driver:

    def __init__(self):
        chrome_path = strings.driver_path + "chromedriver.exe"
        firefox_path = strings.driver_path + "geckodriver.exe"
        ie_path = strings.driver_path + "IEDriverServer.exe"
        edge_path = strings.driver_path + "MicrosoftWebDriver.exe"
        try:
            if os.environ['webdriver'].upper() == "FIREFOX":
                self.instance = webdriver.Firefox(executable_path=firefox_path)
            if os.environ['webdriver'].upper() == "IE":
                self.instance = webdriver.Ie(executable_path=ie_path)
            if os.environ['webdriver'].upper() == "EDGE":
                self.instance = webdriver.Edge(executable_path=edge_path)
            if os.environ['webdriver'].upper() == "CHROME":
                self.instance = webdriver.Chrome(executable_path=chrome_path)
            else:
                print("Unknown 'webdriver' environment variable. Defaulting to Chrome")
                self.instance = webdriver.Chrome(executable_path=chrome_path)
        except KeyError:
            print("'webdriver' environment variable not set. Defaulting to Chrome")
            self.instance = webdriver.Chrome(executable_path=chrome_path)

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")
