import unittest
import optparse
from unittest import TestCase, TestSuite, makeSuite
from selenium import selenium
from NySeleniumConfig import NySeleniumConfig

class NySeleniumTest(unittest.TestCase):
    def setUp(self):
        parameters = optparse.OptionParser()
        configuration = NySeleniumConfig(parameters)
        
        self.verificationErrors = []

        if(configuration.data['browsers'] == "all"):
            for browser in [ '*firefox', '*mock', '*firefoxproxy',
                             '*pifirefox', '*chrome', '*iexploreproxy',
                             '*iexplore', '*firefox3', '*safariproxy',
                             '*googlechrome', '*konqueror', '*firefox2',
                             '*safari', '*piiexplore', '*firefoxchrome',
                             '*opera', '*iehta', '*custom']:
                self.selenium = selenium("localhost", 5555, browser, "http://localhost:8080/")
                self.selenium.start()
