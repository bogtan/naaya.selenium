import sys
import os
import re
import optparse
import logging
from selenium import selenium
sys.path.append(os.path.join(os.getcwd(), '..'))

from NySeleniumTest import NySeleniumTest
from NySeleniumConfig import NySeleniumConfig

class NaayaDocumentTest(NySeleniumTest):
    def test_document(self):
        """
        Steps:
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

        logger = logging.getLogger("Naaya Document Test")
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        configuration = NySeleniumConfig()

        self.verificationErrors = []
        self.selenium.open("/portal/login_html", True)
        loaded = False
        while(loaded == False):
            loaded = self.selenium.is_element_present("__ac_name") and \
            self.selenium.is_element_present("__ac_password")

        self.selenium.type("__ac_name", configuration.data['user'])
        self.selenium.type("__ac_password", configuration.data['password'])
        self.selenium.click("submit")

        self.selenium.wait_for_page_to_load("15000")

        if(self.selenium.is_element_present("__ac_name") and \
            (self.selenium.is_element_present("__ac_password"))):
            self.verificationErrors.append("Login failed! Username and/or"
                                           "password incorrect! Try again...")

        self.selenium.open('/portal')
        self.selenium.wait_for_page_to_load("15000")
        self.selenium.click("link=Information")
        self.selenium.wait_for_page_to_load("15000")

        if(self.selenium.is_element_present("typetoadd") == False):
            self.verificationErrors.append("An error occured while trying to"
                                           "access `typetoadd` select field"
                                           " name!")

        select_options = {'Folder': 1, 'News':2, 'Story':3, 'HTML Document':4,\
                          'Pointer':5, 'URL':6, 'Event':7, 'File':8, \
                          'GeoPoint':9}
        for option in select_options:
            if(self.selenium.is_element_present("typetoadd") != False):
                if(option == "Story"):
                    self.selenium.select("typetoadd", "index=" + str(select_options[option]))
                    self.assertTrue(self.selenium.is_something_selected("typetoadd"));
                    self.assertEquals(option, self.selenium.get_selected_label("typetoadd"));
                    self.selenium.wait_for_page_to_load("15000")
                    if(self.selenium.is_element_present("id=lang") == False):
                        self.verificationErrors.append("Language element not"
                                                       " identified")

                    self.selenium.select("id=lang", "value=en")
                    self.selenium.type("title", "Test Story")
                    self.selenium.type("id=description", "This is a text")
                    self.selenium.type("keywords", "short, story, test story")
                    self.selenium.type("sortorder", "125")
                    self.selenium.click("link=Today")
                    self.selenium.click("//img[@alt='Calendar']")
                    self.selenium.click("link=16")
                    self.selenium.click("link=Today")
                    self.selenium.click("discussion")
                    self.selenium.type("resourceurl", "http://www.eaudeweb.ro/")
                    self.selenium.type("source", "http://www.wikipedia.com/")
                    self.selenium.type("frontpicture", "/home/bogdan/Desktop/no-pre.png")
                    self.selenium.click("//input[@value='Submit']")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Test Story")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("//div[@id='admin_this_folder']/a[2]/span")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("title", "Test Story Updated")
                    self.selenium.type("coverage", "Update geo coverate")
                    self.selenium.type("keywords", "short, story, test story, updated keyword")
                    self.selenium.type("sortorder", "122")
                    self.selenium.click("//img[@alt='Calendar']")
                    self.selenium.click("//div[@id='middle_port']/div[5]/form/div[9]")
                    self.selenium.click("link=Today")
                    self.selenium.click("discussion")
                    self.selenium.click("discussion")
                    self.selenium.click("topitem")
                    self.selenium.type("resourceurl", "http://www.eaudeweb.ro/updated")
                    self.selenium.type("source", "http://www.wikipedia.com/updataed")
                    self.selenium.type("frontpicture", "/home/bogdan/Desktop/89366.png")
                    self.selenium.click("//input[@value='Save changes']")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("15000")
                    self.selenium.click("link=Test Story Updated")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("//div[@id='admin_this_folder']/a[1]/span")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("commitVersion:method")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Checkout")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("discardVersion:method")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Add comment")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("title", "My comment")
                    self.selenium.click("//input[@value='Submit']")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Delete comment")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("//input[@name='id' and @value='test-story']")
                    self.selenium.click("deleteObjects:method")
                    self.failUnless(re.search(r"^Are you sure[\s\S]$", self.selenium.get_confirmation()))

                #if(option == 'Folder'):
                #    self.selenium.select("typetoadd", "index=" + str(select_options[option]))
                #    self.assertTrue(self.selenium.is_something_selected("typetoadd"));
                #    self.assertEquals(option, self.selenium.get_selected_label("typetoadd"));
                #    self.selenium.wait_for_page_to_load("15000")
                #    if(self.selenium.is_element_present("id=lang") == False):
                #        self.verificationErrors.append("Language element not"
                #                                       " identified")
                #
                #
                #    self.selenium.select("id=lang", "value=en")
                #    self.selenium.type("title", "My Folder")
                #    self.selenium.type("id=description", "This is a text")
                #    self.selenium.type("keywords", "my folder, test, folder, test folder")
                #    self.selenium.type("sortorder", "132")
                #    self.selenium.click("//img[@alt='Calendar']")
                #    self.selenium.click("//div[@id='middle_port']/form/div[8]")
                #    self.selenium.click("link=Today")
                #    self.selenium.click("discussion")
                #    self.selenium.click("//img[@alt='Calendar']")
                #    self.selenium.click("link=28")
                #    self.selenium.type("maintainer_email", "bogdan.tanase@eaudeweb.ro")
                #    self.selenium.click("//input[@value='Submit']")
                #    self.selenium.wait_for_page_to_load("30000")
                #
                #if(option == "News"):
                #    self.selenium.select("typetoadd", "index=" + str(select_options[option]))
                #    self.assertTrue(self.selenium.is_something_selected("typetoadd"));
                #    self.assertEquals(option, self.selenium.get_selected_label("typetoadd"));
                #    self.selenium.wait_for_page_to_load("15000")
                #    if(self.selenium.is_element_present("id=lang") == False):
                #        self.verificationErrors.append("Language element not"
                #                                       " identified")
                #
                #
                #    self.selenium.select("id=lang", "value=en")
                #    self.selenium.type("title", "My News")
                #    self.selenium.type("coverage", "aoqk")
                #    self.selenium.type("coverage", "test coverage")
                #    self.selenium.type("keywords", "news, test")
                #    self.selenium.type("sortorder", "83")
                #    self.selenium.click("link=Today")
                #    self.selenium.click("//img[@alt='Calendar']")
                #    self.selenium.click("link=31")
                #    self.selenium.type("releasedate", "29/07/2009")
                #    self.selenium.click("discussion")
                #    self.selenium.click("link=Today")
                #    self.selenium.click("//div[@id='middle_port']/form/div[10]/span/a[1]")
                #    self.selenium.click("//a[@id='calendarlink1']/img")
                #    self.selenium.click("//div[@id='calendarin1']/table/tbody/tr[2]/td[1]/a")
                #    self.selenium.click("topitem")
                #    self.selenium.type("resourceurl", "http://www.eaudeweb.ro/")
                #    self.selenium.type("source", "http://www.wikipedia.com/")
                #    self.selenium.type("smallpicture", "/home/bogdan/Desktop/brain-icon.png")
                #    self.selenium.click("//input[@value='Submit']")
                #    self.selenium.wait_for_page_to_load("30000")

    def tearDown(self):
        #self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
