import pandas as pd


def readCSV(file,type):
	if type == 1:
		domain_list = []
		df = pd.read_csv(file)
		domains = df["domain"].astype(str)

		for domain in domains:
			domain_list.append(domain)

		return domain_list

	elif type == 2:
		domain_list = []
		df = pd.read_csv(file)
		domains = df["domain"].astype(str)
		ip = df["ip"].astype(str)
		for cell in range(0,len(domains)):
			domainip = [domains[cell],ip[cell]]
			domain_list.append(domainip)

		return domain_list


	elif type == 3:
		domain_list = []
		df = pd.read_csv(file)
		domains = df["domain"].astype(str)
		ip = df["ip"].astype(str)
		emails = df["emails"].astype(str)
		for cell in range(0,len(domains)):
			domainip = [domains[cell],ip[cell],emails[cell]]
			domain_list.append(domainip)
		return domain_list


def writePANDAS(filename):

	file = pd.DataFrame()
	return file

def appendRow(pandas,domain,ip,email_list):
	data = {
    'domain':[domain], 
    'ip':[ip],
    'emails':[email_list]
}
	row = pd.DataFrame(data)

	pandas = pandas.append(row,ignore_index = True)


	return pandas


def outputCSV(file,filename):
	try:
		file.to_csv(filename)
	except:
		sys.exit(warn('Not a valid output file path'))

    










