import unittest
import optparse
from unittest import TestCase, TestSuite, makeSuite
from selenium import selenium
from NySeleniumConfig import NySeleniumConfig

class NySeleniumTest(unittest.TestCase):
    def setUp(self):
        configuration = NySeleniumConfig()
        self.verificationErrors = []
        supported_browsers = [ '*firefox', '*mock', '*firefoxproxy',
                             '*pifirefox', '*chrome', '*iexploreproxy',
                             '*iexplore', '*firefox3', '*safariproxy',
                             '*googlechrome', '*konqueror', '*firefox2',
                             '*safari', '*piiexplore', '*firefoxchrome',
                             '*opera', '*iehta', '*custom']
        browsers = configuration.data['browsers'].split(",")

        if(browsers[0] == '*all'):
            for browser in supported_browsers:
                self.selenium = selenium("localhost", 5555, browser,\
                                         configuration.data['site'])
                self.selenium.start()
        elif((len(browsers) == 1) and (browsers[0] in supported_browsers)):
            self.selenium = selenium("localhost", 5555, browsers[0],\
                                         configuration.data['site'])
            self.selenium.start()
        elif((len(browsers) > 1)):
            for browser in browsers:
                if browser in supported_browsers:
                    import pdb;
                    pdb.set_trace()
                    print browser
                    self.selenium = selenium("localhost", 5555, browsers[0],\
                                         configuration.data['site'])
                    self.selenium.start()
        else:
            print "No existing browser!"
