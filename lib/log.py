# -*- coding:utf-8 -*-
__author__ = 'blfeng'
import  os
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
                contexts=(root+"/"+filename+":"+filename+":"+str(counts)+"\n")
                file.write(contexts)
        file.close()
    def gencounts(self,configfile,filepath,filename,counts):
        self.configfile = configfile
        self.counts = counts
        self.filepath = filepath
        self.filename = filename 
        file = open(self.configfile)
        for t in file.readlines():
            tmpconffile= open("tmpconf.txt","a")
            newcontents=self.filepath+":"+self.filename+":"+str(self.counts)+"\n"
            tmpconffile.write(newcontents)
            tmpconffile.close()
        file.close()
