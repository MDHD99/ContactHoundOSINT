import whois
import socket
from lib.output import *
from lib.scraper import *


class Soup():
        def __init__(self, target):
                        self.target = target
                        self.name = "Soup"

        def search(self):
            if self.target != "nan":
                email_list = []
                info('Sniffing in "%s" Homepage'% (self.target))
                emaillist = scraper(self.target).scrape()
                for _ in emaillist:
                    if _ not in email_list and _.split('@')[0] not in ('"',"'"):
                        email_list.append(_)
                return email_list
            else:
                warn("No domain to scrape")


        def strip(self,domain):
            try:
                strippeddomain = get_fld(domain, fix_protocol=True)
                return strippeddomain
            except:
                warn("Please Enter a valid domain")
                exit(0)
