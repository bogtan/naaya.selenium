import sys, os, unittest, time, re
sys.path.append(os.path.join(os.getcwd(), '..'))

from NySeleniumTest import NySeleniumTest

class NaayaDocumentTest(NySeleniumTest):
    def test_document(self):
        sel = self.selenium
        sel.open("/portal/login_html", True)
        sel.type("__ac_name", "admin")
        sel.type("__ac_password", "admin")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Information")
        sel.wait_for_page_to_load("30000")
        sel.select("typetoadd", "label=HTML Document")
        sel.wait_for_page_to_load("30000")
        sel.open("/portal/info/doc10154/add_html" , True)
        sel.wait_for_page_to_load("30000")
        sel.type("title", "dadasad")
        sel.type("keywords", "dasdaqeqdqwweq")
        sel.click("link=Today")
        sel.click("//input[@value='Submit']")
        sel.wait_for_page_to_load("30000")
        
    def tearDown(self):
        #self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DocumentTest)