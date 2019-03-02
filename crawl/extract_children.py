'''
Given a list of urls, retrieve the urls contained in the html pages.
Shibo Yao, sy372@njit.edu
Sep 18, 2018 
'''
from __future__ import print_function
from bs4 import BeautifulSoup
import urllib
import re
from time import sleep
import random
import numpy as np
import sys

parent = np.loadtxt("500urls.txt", dtype = 'str')
parent = np.unique(parent)

# run as, python fname.py delay rand

def urls_inUrl(url, token = "^https://", randomness = 3, delay = None):
    try:
        html_page = urllib.request.urlopen(url)
    except:
        print("HTTP Error")
        return 
    soup = BeautifulSoup(html_page, "lxml")

    result = ''
    count = 0
    for link in soup.findAll('a', attrs = {'href': re.compile(token)}):
        r = link.get('href')
        if token == "^/wiki/":
            r = "https://en.wikipedia.org"+r
        #print(r)
        result = result+r+'\n'
        count += 1
        
        if delay is not None:
            d = delay + random.expovariate(randomness)
            sleep(d)
            print("sleep %.4f s.." %d)

    return result, count



urls = ''
num_url = 0
for p in parent:
    print("Searching in ", p)
    r, num = urls_inUrl(p, token = "^/wiki/")
    print("Found %d chrildren" %num)
    urls = urls+p+'\n'+r
    num_url += num

    if (len(sys.argv)>1):
        d = float(sys.argv[1]) + random.expovariate(float(sys.argv[2])) # python fname.py delay rand
        print("sleep %f s..." %d)
        sleep(d)


print("In total %d children urls found"%num_url)
file = open("chrildren_urls.txt", "w")
file.write(urls)
file.close()


