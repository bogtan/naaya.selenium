import sys
import logging
import optparse

class NySeleniumConfig:
    def __init__(self, options):
        self.data = {}
        
        self.ParseArguments(options)

    def ParseArguments(self, options):
        options.add_option('--site', '-s', default='http://localhost/')
        options.add_option('--port', '-p', default='8080')
        options.add_option('--browsers', '-b', default="all")
        options.add_option('--user', '-u', default="admin")
        options.add_option('--password', '-P', default="admin")
        parsed_options, arguments = options.parse_args()

        browsers = ['firefox', 'chrome', 'ie', 'all']
        param_browsers = parsed_options.browsers.replace("=", "")
        param_browsers = param_browsers.split(" ")

        print "Browsers: "
        for browser in param_browsers:
            print "- " + browser

        self.data['site'] = parsed_options.site
        self.data['port'] = parsed_options.port
        self.data['browsers'] = parsed_options.browsers
        self.data['user'] = parsed_options.user
        self.data['password'] = parsed_options.password

        return parsed_options
