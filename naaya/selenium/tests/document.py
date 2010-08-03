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

        logger.info("Attempt log in...")
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

        logger.info("Succesfully logged in...")
        logger.info("Access portal`s main page")

        self.selenium.open('/portal')
        self.selenium.wait_for_page_to_load("15000")
        logger.info("Access Information page")
        self.selenium.click("link=Information")
        self.selenium.wait_for_page_to_load("15000")

        logger.info("Looking for `typetoadd` select field...")
        if(self.selenium.is_element_present("typetoadd") == False):
            self.verificationErrors.append("An error occured while trying to"
                                           "access `typetoadd` select field"
                                           " name!")

        logger.info("`Typetoadd` found...")

        select_options = {'Folder': 1, 'News':2, 'Story':3, 'HTML Document':4,\
                          'Pointer':5, 'URL':6, 'Event':7, 'File':8, \
                          'GeoPoint':9}

        logger.info("Start test...")
        for option in select_options:

            logger.info("Access option from select options:  " + option)

            if(self.selenium.is_element_present("typetoadd") != False):
                if(option == "Story"):
                    logger.info("Try to select STORY item...")
                    self.selenium.select("typetoadd", "index=" + str(select_options[option]))
                    self.assertTrue(self.selenium.is_something_selected("typetoadd"));
                    #self.assertEquals(option, self.selenium.get_selected_label("typetoadd"));
                    self.selenium.wait_for_page_to_load("15000")
                    if(self.selenium.is_element_present("id=lang") == False):
                        self.verificationErrors.append("Language element not"
                                                       " identified")

                    logger.info("STORY item selected, page ADD News accessed...")

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

                    logger.info("Test STORY added...")

                    self.selenium.click("link=Test Story")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Access EDIT Test STORY...")

                    self.selenium.click("//div[@id='admin_this_folder']/a[2]/span")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("title", "Test Story Updated")
                    self.selenium.type("id=description", "This is a text updated")
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

                    logger.info("Test STORY succesfully edited...")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")

                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("15000")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Test Story Updated")
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

                    logger.info("Add STORY comment...")

                    self.selenium.type("title", "My comment")
                    self.selenium.click("//input[@value='Submit']")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Delete comment")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Delete STORY comment...")
                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("//input[@name='id' and @value='test-story']")
                    self.selenium.click("deleteObjects:method")

                    logger.info("Test STORY deleted, Test passed...")

                    self.failUnless(re.search(r"^Are you sure[\s\S]$", self.selenium.get_confirmation()))

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")

                if(option == "Folder"):
                    logger.info("Try to select Folder item...")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Portal")
                    self.selenium.click("link=Portal")
                    self.selenium.wait_for_page_to_load("30000")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.select("typetoadd", "index=" + str(select_options[option]))
                    self.assertTrue(self.selenium.is_something_selected("typetoadd"));
                    #self.assertEquals(option, self.selenium.get_selected_label("typetoadd"));
                    self.selenium.wait_for_page_to_load("30000")
                    if(self.selenium.is_element_present("id=lang") == False):
                        self.verificationErrors.append("Language element not"
                                                       " identified")

                    logger.info("Folder item selected...")
                    logger.info("Add Folder page accessed...")

                    self.selenium.select("id=lang", "value=en")
                    self.selenium.type("title", "My Folder")
                    self.selenium.type("id=description", "This is a text")
                    self.selenium.type("coverage", "Folder geo cov")
                    self.selenium.type("keywords", "my folder, test, folder, test folder")
                    self.selenium.type("sortorder", "124")
                    self.selenium.click("link=Today")
                    self.selenium.click("//img[@alt='Calendar']")
                    self.selenium.click("link=1")
                    self.selenium.click("discussion")
                    self.selenium.click("discussion")
                    self.selenium.type("maintainer_email", "bo")
                    self.selenium.click("//input[@value='Submit']")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Test Folder added...")

                    self.selenium.click("//table[@id='folderfile_list']/tbody/tr[2]/td[3]/a")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("//div[@id='admin_this_folder']/a[1]/span")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Test Folder editing accessed...")

                    self.selenium.type("title", "My Folder updated")
                    self.selenium.type("id=description", "This is a text updated")
                    self.selenium.type("coverage", "Folder geo cov updated")
                    self.selenium.type("keywords", "my folder, test, folder, test folder, folder updated")
                    self.selenium.type("sortorder", "122")
                    self.selenium.click("link=Today")
                    self.selenium.click("discussion")
                    self.selenium.type("maintainer_email", "bogdan.tanase@eaudeweb.ro")
                    self.selenium.click("saveProperties:method")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Test Folder succesfully edited...")

                    self.selenium.click("link=Back to index")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("//div[@id='admin_this_folder']/a[2]/span")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Test Folder subobjects accessed...")

                    self.selenium.click("load_default")
                    self.selenium.click("load_default")
                    self.selenium.remove_selection("ny_subobjects", "label=Folder")
                    self.selenium.remove_selection("ny_subobjects", "label=Story")
                    self.selenium.remove_selection("ny_subobjects", "label=HTML Document")
                    self.selenium.remove_selection("ny_subobjects", "label=Pointer")
                    self.selenium.remove_selection("ny_subobjects", "label=URL")
                    self.selenium.remove_selection("ny_subobjects", "label=Event")
                    self.selenium.remove_selection("ny_subobjects", "label=File")
                    self.selenium.remove_selection("ny_subobjects", "label=GeoPoint")
                    self.selenium.add_selection("ny_subobjects", "label=Folder")
                    self.selenium.remove_selection("ny_subobjects", "label=News")
                    self.selenium.add_selection("ny_subobjects", "label=Story")
                    self.selenium.add_selection("ny_subobjects", "label=News")
                    self.selenium.click("submit")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Test Folder subobjects added...")

                    self.selenium.click("link=Back to index")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Test Folder approvals accessed...")

                    self.selenium.click("link=Approvals")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Back to index")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Sort order")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Back to index")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Test Folder restricts accessed...")

                    self.selenium.click("link=Restrict")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.add_selection("roles", "label=Contributor")
                    self.selenium.add_selection("roles", "label=Reviewer")
                    self.selenium.add_selection("roles", "label=Authenticated")
                    self.selenium.click("access_to")
                    self.selenium.click("//input[@value='Save changes']")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Test Folder restricts added...")

                    self.selenium.click("link=Back to index")
                    self.selenium.wait_for_page_to_load("30000")

                    self.selenium.click("link=CSV export")
                    self.selenium.wait_for_page_to_load("30000")
                    #self.selenium.click("export:method")
                    #self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Back to index")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=CSV import")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("data", "/home/bogdan/Desktop/Naaya\ Folder\ Export.csv")
                    self.selenium.click("do_import:method")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("//div[@id='breadcrumbtrail']/a[3]")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Add folder comment")

                    self.selenium.click("link=Add comment")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("title", "My comment")
                    self.selenium.click("//input[@value='Submit']")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Folder comment succesully added")

                    self.selenium.click("link=Delete comment")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Folder comment succesully deleted")
                    logger.info("Add NEWS item to folder")

                    self.selenium.select("typetoadd", "label=News")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("title", "My folder News")
                    self.selenium.type("id=description", "This is a text")
                    self.selenium.type("coverage", "Folder geo cov news")
                    self.selenium.type("keywords", "my folder, test, folder, test folder, news")
                    self.selenium.type("sortorder", "25")
                    self.selenium.click("link=Today")
                    self.selenium.click("discussion")
                    self.selenium.click("//div[@id='middle_port']/form/div[10]/span/a[1]")
                    self.selenium.click("//a[@id='calendarlink1']/img")
                    self.selenium.click("//div[@id='calendarin1']/table/tbody/tr[2]/td[4]/a")
                    self.selenium.click("topitem")
                    self.selenium.type("resourceurl", "http://www.eaudeweb.ro/")
                    self.selenium.type("source", "http://www.wikipedia.com/")
                    self.selenium.type("smallpicture", "/home/bogdan/Desktop/no-pre.png")
                    self.selenium.click("//input[@value='Submit']")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("NEWS item succesfully added to folder")

                    self.selenium.click("//input[@type='checkbox']")
                    self.selenium.click("deleteObjects:method")
                    self.failUnless(re.search(r"^Are you sure[\s\S]$", self.selenium.get_confirmation()))

                    logger.info("NEWS item succesfully deleted from folder")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("id")
                    self.selenium.click("deleteObjects:method")
                    self.failUnless(re.search(r"^Are you sure[\s\S]$", self.selenium.get_confirmation()))

                    logger.info("Folder succesfully deleted")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")

                if(option == "News"):
                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("typetoadd")
                    if(loaded == False):
                        self.verificationErrors.append("Information page was"
                                                       " not loaded!"
                                                       " Test closed!")

                    logger.info("Attempt to select NEWS item...")

                    self.selenium.select("typetoadd", "index=" + str(select_options[option]))
                    self.assertTrue(self.selenium.is_something_selected("typetoadd"));
                    #self.assertEquals(option, self.selenium.get_selected_label("typetoadd"));
                    self.selenium.wait_for_page_to_load("30000")
                    if(self.selenium.is_element_present("id=lang") == False):
                        self.verificationErrors.append("Language element not"
                                                       " identified")

                    logger.info("NEWS item selected... Add page accessed...")

                    self.selenium.select("id=lang", "value=en")
                    self.selenium.type("title", "My News")
                    self.selenium.type("id=description", "This is a text")
                    self.selenium.type("coverage", "news geo cov")
                    self.selenium.type("keywords", "news, test")
                    self.selenium.type("sortorder", "35")
                    self.selenium.click("link=Today")
                    self.selenium.click("//img[@alt='Calendar']")
                    self.selenium.click("link=4")
                    self.selenium.click("discussion")
                    self.selenium.click("//div[@id='middle_port']/form/div[10]/span/a[1]")
                    self.selenium.click("//a[@id='calendarlink1']/img")
                    self.selenium.click("//div[@id='calendarin1']/table/tbody/tr[2]/td[5]/a")
                    self.selenium.click("topitem")
                    self.selenium.type("resourceurl", "http://www.eaudeweb.ro/")
                    self.selenium.type("source", "http://www.wikipedia.com/")
                    self.selenium.type("smallpicture", "/home/bogdan/Desktop/89366.png")
                    self.selenium.click("//input[@value='Submit']")

                    logger.info("NEWS item succesfully added...")

                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=My News")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("Add NEWS comment...")

                    self.selenium.click("link=Add comment")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("title", "My comment")
                    self.selenium.click("//input[@value='Submit']")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("NEWS comment succesfully added...")

                    self.selenium.click("link=Delete comment")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("NEWS comment succesfully deleted...")
                    logger.info("Attempt to acces NEWS edit page...")

                    self.selenium.click("link=Edit")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("title", "My News updated")

                    logger.info("NEWS edit page succesfully accessed...")

                    self.selenium.type("id=description", "This is a text updated")
                    self.selenium.type("coverage", "news geo cov updated")
                    self.selenium.type("keywords", "news, test, updated")
                    self.selenium.type("sortorder", "53")
                    self.selenium.click("//img[@alt='Calendar']")
                    self.selenium.click("link=6")
                    self.selenium.click("discussion")
                    self.selenium.click("//a[@id='calendarlink1']/img")
                    self.selenium.click("//div[@id='calendarin1']/table/tbody/tr[5]/td[4]/a")
                    self.selenium.type("smallpicture", "/home/bogdan/Desktop/logo.png")
                    self.selenium.type("bigpicture", "/home/bogdan/Desktop/no-pre.png")
                    self.selenium.click("saveProperties:method")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("NEWS item succesfully edited...")

                    self.selenium.click("link=Back to index")
                    self.selenium.wait_for_page_to_load("30000")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("//input[@name='id' and @value='my-news']")
                    self.selenium.click("deleteObjects:method")
                    self.failUnless(re.search(r"^Are you sure[\s\S]$", self.selenium.get_confirmation()))

                    logger.info("NEWS item succesfully deleted...")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")

                if(option == "HTML Document"):
                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")

                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")
                    print 1
                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("typetoadd")
                    if(loaded == False):
                        self.verificationErrors.append("Information page was"
                                                       " not loaded!"
                                                       " Test closed!")

                    logger.info("Try to select HTML DOCUMENT item...")

                    self.selenium.select("typetoadd", "index=" + str(select_options[option]))
                    self.assertTrue(self.selenium.is_something_selected("typetoadd"));
                    #self.assertEquals(option, self.selenium.get_selected_label("typetoadd"));
                    self.selenium.wait_for_page_to_load("15000")
                    if(self.selenium.is_element_present("id=lang") == False):
                        self.verificationErrors.append("Language element not"
                                                       " identified")

                    self.selenium.type("title", "My test HTML document")

                    logger.info("HTML DOCUMENT item selected... Add page accessed...")

                    self.selenium.type("id=description", "This is a text")
                    self.selenium.type("coverage", "HTML Doc geo cov")
                    self.selenium.type("keywords", "html,document,test")
                    self.selenium.type("sortorder", "135")
                    self.selenium.click("link=Today")
                    self.selenium.click("//img[@alt='Calendar']")
                    self.selenium.click("link=10")
                    self.selenium.click("discussion")
                    self.selenium.click("//input[@value='Submit']")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("HTML DOCUMENT succesfully added...")

                    self.selenium.click("link=My test HTML document")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("//div[@id='admin_this_folder']/a[2]/span")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("title", "My test HTML document updated")
                    self.selenium.type("id=description", "This is a text updated")
                    self.selenium.type("coverage", "HTML Doc geo cov updated")
                    self.selenium.type("keywords", "html,document,test, updated")
                    self.selenium.type("sortorder", "531")
                    self.selenium.click("link=Today")
                    self.selenium.click("//img[@alt='Calendar']")
                    self.selenium.click("link=19")
                    self.selenium.click("saveProperties:method")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("HTML DOCUMENT succesfully edited...")

                    self.selenium.click("link=Back to index")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("//div[@id='admin_this_folder']/a[2]/span")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Back to index")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("HTML DOCUMENT add comments...")

                    self.selenium.click("link=Add comment")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("title", "My Comment")
                    self.selenium.click("//input[@value='Submit']")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Add comment")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.type("title", "My Comment")
                    self.selenium.click("//input[@value='Submit']")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("HTML DOCUMENT comments added...")

                    self.selenium.click("link=Delete comment")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("link=Delete comment")
                    self.selenium.wait_for_page_to_load("30000")

                    logger.info("HTML DOCUMENT comments deleted...")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")
                    self.selenium.click("id")
                    self.selenium.click("deleteObjects:method")
                    self.failUnless(re.search(r"^Are you sure[\s\S]$", self.selenium.get_confirmation()))
                    logger.info("HTML DOCUMENT succesfully deleted...")

                    loaded = False
                    while(loaded == False):
                        loaded = self.selenium.is_element_present("link=Information")
                    self.selenium.click("link=Information")
                    self.selenium.wait_for_page_to_load("30000")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
