#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。
import time;  # 引入time模块

ticks = time.time()
print('time:', ticks)

#输出结果：
#time: 1498547087.386078
