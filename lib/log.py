# -*- coding:utf-8 -*-
__author__ = 'blfeng'
import sys,os
sys.path.append(os.getcwd()+'../lib')

import os

from debug import logdebug

log = logdebug()

class Collectlog:
    #初始化配置读取的行为0
    def getfile_count(self,configfile,path):
        filecount_name={}
        self.path = path
        self.configfile = configfile
        #生产配置文件
        file = open(self.configfile,"w+")
        for root, dirs, files in os.walk(self.path):
            for filename in files:
                counts = 0
                endsig = os.path.splitext(filename)[1]
                if endsig == ".log":
                   contexts=(root+"/"+filename+":"+filename+":"+str(counts)+"\n")
                   file.write(contexts)
        file.close()
    def gen_new_config(self,new_filepath_name,path):
        self.path = path
        self.new_filepath_name = new_filepath_name
        #初始化
        if os.path.exists(self.new_filepath_name):
            os.remove(self.new_filepath_name)
        #生产配置文件
        file = open(self.new_filepath_name,"a")
        for root, dirs, files in os.walk(self.path):
            for filename in files:
                contexts=(root+"/"+filename+"\n")
                file.write(contexts)
        file.close()
    def gen_old_config(self,configfile,old_filepath_name):
        self.configfile = configfile
        self.old_filepath_name = old_filepath_name
        cfile = open(self.configfile)
        #初始化
        if os.path.exists(self.old_filepath_name):
            os.remove(self.old_filepath_name)
        gen_cfile = open(self.old_filepath_name,"a")
        for t in cfile.readlines():
            contents = t.strip().split(':')
            filepath_name=contents[0]
            gen_cfile.write(filepath_name+"\n")
        cfile.close()
        gen_cfile.close()

    def addlog(self,old_filepath_name,new_filepath_name,configfile):
        self.old_filepath_name = old_filepath_name
        self.new_filepath_name = new_filepath_name
        self.configfile = configfile
        #添加新采集日志文件名到配置文件
        fold = open(self.old_filepath_name)
        old_contents = fold.readlines()
        fold.close()
        fnew = open(self.new_filepath_name)
        new_contexts = fnew.readlines()
        fnew.close()
        cfile = open(self.configfile,"a")
        add_contexts = [i for i in new_contexts if i not in old_contents]
        if add_contexts:
            for t in add_contexts:
                filename = t.split("/")[-1]
                counts = 0
                endsig = os.path.splitext(filename)[1]
                if endsig == ".log":
                   contents = t.strip("\n").strip()+":"+filename.strip("\n").strip()+":"+str(counts)
                   cfile.write(contents+"\n")
        cfile.close()



    def dellog(self,new_filepath_name,configfile):
        self.new_filepath_name = new_filepath_name
        self.configfile = configfile
        logsname = open(self.new_filepath_name)
        new_log_contents = logsname.readlines()
        for t in new_log_contents:
            logname = t.strip("\n")
            if not os.path.exists(logname):
                cmd ="sed -i '/%s/d' %s " % (logname,self.configfile)
                os.system(cmd)
        logsname.close()
