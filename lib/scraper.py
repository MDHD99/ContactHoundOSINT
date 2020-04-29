from bs4 import BeautifulSoup
import requests
import re
from lib.output import *

class scraper():
    def __init__(self,target):
        self.target = target

    def scrape(self):
        email_list = []
        reg = re.compile(r'[\w\.-]+@[\w\.-]+')
        httpurl =  "http://"+self.target+"/"
        httpsurl = "https://"+self.target+"/"
        try:
            test('Searching "%s" HTTP Website...' % (self.target))
            
            result = requests.get(httpurl)
            
                

            if result.status_code == 200:
                 
                soup = BeautifulSoup(result.content,features="html.parser")

                try:

                    soupemails = soup.find_all('a', {'href': re.compile('\w+@\w+\.{1}\w+')})  # scrape data from "a" elements and filter only emails using regex
                    for i in range(0,len(soupemails)):
                        email = soup.find_all('a', {'href': re.compile('\w+@\w+\.{1}\w+')})[i].text
                        email_list.append(email)
                except:
                    try:
                        soupemails = soup.find_all('a', {'href': re.compile('\w+@\w+\.{1}\w+')})
                        for i in range(0,len(soupemails)):
                            email = soup.find_all('a', {'href': re.compile('\w+@\w+\.{1}\w+')})[i].text
                            email_list.append(email)
                    except:
                        raise ValueError('Nothing found in HTTP')
            else:
                raise ValueError('HTTP does not exist')

        except (requests.exceptions.RequestException,ValueError) as e:
            try:
                test('Searching "%s" HTTPS Website...' % (self.target))
                result = requests.get(httpsurl)
                if result.status_code == 200:

                    soup = BeautifulSoup(result.content,features="html.parser")
                    try:
                        soupemails = soup.find_all('a', {'href': re.compile('\w+@\w+\.{1}\w+')})  # scrape data from "a" elements and filter only emails using regex
                        for i in range(0,len(soupemails)):
                            email = soup.find_all('a', {'href': re.compile('\w+@\w+\.{1}\w+')})[i].text
                            email_list.append(email)
                    except:
                        try:
                            soupemails = soup.find_all('a', {'href': re.compile('\w+@\w+\.{1}\w+')})
                            for i in range(0,len(soupemails)):
                                email = soup.find_all('a', {'href': re.compile('\w+@\w+\.{1}\w+')})[i].text
                                email_list.append(email)
                        except:
                            raise NameError("Nothing found in HTTPS")
                else:
                    raise ValueError('HTTP does not exist')

            except requests.exceptions.RequestException as e:
                warn('"%s" Website was not found' % (self.target))

            except NameError:
                warn('No emails were found in "%s" website' % (self.target))
    
        return email_list






