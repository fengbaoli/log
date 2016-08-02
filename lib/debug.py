# -*- coding:utf-8 -*-
__author__ = 'blfeng'
import logging
import os
from Platform import  Platform
platform = Platform()


class logdebug:
    def loginfo(self,message):
        self.message = message
        if platform.isLinuxSystem():
            logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.getcwd()+"/logs/collect-info.log",
                    filemode='w')
        else:
            logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.getcwd()+"\logs\collect-info.log",
                    filemode='w')
        logging.info(self.message)
    def logerror(self,message):
        self.message = message
        if platform.isLinuxSystem():
            logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.getcwd()+"/logs/collect-error.log",
                    filemode='w')
        else:
            logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.getcwd()+"\logs\collect-error.log",
                    filemode='w')
        logging.error(message)
