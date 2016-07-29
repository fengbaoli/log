# -*- coding:utf-8 -*-
__author__ = 'blfeng'
import  os

class Collectlog:
    #初始化配置读取的行为0
    def getfile_count(self,configfile,path):
        filecount_name={}
        self.path = path
        self.configfile = configfile
        for root, dirs, files in os.walk(self.path):
            for filename in files:
                file = open(self.configfile,"a")
                #count = len(open(root+"/"+filename,'rU').readlines())
                counts = 0
                context=root+":"+filename+":"+str(counts)+"\n"
                file.write(context)
            file.close()
    #更新同步后，记录同步行数
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
