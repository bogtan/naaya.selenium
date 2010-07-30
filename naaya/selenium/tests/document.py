import sys, os, unittest, time, re
sys.path.append(os.path.join(os.getcwd(), '..'))

from NySeleniumTest import NySeleniumTest

class NaayaDocumentTest(NySeleniumTest):
    def test_document(self):
        """Steps:
        1. Access the login page
        2. Check if elements username and passwords
           are loaded before typing the values and submit form
        3. Submit the form and redirect to the needed page if login
           succeeds
        4. If login fails return exception like error
        5. If login succeeds select value from typetoadd field and go to
           the redirected page
        6. Complete the form and submit
        7. Get the error/success message

        """

        self.verificationErrors = []
        self.selenium.open("/portal/login_html", True)
        loaded = False
        while(loaded == False):
            loaded = self.selenium.is_element_present("__ac_name") and \
            self.selenium.is_element_present("__ac_password")

        self.selenium.type("__ac_name", "admidsa")
        self.selenium.type("__ac_password", "admin")
        self.selenium.click("submit")

        self.selenium.wait_for_page_to_load("15000")

        if((self.selenium.is_element_present("__ac_name") == True) and \
            (self.selenium.is_element_present("__ac_password") == True)):
            print "Login failed! Try again..."
            return False

        self.selenium.open('/portal')
        self.selenium.wait_for_page_to_load("15000")
        self.selenium.click("link=Information")
        self.selenium.wait_for_page_to_load("15000")

        if(self.selenium.is_element_present("typetoadd") == False):
            print "An error occured while trying to access `typetoadd` \
                    select field name!";
            return False

        select_options = {'Folder': 1, 'News':2, 'Story':3, 'HTML Document':4, \
                          'Pointer':5, 'URL':6, 'Event':7, 'File':8, \
                          'GeoPoint':9}

        for option in select_options:
            if(self.selenium.is_element_present("typetoadd") != False):
                self.selenium.select("typetoadd", "index=" + str(select_options[option]))
                self.assertTrue(self.selenium.is_something_selected("typetoadd"));
                self.assertEquals(option, self.selenium.get_selected_label("typetoadd"));
                self.selenium.wait_for_page_to_load("15000")

            return False

        #
        #self.selenium.select("typetoadd", "label=HTML Document")
        #self.selenium.fireEvent("name=typetoadd", "change")
        #import pdb
        #pdb.set_trace()
        #self.selenium.wait_for_page_to_load("30000")
        #self.selenium.open("/portal/info/doc10154/add_html" , True)
        #self.selenium.wait_for_page_to_load("30000")
        #self.selenium.type("title", "dadasad")
        #self.selenium.type("keywords", "dasdaqeqdqwweq")
        #self.selenium.click("link=Today")
        #self.selenium.click("//input[@value='Submit']")
        #self.selenium.wait_for_page_to_load("30000")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

#if __name__ == "__main__":
#    suite = unittest.TestLoader().loadTestsFromTestCase(DocumentTest)
