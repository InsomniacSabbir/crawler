import urllib
from bs4 import *
import sys
import os
import re
reload(sys)
sys.setdefaultencoding('utf-8')
url="https://www.rokomari.com/book/category/35/%E0%A6%85%E0%A6%A8%E0%A7%81%E0%A6%AC%E0%A6%BE%E0%A6%A6"
html=urllib.urlopen(url)
soup=BeautifulSoup(html.read())
tags=soup("img")
for tag in tags:
    print tag.get("href")
#directory=os.getcwd()
#def process(f,fpath):
#    url = r""+fpath
#    page = open(url)
#    path =fpath.split("latin_text_lacus_curtius")
#    path=path[0]+"latin_text_lacus_curtius/plain"+path[1]
#    pa=path.split("/")
#    length=len(pa)
#    print length
#    fp=""
#    for p in pa:
#        if(length<2):
#            continue
#        length-=1
       # fp+=p+"/"
#    print fp
#    path=path.split(".")
#    path=path[0]
#    path=path+".txt"
#    if not os.path.exists(fp):
#        os.makedirs(fp)
#    print path
#    soup = BeautifulSoup(page.read())
#    tags=soup.findAll("body")
#    output = open(''+path,'a+')
#    for tag in tags:
#        print tag.get_text()
#        output.write(tag.get_text())
#    output.close()
#
#for root, dirs, files in os.walk(directory):
#    for f in files:
#        if str(f).endswith('.htm'):
#            fpath = root+"/"+str(f)
#            process(f,fpath)
