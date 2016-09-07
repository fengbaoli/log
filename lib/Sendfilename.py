# -*- coding:utf-8 -*-
import os,sys
import  datetime
import time
from socket import *
import  time
import  struct,linecache
import  platform
if 'Windows' in platform.system():
    sys.path.append(os.getcwd()+'..\lib')
else:
    sys.path.append(os.getcwd()+'../lib')
from debug import logdebug
log = logdebug()

class Sendfilename:
    def __init__(self,filename,ip,port):
        self.filename = filename
        self.ip = ip
        self.port = port
    def sendfilename(self):
        ADDR = (self.ip,self.port)
        BUFSIZE = 1024
        FILEINFO_SIZE = struct.calcsize('128s32sI8s')
        sendSock = socket(AF_INET,SOCK_STREAM,0)
        while True:
                try:
                    sendSock.connect(ADDR)
                    break
                except:
                    (ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
                    message = "Connect server failed:"+str(ErrorValue)
                   #log.logerror(message)
                    #time.sleep(5)
                    message="开始重新连接....."
                    #log.logerror(message)
                    continue
        message = "成功连接远端服务器，进行数据发送准备"
        fhead=struct.pack('128s11I',self.filename,0,0,0,0,0,0,0,0,os.stat(self.filename).st_size,0,0)
        sendSock.send(fhead)
        sendSock.shutdown(0)
        sendSock.close()
