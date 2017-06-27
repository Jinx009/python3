#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import time

localtime = time.asctime( time.localtime(time.time()) )
print('本地时间为 :', localtime)

#输出结果：
#本地时间为 : Tue Jun 27 15:03:32 2017
