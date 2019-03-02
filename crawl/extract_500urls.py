'''
Gather wiki page urls for all S&P500 companies. 
Some websites are very sensitive to spiders, e.g. Bloomberg and SeekingAlpha. While wiki is relatively friendly. 
Shibo Yao, espoyao@gmail.com
Sep 18, 2018
'''
from __future__ import print_function
from bs4 import BeautifulSoup
import urllib
import re
from time import sleep
import random

start = '3M'
mid = ['Aon_plc', 'Aptiv_Plc', 'IHS_Markit', 'Medtronic_plc', 'Mylan_N.V.', 'Schlumberger_Ltd.', 'TechnipFMC'] ## update! Sep 18, 2018
end = 'Zoetis'

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
#url = 'http://saintpaulhistorical.com/items/show/354' error page for test
#url = 'https://en.wikipedia.org/wiki/Apple_Inc.'
#url = 'https://en.wikipedia.org/wiki/3M'
#url = 'https://www.cnbc.com/quotes/?symbol=AAPL'
#url = "https://finance.yahoo.com/quote/AMD/news?p=AMD"
#url = "https://seekingalpha.com/symbol/AMD?analysis_tab=focus&news_tab=press-release"

def urls_inUrl(url, token = "^https://", randomness = 3, delay = None):
    try:
        html_page = urllib.request.urlopen(url)
    except:
        print("HTTP Error")
        return 
    soup = BeautifulSoup(html_page)

    result = []
    for link in soup.findAll('a', attrs = {'href': re.compile(token)}):
        r = link.get('href')
        print(r)
        result.append(r)
        
        if delay is not None:
            d = delay + random.expovariate(randomness)
            sleep(d)
            print("sleep %.4f s.." %d)

    return result



candidates = urls_inUrl(url, token = "^/wiki/", randomness = 3, delay = None)



def find500Urls(urls, start, end, mid = None):
    if mid is None:
        cand = urls[urls.index("/wiki/"+start):urls.index("/wiki/"+end)+1:2]
    else :
        cand = urls[urls.index("/wiki/"+start):urls.index("/wiki/"+mid[0])+1:2]
        for i in range(len(mid)-1):
            cand = cand+urls[urls.index("/wiki/"+mid[i])+3:urls.index("/wiki/"+mid[i+1])+1:2]
        cand = cand+urls[urls.index("/wiki/"+mid[len(mid)-1])+3:urls.index("/wiki/"+end)+1:2] 

    return ["https://en.wikipedia.org"+c for c in cand]

lis = find500Urls(candidates, start, end, mid)
print(lis)
print(len(lis))

string = ''
for l in lis:
    string = string+l+'\n'

file = open("500urls.txt","w")  
file.write(string)
file.close() 



