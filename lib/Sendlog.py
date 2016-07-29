# -*- coding:utf-8 -*-
__author__ = 'blfeng'

from socket import *
import os
import struct
import time
class Sendlog:
    def slog(self,ip,port,filename):
        self.port = port
        self.ip = ip
        self.filename = filename
        ADDR = (self.ip,self.port)
        BUFSIZE = 1024
        FILEINFO_SIZE=struct.calcsize('128s32sI8s')
        sendSock = socket(AF_INET,SOCK_STREAM,0)
        sendSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        sendSock.connect(ADDR)
        fhead=struct.pack('128s11I',self.filename,0,0,0,0,0,0,0,0,os.stat(self.filename).st_size,0,0)
        sendSock.send(fhead)
        fp = open(self.filename,'rb')
        while 1:
           filedata = fp.read(BUFSIZE)
           if not filedata: break
           sendSock.send(filedata)
        print "文件传送完毕，正在断开连接..."
        fp.close()
        sendSock.close()
        print "连接已关闭..."
        time.sleep(10)
