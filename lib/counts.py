# -*- coding:utf-8 -*-
__author__ = 'blfeng'
class Counts:
    def __init__(self,filepath_name):
        self.filepath_name = filepath_name
    def counts(self):
        count = 0
        thefile = open(self.filepath_name, 'rb')
        while True:
            buffer = thefile.read(8192*1024)
            if not buffer:
                break
            count += buffer.count('\n')
        thefile.close( )
        return  count
