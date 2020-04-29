import whois
import socket
from lib.output import *


class Whois():
        def __init__(self, target, ip):
                        self.target = target
                        self.name = "Whois"
                        self.ip = ip

        def search(self):
                test('Searching "%s" in Whois...' % (self.target))
                try:
                	if self.ip == 'nan' or self.ip == None:
                		self.ip = socket.gethostbyname(self.target)
                	
	                whoisdata = whois.whois(self.ip)
	                emaillist = whoisdata.get("emails")

	                email_list = []



	                if type(emaillist) == str:

	                    email_list.append(emaillist)

	                else:
	                    for _ in emaillist:
	                        if _ not in email_list and _.split('@')[0] not in ('"',"'"):
	                            email_list.append(_)
  


	                return email_list,self.ip;

                except:
                	warn('Could not fetch public IP of "%s" ...' % (self.target))

