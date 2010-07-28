import os, optparse, time, re, unittest, importlib, sys, inspect
from unittest import TestSuite, makeSuite
from selenium import selenium
from NySeleniumTest import NySeleniumTest

def main():
    parameters = optparse.OptionParser()
    parameters.add_option('--site', '-s', default='http://localhost/')
    parameters.add_option('--port', '-p', default='8080')
    parameters.add_option('--browsers', '-b', default="all")
    
    options, arguments = parameters.parse_args()
    
    print "Base link to start testing: " + options.site + ":" + options.port + "/"
    
    browsers = ['firefox', 'chrome', 'ie', 'all']
    
    param_browsers = options.browsers.replace("=", "")
    param_browsers = param_browsers.split(" ")
    
    print "Browsers: "
    for browser in param_browsers:
        print "- " + browser
    
    suite = TestSuite()
    
    # Check for tests files and them to test suite
    test_files = os.listdir('./tests/')
    
    for test_file in test_files:
        file_parts = test_file.split(".")
        
        test_file_extension = file_parts[1]
        test_file_name = file_parts[0]
        
        if test_file_extension != "pyc" and test_file_name != "__init__":
            test_module = importlib.import_module('tests.' + test_file_name)
            
            test_name = 'Naaya' + test_file_name[0].upper() + test_file_name[1:] + 'Test'
            
            test_class = getattr(test_module, test_name)
            suite.addTest(makeSuite(test_class))
    
    site = options.site
    
    return suite

if __name__ == '__main__':
    os.system('clear')
    
    unittest.TextTestRunner(verbosity=2).run(main())