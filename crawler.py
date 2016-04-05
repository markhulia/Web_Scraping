import datetime
import os
import random
import json
import re
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup

random.seed(datetime.datetime.now())
# link_count = set()
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
# '''
#
# link_count = 0
# # Retrieve a list of all external links on the page
# def getInternalLinks(bsObj, includeDomain):
#     print('getInternalLinks')
#     internalLinks = []
#     for link in bsObj.findAll('a', href=re.compile(
#                             '^(/|.*'+includeDomain+ ')')):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in internalLinks:
#                 internalLinks.append(link.attrs['href'])
#     return internalLinks
#
# # Retrieve a list of all external links on the page
# def getExternalLinks(bsObj, excludeDomain):
#     externalLinks = []
#     for link in bsObj.findAll('a', href=re.compile(
#                             '^(http|https|www)((?!'+excludeDomain+ ').)*$')):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in externalLinks:
#                 externalLinks.append(link.attrs['href'])
#     return externalLinks
#
#
# def splitURL(URL):
#     print('splitURL')
#     addressParts = []
#     # if 'https://' in URL:
#     addressParts = URL.replace('https://','').replace('http://','').split('/')
#     # else:
#     #     addressParts = URL.replace('http://','').split('/')
#     return addressParts
#
#
# def getAllLinks(siteURL):
#     global link_count
#     allInternalLinks = set()
#     allExternalLinks = set()
#     print('allLinks')
#     try:
#         html = urlopen(siteURL)
#     except HTTPError as e:
#         print(e)
#     try:
#         bsObj = BeautifulSoup(html, 'html.parser')
#     except:
#         print('Cant create BS object \o.O/')
#     internalLinks = getInternalLinks(bsObj, splitURL(siteURL)[0])
#     externalLikns = getExternalLinks(bsObj, splitURL(siteURL)[0])
#
#
#     for link in allInternalLinks:
#         if link not in internalLinks:
#             print(link_count, 'Internal: ', link)
#             allInternalLinks.add(link)
#             link_count += 1
#             getAllLinks(link)
#
#     for link in externalLikns:
#         if link not in allExternalLinks:
#             print(link_count, 'External: ', link)
#             link_count+=1
#             allExternalLinks.add(link)
#
#
# getAllLinks('http://oreilly.com')

'''
Post to twitter
'''
# from twitter import *
#
# t = Twitter(auth=OAuth('365075472-MlwOpCHnTTiw3AkplRHWM0FziAlPkOTe28F76hLd',
#                        'j4yHB6SV0enxTwGtMNbpXZ5Le9ago40Gi7cVyPcsbQWD3',
#                        'jjtbX7A5qet5oGQlo7hiJW9lp',
#                        '9FMIlsRkRtx0wcJocJSQxc42uS1z3UxWpgEC1qj61xkI7RKtMi'))
# pythonTweets = t.statuses.update(status='updated with my #pythoncrawler')
# # pythonTweets = t.search.tweets(q='#python')
# print(pythonTweets)



# def countryCode(ipAddress):
#     response = urlopen("http://geoip.nekudo.com/api/"+ipAddress).read().decode('utf-8')
#     responseJson = json.loads(response)
#     return responseJson.get('country').get('name')
#
# print(countryCode('50.78.253.58'))



'''
gets IP addresses of edits on wikipedia page from revision history
'''
# https://en.wikipedia.org/wiki/Python_(programming_language)
# random.seed(datetime.datetime.now())
# def getLinks(URL):
#     try:
#         html = urlopen('https://en.wikipedia.org/'+URL)
#     except HTTPError as e:
#         print('err', e)
#     try:
#         bsObj = BeautifulSoup(html, 'html.parser')
#     except:
#         print('Cant create BS object \o.O/')
#     return bsObj.find('div', {'id':'bodyContent'}).\
#         findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
#
#
# def getHistoryIP(pageURL='Dynamic_typing'):
#     pageURL = pageURL.replace('/wiki/','')
#     historyURL = 'https://en.wikipedia.org/w/index.php?title=' \
#                  +pageURL+'&action=history'
#     print('History URL: ', historyURL)
#     try:
#         html = urlopen(historyURL)
#     except HTTPError as e:
#         print('err', e)
#     try:
#         bsObj = BeautifulSoup(html, 'html.parser')
#     except:
#         print('Cant create BS object \o.O/')
#     ipAddresses = bsObj.findAll('a', {'class':'mw-anonuserlink'})
#     addressList = set()
#     for ipAddress in ipAddresses:
#         addressList.add(ipAddress.get_text())
#     return addressList
#
# # Display country and city name
# def findCountry(IP):
#     try:
#         response = urlopen("http://geoip.nekudo.com/api/"+IP).read().decode('utf-8')
#     except HTTPError as e:
#         print('err', e)
#     responseJson = json.loads(response)
#     try:
#         country = responseJson.get('country').get('name')
#     except AttributeError as e:
#         country = 'Unkown'
#     try:
#         city = responseJson.get('city')
#     except AttributeError as e:
#         city = 'Unkown'
#
#     return country, city
#
#
# links = getLinks('wiki/Python_(programming_language)')
# while(len(links)>0):
#     for link in links:
#         print('--------------')
#         historyIPs = getHistoryIP(link.attrs['href'])
#         for historyIP in historyIPs:
#             print(historyIP, findCountry(historyIP))
#     # newLink = links[random.randint(0, len(links)-1)].attrs['href']
#     # links = getLinks(newLink)
''''''

'''
Scrape for images and download them
'''
# downloadDirectory = 'downloaded'
# baseUrl = 'http://pythonscraping.com'
#
#
#
# def getAbsoluteURL(baseUrl, source):
#     if source.startswith('http://www.'):
#         url = 'http://'+source[11:]
#     elif source.startswith('http://'):
#         url = source
#     elif source.startswith('www.'):
#         url = 'http://'+source[4:]
#     else:
#         url = 'http://'+source
#     if baseUrl not in url:
#         return None
#     return url
#
#
# def getDownloadPath(baseUrl, fileUrl, downloadDirectory):
#     path = fileUrl.replace('www.','')
#     path = path.replace(baseUrl,'')
#     path = downloadDirectory+path
#     directory = os.path.dirname(path)
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     return path
#
#
# html = urlopen(baseUrl)
# bsObj = BeautifulSoup(html, 'html.parser')
# downloadList = bsObj.findAll(src=True)
#
# for file in downloadList:
#     # print(file['src'])
#     fileUrl = getAbsoluteURL(baseUrl, file['src'])
#     if fileUrl is not None:
#         print(fileUrl)
#
#
# urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))


