# -*- coding:utf-8 -*-
from socket import *
import struct
import  os,repr
import sys
import  platform
if 'Windows' in platform.system():
    sys.path.append(os.getcwd()+'\lib')
else:
    sys.path.append(os.getcwd()+'/lib')

from debug import logdebug
log = logdebug()

def Collog(port,BUFSIZE,receive_path):
    while True:
        ADDR = ('0.0.0.0',port)
        BUFSIZE = BUFSIZE
        FILEINFO_SIZE=struct.calcsize('128s32sI8s')
        recvSock = socket(AF_INET,SOCK_STREAM,0)
        recvSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
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
        message = "获取文件:"+filename
        log.loginfo(message)
        #创建接收端存放日志路径
        message = "创建接收端存放日志路径"
        log.loginfo(message)
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
        log.loginfo(message)
        while 1:
            if restsize>BUFSIZE:
                filedata=conn.recv(BUFSIZE)
            else:
                filedata = conn.recv(restsize)
            if not filedata:
                break
            fp.write(filedata)
            restsize = restsize-len(filedata)
            if restsize == 0:
                break
        message= "接收文件 %s 完毕，正在断开连接..." % filename
        log.loginfo(message)
        fp.close()
        conn.close()
        recvSock.close()
        message= "连接已关闭..."
        log.loginfo(message)



if __name__ == "__main__":
    port = 8000
    BUFSIZE = 1024
    receive_path ="logs"
    Collog(port,BUFSIZE,receive_path)
