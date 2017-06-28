from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.qq.com/")
bsObj = BeautifulSoup(html, "lxml")
imgList = bsObj.findAll("img")
for img in imgList:
    print(img)
