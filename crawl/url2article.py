'''
Given a list of urls, retrieve articles contained in html files. 
Shibo Yao, sy372@njit.edu
Sep 18, 2018
'''
#import string
import numpy as np
from newspaper import Article
#import sys
from time import sleep
import random

with open("children.txt", 'rb') as f:
    urls = np.loadtxt(f, dtype='str')
print("In total %d urls" %len(urls))
urls = np.unique(urls)
l = len(urls)
print("In total %d urls after removing duplicates" %l)

with open("raw.txt", 'w') as f:
    f.write("")
with open("log_download.txt", 'w') as f:
    f.write("")
# run as, python fname.py >> log_download.txt
#table = str.maketrans(string.punctuation, " "*len(string.punctuation))


delay = 1
rand = 2
maxi = l
step_show = 100
step_save = 1000

s = ''
log = ''
count = 0
num_article = 0
for url in urls[:maxi]:
    count += 1
    try :
        a = Article(url)
        a.download()
        a.parse()
        text = a.text
        #print(text)
        #txt = text.translate(table)
        #print(text.translate(table))
        s = s + text
        num_article += 1
        log = log+'cross | '+url+'\n'
        print("cross | ", url)
    except:
        log = log+'wall | '+url+'\n'
        print("wall | ", url)
        pass
    '''
    if len(sys.argv)>1:
        #d = float(sys.argv[1]) + random.expovariate(float(sys.argv[2]))
        d = delay + random.expovariate(rand)
        print("Sleep %.2f s..." %d)
        sleep(d)
    '''
    d = delay + random.expovariate(rand)
    print("Sleep %.2f s..." %d)
    sleep(d)

    if (count%step_show == 0):
        print("%d/%d requested"%(count,l))
        print("%d/%d retrieved\n"%(num_article,l))    

  
    if (num_article%step_save == 0 or count == maxi):
        with open("raw.txt", 'a') as f:
            f.write(s)
        s = ''
            
        with open("log_download.txt", 'a') as f:
            f.write(log)
        log = ''
        print("%d articles saved\n" %num_article)


'''
print("In total %d/%d articles retrieved"%(num_article,l))
file = open("raw.txt", "w")
file.write(s)
file.close()
'''

