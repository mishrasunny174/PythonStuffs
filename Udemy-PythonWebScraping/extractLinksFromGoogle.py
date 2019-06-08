#!/usr/bin/env python2 
from bs4 import BeautifulSoup
import requests
import sys

baseURL = 'https://www.google.com/?q='


def getLinks(keyword):
    # result is inside r class div a tag extract that
    soup = getSoupObject(keyword)
    links = soup.find_all('a')
    return links


def getSoupObject(keyword):
    return BeautifulSoup(search(keyword),'html.parser')

def search(keyword):
    url = baseURL+keyword
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("[!] unable to connect to server")
        exit(2)

def main():
    if len(sys.argv) != 2:
        print("usage: {} <Keyword>".format(sys.argv[0]))
        exit(1)
    else:
        links = getLinks(sys.argv[1])
        print("Search result links are: ")
        for link in links:
            url = link['href']
            if 'setprefs' in url:
                print(url)
            else:
                pass

if __name__ == "__main__":
    main()
