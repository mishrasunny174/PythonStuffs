#!/usr/bin/env python2
from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.programmableweb.com/apis/directory'
BASE_URL = 'https://www.programmableweb.com'

def getSoupObject(url):
	print "[*] connecting to {}".format(url)
	response = requests.get(url)
	if response.status_code == 200:
	    return BeautifulSoup(response.text,'html.parser')
	else:
		print('ERROR: unable to connect to the server')
		exit(1)

def getAllAPIs(url):
	api_dict = {}
	count = 0
	soup = getSoupObject(url)
	while True:
		api_table = soup.find('table',{'class':'views-table cols-4 table'})
		api_rows = api_table.find_all('tr')
		api_rows = api_rows[1:]
		for api in api_rows:
			name = api.find('td',{'class':'views-field-title'}).find('a').text.strip()
			url = BASE_URL+api.find('td',{'class':'views-field-title'}).find('a')['href'].strip()
			description = api.find('td',{'class':'views-field-field-api-description'}).text.strip()
			category = api.find('td',{'class':'views-field-field-article-primary-category'})
			category = category.text.strip() if category else 'N/A'
			api_dict[count] = [name,url,description,category]
			count = count + 1
		print "[+] current total count {}".format(count)
		next_url = soup.find('li',{'class':'pager-last'})
		if next_url:
			soup = getSoupObject(BASE_URL+next_url.find('a')['href'])
		else:
			break
	print "[+] total api's = {}".format(count)
	return api_dict
	    

def exportToCSv(api_dict, filename):
    df = pd.DataFrame.from_dict(api_dict, orient='index', columns=['name', 'url', 'description', 'category'])
    print df.head()
    df.to_csv(filename, encoding='utf-16')

def main():
    url = URL
    api_dict = getAllAPIs(url)
    exportToCSv(api_dict,'apiList.csv')

if __name__ == '__main__':
    main()
