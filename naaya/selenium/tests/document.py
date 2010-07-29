import sys, os, unittest, time, re
sys.path.append(os.path.join(os.getcwd(), '..'))

from NySeleniumTest import NySeleniumTest

class NaayaDocumentTest(NySeleniumTest):
    def test_document(self):
        print sys.argv
        
        self.verificationErrors = []
        
        #
        #Steps:
        #    
        #    1. Access the login page
        #    2. Check if elements username and passwords
        #       are loaded before typing the values and submit form
        #    3. Submit the form and redirect to the needed page if login succeeds
        #    4. If login fails return exception like error
        #    5. If login succeeds select value from typetoadd field and go to the redirected page
        #    6. Complete the form and submit
        #    7. Get the error/success message
        #
        
        sel = self.selenium
        # 1
        sel.open("/portal/login_html", True)
        
        # 2
        loaded = False
        while(loaded == False):
            loaded = sel.is_element_present("__ac_name") and sel.is_element_present("__ac_password")
        
        sel.type("__ac_name", "admin")
        sel.type("__ac_password", "admin")
        sel.click("submit")
        
        sel.wait_for_page_to_load("15000")
        
        if((sel.is_element_present("__ac_name") == True) and (sel.is_element_present("__ac_password") == True)):
            print "Login failed! Try again..."
            return False
        
        sel.open('/portal')
        sel.wait_for_page_to_load("15000")
        sel.click("link=Information")
        sel.wait_for_page_to_load("15000")
        
        if(sel.is_element_present("typetoadd") == False):
            print "An error occured while trying to access `typetoadd` select field name!";
            return False
        
        select_options = {'Folder': 1, 'News':2, 'Story':3, 'HTML Document':4, 'Pointer':5, 'URL':6, 'Event':7, 'File':8, 'GeoPoint':9}
        
        for option in select_options:
            if(sel.is_element_present("typetoadd") != False):
                sel.select("typetoadd", "index=" + str(select_options[option]))
                self.assertTrue(sel.is_something_selected("typetoadd"));
                self.assertEquals(option, sel.get_selected_label("typetoadd"));
                sel.wait_for_page_to_load("15000")
            
            return False
        
        #
        #sel.select("typetoadd", "label=HTML Document")
        #sel.fireEvent("name=typetoadd", "change")
        #import pdb
        #pdb.set_trace()
        #sel.wait_for_page_to_load("30000")
        #sel.open("/portal/info/doc10154/add_html" , True)
        #sel.wait_for_page_to_load("30000")
        #sel.type("title", "dadasad")
        #sel.type("keywords", "dasdaqeqdqwweq")
        #sel.click("link=Today")
        #sel.click("//input[@value='Submit']")
        #sel.wait_for_page_to_load("30000")
        
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DocumentTest)