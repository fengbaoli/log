# -*- coding:utf-8 -*-
__author__ = '343715'
import logging
import os

class logdebug:
    def loginfo(self,message):
        self.message = message
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.getcwd()+"/logs/collect-info.log",
                    filemode='w')
        logging.info(self.message)
    def logerror(self,message):
        self.message = message
        logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.getcwd()+"/logs/collect-error.log",
                    filemode='w')
        logging.error(message)
