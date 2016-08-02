# -*- coding:utf-8 -*-
__author__ = 'blfeng'
import  platform

class Platform:

    def isWindowsSystem(self):
        mes =  'Windows' in platform.system()
        return  mes

    def isLinuxSystem(self):
        mes = 'Linux' in platform.system()
        return  mes
