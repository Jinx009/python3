import urllib.request
import re
import time

url = 'http://image.baidu.com'
req = urllib.request.Request(url, headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})


def get_html():
    page = urllib.request.urlopen(req)
    _html = page.read()
    print(_html.decode('utf-8'))
    return _html


def get_img(_html):
    reg = 'src="([^ >]+\.(?:jpeg|jpg))"'
    img_re = re.compile(reg)
    _html = _html.decode('utf-8')
    img_list = re.findall(img_re, _html)
    _time = time.time()
    x = 0
    for img_url in img_list:
        #随机生成文件名称
        _time = _time + x
        #保存文件到指定文件夹
        urllib.request.urlretrieve(img_url, '/Users/jinx/Downloads/img/%s.jpg' % _time)
        x += 1
    return x


html = get_html()
print(get_img(html))

