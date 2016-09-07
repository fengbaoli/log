# -*- coding:utf-8 -*-
from socket import *
import struct
import  os,repr
import sys
import  platform
import  re
import time
import datetime

if 'Windows' in platform.system():
    sys.path.append(os.getcwd()+'\lib')
else:
    sys.path.append(os.getcwd()+'/lib')

from debug import logdebug
log = logdebug()


def VisitDir(path,days):
    """
    :rtype : object
    """
    li = os.listdir(path)
    for p in li :
        pathnamne = os.path.join(path,p)
        if not os.path.join(pathnamne):
            VisitDir(pathnamne,days)
        else:
            ltime =  int(os.path.getatime(pathnamne))
            save_days = days
            save_seconds = save_days*24*3600
            ntime = int(time.time())-save_seconds
            if ltime<=ntime :
                message = "文件 %s 已经超过三天,正在删除" % (pathnamne)
                #log.loginfo(message)
                os.remove(pathnamne)




def Collog(port,BUFSIZE,receive_path,save_days):
    while True:
        #文件进行备份保留三天的数据
        curr_hour = datetime.datetime.now().hour
        if curr_hour == 5:
            bak_dir = os.getcwd()+"\\logbak"
            if not os.path.exists(bak_dir):
                os.mkdir(bak_dir)
            #文件复制
            logs_dir = os.getcwd()+"\\logs"
            li = os.listdir(logs_dir)
            for p in li :
                filename = os.path.join(logs_dir,p)
                currdata = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                targetfilename = filename.split("\\")[-1]+"-"+currdata+"-bak"
                bakfile= bak_dir+"\\"+targetfilename
                if not os.path.exists(bakfile):
                    message = "开始备份日志文件 %s" %(filename)
                    log.loginfo(message)
                    file1 = open(filename,'r')
                    file2 = open(bak_dir+"\\"+targetfilename,'w')
                    file2.write(file1.read())
                    file1.close()
                    file2.close()
                    message = "备份日志文件 %s  完成" % (filename)
                    log.loginfo(message)
                    #源文件删除
                    message = "源文件删除 %s" %(filename)
                    log.loginfo(message)
                    if filename.split("\\")[-1] == "collect-info.log":
                        pass
                    else:
                        os.remove(filename)
                else:
                    message="日志文件已经备份，不需要再备份"
                    log.loginfo(message)
        ADDR = ('0.0.0.0',port)
        BUFSIZE = BUFSIZE
        FILEINFO_SIZE=struct.calcsize('128s32sI8s')
        recvSock = socket(AF_INET,SOCK_STREAM,0)
        recvSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        #recvSock.settimeout(60)
        recvSock.bind(ADDR)
        recvSock.listen(True)
        message = "等待连接..."
        log.loginfo(message)
        conn,addr = recvSock.accept()
        network = []
        for  ipaddr in addr:
            network.append(ipaddr)
        message = "客户端已连接—>"+str(ipaddr)
        log.loginfo(message)
        fhead = conn.recv(FILEINFO_SIZE)
        filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)
        #获取发送端的文件名
        filename=filename.split('\x00')[0]
        message = "读取文件名:"+filename
        log.loginfo(message)
        if filename == "log.conf":
            continue
        #创建接收端存放日志路径
        message = "创建接收端存放日志路径"
        #log.loginfo(message)
        if  'Windows' in platform.system():
            receive_full_path = os.getcwd()+"\\"+receive_path+"\\"
        else:
            receive_full_path = os.getcwd()+"/"+receive_path+"/"
        if not os.path.exists(receive_full_path):
            os.mkdir(receive_full_path)
        filename = receive_full_path+filename
        fp = open(filename,'a')
        restsize = filesize
        message = "正在接收文件:"+filename
        #log.loginfo(message)
        while 1:
            if restsize>BUFSIZE:
                filedata=conn.recv(BUFSIZE)
            else:
                filedata = conn.recv(restsize)
            if not filedata:
                break
            data = filedata.replace("test","password")
            fp.write(data)
            restsize = restsize-len(filedata)
            if restsize == 0:
                break
        message= "接收文件 %s 完毕，正在断开连接..." % filename
        #log.loginfo(message)
        fp.close()
        conn.close()
        recvSock.close()
        message= "连接已关闭..."
        #log.loginfo(message)
         #备份文件过期删除
        days  = save_days
        path = r"d:\job-agent-logs\log-master\logbak"
        VisitDir(path,days)
if __name__ == "__main__":
    port = 8000
    BUFSIZE = 1024
    receive_path ="logs"
    days = 3
    Collog(port,BUFSIZE,receive_path,save_days=days)
