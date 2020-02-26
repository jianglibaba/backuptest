#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

def logw(log_file,data):
    logtime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    logline ='%s\t%s\n' %(logtime,data)
    f =open(log_file,'a')
    f.write(logline)
    f.flush()
    f.close()