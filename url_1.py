#!/usr/local/bin/python3
# -*- coding: gb2312 -*-
from urllib.request import urlopen

qq = urlopen('http://www.baidu.com')
print('http header:/n', qq.info())
print('http status:', qq.getcode())
print('url:', qq.geturl())
for line in qq:  # 就像在操作本地文件
    print(line.decode('utf-8')),
qq.close()



