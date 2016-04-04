import datetime
import random
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

random.seed(datetime.datetime.now())
link_count = set()
# def getLinks(articleURL = None):
#     # read URL
#     global pages
#     try:
#         html = urlopen('https://en.wikipedia.org'+articleURL)
#     except HTTPError as e:
#         print('URL not found')
#         return -1
#     # create Beautiful Soup object
#     try:
#         bsObj = BeautifulSoup(html, 'html.parser') #use html parser
#     except:
#         print('Cant create BS object \o.O/')
#         return -1
#     # return bsObj.find('div', {'id':'bodyContent'}).findAll('a',
#     #             href=re.compile('^(/wiki/)((?!:).)*$'))
#     for link in bsObj.findAll('a', href=re.compile('^(/wiki)((?!:).)*$')):
#     # for link in bsObj.findAll('a', href=re.compile('^(https://deshmukhsuraj)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 newPage = link.attrs['href']
#                 print(': ',newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#
#
# def articles():
#     links = getLinks('/wiki/NASA')
#     links = getLinks()
#     counter = 1
#     while len(links)>0:
#         newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#         print(counter, ': ',newArticle)
#         links = getLinks(newArticle)


# articles()

####################################################################

'''
collect all internal and external links on the site
'''

link_count = 0
# Retrieve a list of all external links on the page
def getInternalLinks(bsObj, includeDomain):
    print('getInternalLinks')
    internalLinks = []
    for link in bsObj.findAll('a', href=re.compile(
                            '^(/|.*'+includeDomain+ ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# Retrieve a list of all external links on the page
def getExternalLinks(bsObj, excludeDomain):
    externalLinks = []
    for link in bsObj.findAll('a', href=re.compile(
                            '^(http|https|www)((?!'+excludeDomain+ ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitURL(URL):
    print('splitURL')
    addressParts = []
    # if 'https://' in URL:
    addressParts = URL.replace('https://','').replace('http://','').split('/')
    # else:
    #     addressParts = URL.replace('http://','').split('/')
    return addressParts


def getAllLinks(siteURL):
    global link_count
    allInternalLinks = set()
    allExternalLinks = set()
    print('allLinks')
    try:
        html = urlopen(siteURL)
    except HTTPError as e:
        print(e)
    try:
        bsObj = BeautifulSoup(html, 'html.parser')
    except:
        print('Cant create BS object \o.O/')
    internalLinks = getInternalLinks(bsObj, splitURL(siteURL)[0])
    externalLikns = getExternalLinks(bsObj, splitURL(siteURL)[0])


    for link in allInternalLinks:
        if link not in internalLinks:
            print(link_count, 'Internal: ', link)
            allInternalLinks.add(link)
            link_count += 1
            getAllLinks(link)

    for link in externalLikns:
        if link not in allExternalLinks:
            print(link_count, 'External: ', link)
            link_count+=1
            allExternalLinks.add(link)


getAllLinks('http://oreilly.com')