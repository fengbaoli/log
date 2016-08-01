# -*- coding:utf-8 -*-
from socket import *
import struct
import  os,repr
receive_path="logs"
while True:
    ADDR = ('0.0.0.0',8000)
    BUFSIZE = 1024
    FILEINFO_SIZE=struct.calcsize('128s32sI8s')
    recvSock = socket(AF_INET,SOCK_STREAM,0)
    recvSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    recvSock.bind(ADDR)
    recvSock.listen(True)
    print "等待连接..."
    conn,addr = recvSock.accept()
    print "客户端已连接—> ",addr
    fhead = conn.recv(FILEINFO_SIZE)
    filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)
    #获取发送端的文件名
    filename=filename.split('\x00')[0]
    #创建接收端存放日志路径
    receive_full_path = os.getcwd()+"\\"+receive_path+"\\"
    if not os.path.exists(receive_full_path):
        os.mkdir(receive_full_path)

    filename = receive_full_path+filename
    fp = open(filename,'a')
    restsize = filesize
    print "正在接收文件... ",
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
    print "接收文件完毕，正在断开连接..."
    fp.close()
    conn.close()
    recvSock.close()
    print "连接已关闭..."
