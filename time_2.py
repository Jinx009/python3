#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import time

localtime = time.localtime(time.time())
print ('本地时间为 :', localtime)

#输出结果：
#本地时间为 : time.struct_time(tm_year=2017, tm_mon=6, tm_mday=27, tm_hour=15, tm_min=1, tm_sec=51, tm_wday=1, tm_yday=178, tm_isdst=0)
