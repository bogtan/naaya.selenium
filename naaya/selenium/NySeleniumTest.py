import unittest
from unittest import TestCase, TestSuite, makeSuite
from selenium import selenium

class NySeleniumTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 5555, "*chrome", "http://localhost:8080/")
        self.selenium.start()
    