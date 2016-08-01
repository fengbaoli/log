# -*- coding:utf-8 -*-
__author__ = 'blfeng'
import logging
import os

class logdebug:
    def loginfo(self,message):
        self.message = message
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.getcwd()+"/logs/collect.log",
                    filemode='w')
        logging.info(self.message)
    def logerror(self,message):
        self.message = message
        logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.getcwd()+"/logs/collect.log",
                    filemode='w')
        logging.error(message)
