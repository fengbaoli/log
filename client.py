# -*- coding:utf-8 -*-
__author__ = 'blfeng'
import  sys,os
sys.path.append(os.getcwd()+'/lib')
import os,datetime
from log import  Collectlog
import time,struct,linecache
from socket import *
from  Sendlog import  Sendlog
import ConfigParser
from debug import logdebug


#读取配置文件
cf = ConfigParser.ConfigParser()
cf.read(os.getcwd()+"/conf/collog.conf")
logpath = cf.get("client","logpath")
configfile = cf.get("client","configfile")
ip = cf.get("client","ip")
port = int(cf.get("client","port"))
interval_time = int(cf.get("client","interval_time"))



#初始化配置文件
#Collectlog().getfile_count(configfile,logpath)
#开始采集

def collectdata(logpath,configfile,ip,port,interval_time):
    while True:
        if not  os.path.exists(os.getcwd()+"/configfile"):
            message = “xx”
            log.logerror(message)
        #发送数据
        s= Sendlog(configfile=configfile,ip=ip,port=port)
        s.sendlog()
        #判断配置文件是否有更新文件
        if not os.path.exists(os.getcwd()+"/"+"tmp"):
            os.mkdir(os.getcwd()+"/"+"tmp")
        gen_cfile = os.getcwd()+"/"+configfile
        old_filepath_name = (os.getcwd()+"/tmp/old.conf")
        new_filepath_name = (os.getcwd()+"/tmp/new.conf")
        Collectlog().gen_old_config(configfile=gen_cfile,old_filepath_name=old_filepath_name)
        #生成临时配置文件
        Collectlog().gen_new_config(new_filepath_name=new_filepath_name,path=logpath)
        #更新
        Collectlog().addlog(old_filepath_name=old_filepath_name,new_filepath_name=new_filepath_name,configfile=configfile)
        #删除临时文件
        if os.path.exists(old_filepath_name):
            os.remove(old_filepath_name)
        elif os.path.exists(new_filepath_name):
            os.remove(new_filepath_name)
        else:
            pass
        #更新已经删除日志文件到配置文件
        Collectlog().dellog(new_filepath_name=new_filepath_name,configfile=gen_cfile)
        time.sleep(interval_time)


if __name__ =="__main__":

    collectdata(logpath,configfile,ip,port,interval_time)
