#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : chound - Email OSINT
# @url    : http://github.com/m4ll0k
# @author : Momo Outaadi (m4ll0k)

import sys
import json
import getopt
# chound.lib
from lib.pandas import *
from lib.check import *
from lib.output import *
from lib.banner import Banner
# chound.recon
from recon.ask import *
from recon.baidu import *
from recon.bing import *
from recon.pgp import *
from recon.yahoo import *
from recon.dogpile import *
from recon.exalead import *
from recon.google import *
from recon.yandex import *
from recon.whois import *
from recon.soup import *
from recon.mailtester import *
from lib.output import PPrint
from tld import get_fld

class chound(object):
	""" chound """
	def __init__(self):
		self.verbose = 1
		self.domain = None
		self.domain_list = None
		self.breach = False
		self.listEmail = []
		self.output = None
		self.fileName = None
		self.input = None
		self.filetype = 1
		self.ip = None

	def search(self,module):
		try:
			modName = module.name
			if modName != 'Whois':
				emails = module.search()
			else:
				emails,ip = module.search()
				self.ip = ip	
			if emails != ([] or None):
				for email in emails:
					if email not in self.listEmail:
						self.listEmail.append(email)
				if self.verbose in (1,2,3):
					info('Found %s emails in %s'%(len(emails),
						module.__class__.__name__))
		except TypeError:
			info("Skippig Whois")

	def engine(self,target,engine):
		engine_list = [ Soup(target),Yandex(target),Ask(target),Baidu(target),Bing(target),Dogpile(target),
						Exalead(target),Google(target),Yahoo(target),Whois(target,self.ip)
						]
		if engine == 'all':
			if target!='nan':
				for e in engine_list:
					self.search(e)
			else: self.search(Whois(target,self.ip))

			if len(self.listEmail)<5 and target != 'nan':
				root = get_fld(target, fix_protocol=True)
				if root != target:
					warn("Not enough emails were found, will try again with different tactics")
					target = root
					self.engine(target,'all')


	def main(self):
		if len(sys.argv) <= 2:Banner().usage(True)
		try:
			opts,args = getopt.getopt(sys.argv[1:],'d:t:f:i:v:o:hb',
				['domain=','info=','file=','type=','breach','verbose=','help','output='])
		except Exception as e:
			Banner().usage(True)
		Banner().banner()
		for o,a in opts:
			if o in ('-d','--domain'):self.domain=checkTarget(a)
			elif o in ('-f','--file'):self.input=checkFile(a)
			if o in ('-t','--type'):self.filetype =checkType(a)
			if o in ('-v','--verbose'):self.verbose=checkVerbose(a)
			if o in ('-b','--breach'):self.breach=True
			if o in ('-o','--o'):
				if a != '':
		
					self.fileName = checkPath(a)
					self.output = writePANDAS(a)

				else:
					Banner().usage(True)

				
			if o in ('-h','--help'):Banner().usage(True)

			if((self.domain != None and self.input != None) or (self.domain == None and self.input == None)):
				Banner().usage(True)



		### start ####

		if(self.input == None):
			if self.domain != ('' or None):
				plus('Searching for: %s'%self.domain)
				self.engine(self.domain,'all')

			if self.listEmail == [] or self.listEmail == None:
				sys.exit(warn('Not found emails... :('))
			
			else:
				Banner().output()
				info("List of found emails is...")
				for email in self.listEmail:
					plus(email)
		

			self.listEmail = []



		elif(self.input != None):
			if self.filetype == 1:
				self.domain_list = readCSV(self.input,self.filetype)
				for domain in self.domain_list:			  
					self.domain = domain
					if self.domain != ('' or None):
						plus('Searching for: %s'%self.domain)
						self.engine(self.domain,'all')

					if self.listEmail == [] or self.listEmail == None:
						warn('No Emails were found...')
						 
					else:
						Banner().output()
						info("List of found emails is...")
						for email in self.listEmail:
							plus(email)

						
					if type(self.output) != 'NoneType':
						self.listEmail = ','.join(self.listEmail)
						self.output = appendRow(self.output,self.domain, self.ip, self.listEmail)


					self.listEmail = []

					print("""	




						  """)
				if type(self.output) != 'NoneType':
					outputCSV(self.output,self.fileName)


			elif self.filetype == 2:
				self.domain_list = readCSV(self.input,self.filetype)
				for i in range(0,len(self.domain_list)):			  
					self.domain = self.domain_list[i][0]
					self.ip = self.domain_list[i][1]
					if self.domain != ('' or None):
						plus('Searching for: %s'%self.domain)

						self.engine(self.domain,'all')


					if self.listEmail == [] or self.listEmail == None:
						warn('No Emails were found...') 
				
					else:
						Banner().output()
						info("List of found emails is...")
						for email in self.listEmail:
							plus(email)

						
					if type(self.output) != 'NoneType':
						self.listEmail = ','.join(self.listEmail)
						self.output = appendRow(self.output,self.domain, self.ip, self.listEmail)

					self.listEmail = []

					print("""	




						  """)
				if type(self.output) != 'NoneType':
					outputCSV(self.output,self.fileName)


			if self.filetype == 3:
				self.domain_list = readCSV(self.input,self.filetype)
				for i in range(0,len(self.domain_list)):			  
					self.domain = self.domain_list[i][0]
					self.ip = self.domain_list[i][1]
					self.listEmail = self.domain_list[i][2]
					emailsFound = True
					if self.listEmail == 'nan':
						self.listEmail = []
						emailsFound = False
						if self.domain != ('' or None):
							plus('Searching for: %s'%self.domain)

							self.engine(self.domain,'all')

							if self.listEmail == [] or self.listEmail == None:
								warn('No Emails were found...') 
						
							else:
								Banner().output()
								info("List of found emails is...")
								for email in self.listEmail:
									plus(email)
							print("""	




						  		 """)

						
					if type(self.output) != 'NoneType':
						if emailsFound == False:
							self.listEmail = ','.join(self.listEmail)
						self.output = appendRow(self.output,self.domain, self.ip, self.listEmail)

					self.listEmail = []

					
				if type(self.output) != 'NoneType':
					outputCSV(self.output,self.fileName)


		# end
if __name__ == "__main__":
	try:
		chound().main()
	except KeyboardInterrupt as e:
		sys.exit(warn('Exiting...'))