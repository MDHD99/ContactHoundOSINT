#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email OSINT
# @url    : http://github.com/m4ll0k
# @author : Momo Outaadi (m4ll0k)

from lib.colors import *

class Banner:
	def banner(self):
		print("\n")
		print("""
 _____             _             _     _   _                       _ 
/  __ \           | |           | |   | | | |                     | |      / \_
| /  \/ ___  _ __ | |_ __ _  ___| |_  | |_| | ___  _   _ _ __   __| |     (    @\___
| |    / _ \| '_ \| __/ _` |/ __| __| |  _  |/ _ \| | | | '_ \ / _` |    /         O
| \__/\ (_) | | | | || (_| | (__| |_  | | | | (_) | |_| | | | | (_| |   /   (_____/    
 \____/\___/|_| |_|\__\__,_|\___|\__| \_| |_/\___/ \__,_|_| |_|\__,_|  /_____/   U                                                           
   
   
** Email gathering and automatic email sending tool
** Author: Mohamad Hammoud a.k.a MDHD
** DISCLAMER This tool is based on infoga developed by m4ll0k. 
** DISCLAMER This tool is aimed for ethical information security usage.
** Version ALPHA

		        """)

	def usage(self,_exit_=False):
		self.banner()
		print("""

		
 Usage: CHound.py [options]
 Options:
 -h,            --help                    show this help message and exit
 --emailgather                            use email gathering
 --emailsend                              use email sending  


 Email Gathering:

 -d,            --domain                  specify domain
 -f,            --file                    specify domain or ip input file
 -t,            --type                    specify input file type:
 												1 => Only domains column
 												2 => Domain and ip
 												3 => Domain ip and emails   
 --ip,                                    specify IPV4 address
 -o,            --output                  specify output file('.csv or .json only')
 --ot                                     specify output type:  0  => List of all found emails
																1  => Most accurate email    
 Example:
		 CHound.py --emailgather -d google.com --ot 0 
		 CHound.py --emailgather -D domains.csv -o results.csv --ot 1 

 Email Sending:  

 -h             --html                    input file with dynamic html
 -f             --file                    input file (csv)
 -e             --email                   sender email(if not used would result to default tool email) 
 -p             --password                sender password
 -s             --subject                 email subject     

	 """)

		if _exit_: exit(0)
	def output(self):
		print("""
		
     |\_/|                  
     | @ @   Woof! 
     |   <>              _  
     |  _/\------____ ((| |))
     |               `--' |   
 ____|_       ___|   |___.' 
/_/_____/____/_______|



**List of emails fetched
		

				        """)
