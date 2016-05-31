import requests
from bs4 import *

url = 'https://www.rokomari.com/book/category/35/%E0%A6%85%E0%A6%A8%E0%A7%81%E0%A6%AC%E0%A6%BE%E0%A6%A6?page='
count=1
output=open("pasha_vai.txt","w")
while count<=136:
    url=url+str(count)
    count+=1
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup=BeautifulSoup(response.content)
    tags=soup('img')
    for tag in tags:
        link = tag.get('data-src')
        if not link is None:
            if link.startswith('http'):
                output.write(link)
                output.write('\n')
output.close()

