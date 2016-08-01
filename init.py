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
Collectlog().getfile_count(configfile,logpath)
