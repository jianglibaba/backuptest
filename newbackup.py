#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 备份程序2019.5.15

import zipfile,os,bakuplog
from ftplib import FTP
#第一步：压缩文件
file ='E:\\kingdeeDataBK'
bakfile ='E:\\kingdeezip\\kingdeebk.zip'
log_file ='bakuplog.txt'
dataz ='压缩了备份文件'

os.remove(bakfile)  #1，删除原压缩文件

with zipfile.ZipFile(bakfile,'w') as z:     #2，压缩文件
    for i in os.walk(file):
        for n in i[2]:
            z.write(''.join((i[0],'\\',n)))

if not os.path.exists(log_file) :   #3，记录日志
    f =open(log_file, 'w')
    f.write('备份日志：\n')
    f.flush()
    f.close()
bakuplog.logw(log_file,dataz)

#第二步：上传压缩文件
host ='192.168.0.13'
port =21
usename ='ds'
password ='hfDSftp'
ftp =FTP()
ftppath ='kingdeebak'
dataf ='把压缩文件上传了ftp服务器'

def ftpconnect(ftp,host,port,usename,password):
    try:
        ftp.connect(host,port)
    except:
        raise IOError ('ftp没连上！')
    try:
        ftp.login(usename,password)
    except:
        raise IOError('ftp的账号密码不对！')
    else:
        print('********** ftp连接成功！***********')
        return ftp

def upfile(ftp,ftppath,bakfile):
    try:
        bufsize = 1024
        fp = open(bakfile,'rb')
        cmd ='STOR %s/kingdeebk.zip' %ftppath   #STOR是FTP命令，是复制文件到服务器上
        ftp.storbinary(cmd,fp,bufsize)
        print('上传成功！')
    except:
        print('上传失败！')

def ftpclose(ftp):
    ftp.quit()
    print('********** 退出ftp ***********')

ftpconnect(ftp,host,port,usename,password)    #连接并登录ftp
upfile(ftp,ftppath,bakfile)    #上传文件到ftp指定的文件夹
ftpclose(ftp)   #退出ftp
bakuplog.logw(log_file,dataf)   #记录日志