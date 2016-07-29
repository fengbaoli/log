# -*- coding:utf-8 -*-
__author__ = 'blfeng'
import  sys,os
sys.path.append(os.getcwd()+'/lib')
import os
from log import  Collectlog
from  Sendlog import  Sendlog
import time
logpath = "/var/log"
configfile = "log.conf"
ip = '192.168.17.134'
port = 8000


#初始化配置文件
Collectlog().getfile_count(configfile,logpath)
#开始采集
while True:
    #读取上次采集的行
    cfile = open(configfile)
    for t in cfile.readlines():
        contents = t.strip().split(':')
        filepath=contents[0]
        filename=contents[1]
        old_counts =contents[2]
    #目前文件行数
        now_counts = len(open(filepath+"/"+filename,'rU').readlines())
        Collectlog().gencounts(configfile,filepath,filename,counts=now_counts)
        #如果有新日志发送新日志
        if int(old_counts) < now_counts:
            sfilename = filepath+"/"+filename
            Sendlog().slog(ip=ip,port=port,filename=sfilename)
            #更新配置文件
            Collectlog().gencounts(configfile,filepath,filename,counts=now_counts)
        else:
            pass
    os.remove(configfile)
    obuff = []
    for ln in open('tmpconf.txt'):
        if ln in obuff:
            continue
    obuff.append(ln)
    with open(configfile, 'w') as handle:
         handle.writelines(obuff)
    os.remove('tmpconf.txt')
