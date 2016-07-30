# -*- coding:utf-8 -*-
__author__ = 'blfeng'
import  sys,os
sys.path.append(os.getcwd()+'/lib')
import os
from log import  Collectlog
import time,struct,linecache
from socket import *
logpath = "/var/log"
configfile = "log.conf"
ip = '192.168.16.128'
port = 8000


#初始化配置文件
Collectlog().getfile_count(configfile,logpath)
#开始采集
while True:
    cfile = open(configfile)
    for t in cfile.readlines():
        #建立链接
        ADDR = (ip,port)
        BUFSIZE = 1024
        FILEINFO_SIZE=struct.calcsize('128s32sI8s')
        sendSock = socket(AF_INET,SOCK_STREAM,0)
        sendSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        sendSock.connect(ADDR) 
        contents = t.strip().split(':')
        filepath_name=contents[0]
        filename=contents[1]
        old_counts =int(contents[2])
    #目前文件行数
        now_counts = len(open(filepath_name,'rU').readlines()) 
    #发送数据
        if old_counts < now_counts:
            fhead=struct.pack('128s11I',filepath_name,0,0,0,0,0,0,0,0,os.stat(filepath_name).st_size,0,0)
            sendSock.send(fhead)
            while old_counts <= now_counts:
                tmpfiledata = linecache.getline(filepath_name,old_counts)
                filedata =  ''.join(tmpfiledata)
                sendSock.send(filedata)
                linecache.clearcache()
                old_counts = old_counts + 1
        print "文件传送完毕，正在断开连接..."
        sendSock.close()
        time.sleep(10)
        print "连接已关闭..."
        time.sleep(1)
        print filename+"更新配置文件"
        #更新配置文件




        print filename+"配置文件更新完毕"
    
