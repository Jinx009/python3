from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.800bank.com.cn/")
bsObj = BeautifulSoup(html, "lxml")
eList = bsObj.findAll("div")
for e in eList:
    print(e)
