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
from counts import Counts
log = logdebug()

class Sendlog:
    def __init__(self,configfile,ip,port):
        self.configfile =configfile
        self.ip = ip
        self.port = port
    def sendlog(self):
        cfile = open(self.configfile)
        num = 1
        for t in cfile.readlines():
            #读取配置文件
            contents = t.strip().split(':')
            filepath_name=contents[0]
            filename=contents[1]
            old_counts =int(contents[2])
            #文件被删除后，直接跳过
            if not os.path.exists(filepath_name):
                message = "文件:"+filepath_name+"已经被删除不需要发送"
                log.loginfo(message)
                continue
            #目前文件行数
            #now_counts = len(open(filepath_name,'rU').readlines())
            Statistics_num = Counts(filepath_name)
            now_counts = Statistics_num.counts()
            message = "文件"+filepath_name+"目前行数为"+str(now_counts)
            log.loginfo(message)
            if now_counts < old_counts:
                message = "文件"+filename+"记录数被重置，需要重新发送数据"
                log.loginfo(message)
                #读取配置
                tt = filepath_name.replace('/','\/')
                new_content = "%s:%s:0" % (tt,filename)
                cmd ='sed -i \'%ds/^.*$/%s/\'  %s' % (num,new_content,self.configfile)
                os.system(cmd)
                num=num+1
                time.sleep(10)
                continue
            message="文件"+filename+"更新配置文件:行数为"+str(now_counts)
            log.loginfo(message)
            #更新配置文件
            tt = filepath_name.replace('/','\/')
            new_content = "%s:%s:%s" % (tt,filename,now_counts)
            cmd ='sed -i \'%ds/^.*$/%s/\'  %s' % (num,new_content,self.configfile)
            os.system(cmd)
            num=num+1
            message = "文件"+filename+"配置文件更新完毕"
            log.loginfo(message)
            if now_counts == 0 :
                message = "文件"+filename+"记录为空,没有数据可以发送"
                log.loginfo(message)
                #time.sleep(5)
                continue
            if now_counts == old_counts:
                message = "文件"+filename+"记录数没有更新，没有新数据"
                log.loginfo(message)
                #time.sleep(5)
                continue
            #连接服务端
            message="开始连接服务端......."
            log.loginfo(message)

            ADDR = (self.ip,self.port)
            BUFSIZE = 1024
            FILEINFO_SIZE=struct.calcsize('128s32sI8s')
            sendSock = socket(AF_INET,SOCK_STREAM,0)
            sendSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
            while True:
                try:
                    sendSock.connect(ADDR)
                    break
                except:
                    (ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
                    message = "Connect server failed:"+str(ErrorValue)
                    log.logerror(message)
                    time.sleep(5)
                    message="开始重新连接....."
                    log.logerror(message)
                    continue
            message = "成功连接远端服务器，进行数据发送准备"
            log.loginfo(message)
             #发送数据
            if old_counts < now_counts:
                #开始发送数据
                message= "文件"+filename+"开始发送数据"
                log.loginfo(message)
                fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filepath_name).st_size,0,0)
                sendSock.send(fhead)
                #读取文件数据到缓存
                message = "读取文件:"+filepath_name+"数据到缓存"
                log.loginfo(message)
                for  tmpfiledata in linecache.getlines(filepath_name)[old_counts:now_counts]:
                        filedata =  ''.join(tmpfiledata)
                        sendSock.send(filedata)
                message = "缓存数据读取完毕，清理缓存"
                log.loginfo(message)
                linecache.clearcache()
                message= "文件"+filename+"数据发送完毕"
                log.loginfo(message)
                message= "文件"+filename+"文件传送完毕，正在断开连接..."
                log.loginfo(message)
            sendSock.close()
            message = "文件"+filename+"连接已关闭..."
            log.loginfo(message)
            time.sleep(5)
