import datetime
import random
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

random.seed(datetime.datetime.now())
pages = set()
def getLinks(articleURL = None):
    # read URL
    global pages
    try:
        # html = urlopen('https://en.wikipedia.org'+articleURL)
        html = urlopen('https://deshmukhsuraj.wordpress.com/2015/03/08/anonymous-web-scraping-using-python-and-tor/')
    except HTTPError as e:
        print('URL not found')
        return -1
    # create Beautiful Soup object
    try:
        bsObj = BeautifulSoup(html, 'html.parser') #use html parser
    except:
        print('Cant create BS object \o.O/')
        return -1
    # return bsObj.find('div', {'id':'bodyContent'}).findAll('a',
    #             href=re.compile('^(/wiki/)((?!:).)*$'))
    # for link in bsObj.findAll('a', href=re.compile('^(/wiki)((?!:).)*$')):
    for link in bsObj.findAll('a', href=re.compile('^(https://deshmukhsuraj)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(': ',newPage)
                pages.add(newPage)
                getLinks(newPage)


# def articles():
#     # links = getLinks('/wiki/Kevin_Bacon')
#     links = getLinks()
#     counter = 1
#     while len(links)>0:
#         newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#         print(counter, ': ',newArticle)
#         links = getLinks(newArticle)
#

# getLinks()

def splitLink(address):
    addressParts = address.replace('http://', '').split('/')
    return addressParts

print(splitLink('http://oreilly.com/'))