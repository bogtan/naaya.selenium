import os
import importlib
import time
import re
import unittest
from unittest import TestSuite, makeSuite
from NySeleniumConfig import NySeleniumConfig

def main():
    suite = TestSuite()
    test_files = os.listdir('./tests/')

    for test_file in test_files:
        file_parts = test_file.split(".")
        test_file_extension = file_parts[1]
        test_file_name = file_parts[0]

        if test_file_extension != "pyc" and test_file_name != "__init__":
            test_module = importlib.import_module('tests.' + test_file_name)
            test_name = 'Naaya' + test_file_name[0].upper() + \
                        test_file_name[1:]+ \
                        'Test'
            test_class = getattr(test_module, test_name)
            suite.addTest(makeSuite(test_class))

    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(main())
